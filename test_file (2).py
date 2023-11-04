from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

import  pandas

input_path = './input.xlsx'
df_input = pandas.read_excel(input_path)

# print(df_input['Player ID'][0])


driver = webdriver.Chrome()

# driver.get('https://www.midasbuy.com/midasbuy/ot/redeem/pubgm?from=undefined#')

time.sleep(3)

# print(type(df_input["Code 60"][13]))

# Input ID
def input_id(id):
    driver.find_element(By.XPATH, "//span[@class='UserTabBox_switch_btn__428iM']").click()

    id_input = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Player ID')]").clear()
    time.sleep(1.2)
    # print(df_input['Player ID'][i],i,'iiiiiiiiiiii')
    id_input = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Enter Player ID')]").send_keys(id)
    time.sleep(2.1)
    driver.find_element(By.XPATH, "//div[@class='PlayerIdEnterPop_btn_wrap__CxT-p']//div[@class='Button_btn_wrap__utZqk']//div[@class='Button_btn__P0ibl Button_btn_primary__1ncdM']//div//div[contains(text(),'OK')]").click()
    time.sleep(2.3)



# Required Redeem Codes
# def required_redeem_codes(UC_Coins,UC_alloted):
#     redeem_codes = []
#     # UC_Coins = df_input["UC Coins"][i]
#     UC = ""
#     flag = ''
#     for x in range(len(uc_multiples)-1,-1,-1):
#         # print(x)
#         if UC_alloted%UC_Coins[x]==0:
#             print(UC_Coins[x],UC_alloted%UC_Coins[x],UC_alloted)
#             redeem_codes = []
#             redeem_codes = [UC_Coins[x] for z in range(int(UC_alloted/UC_Coins[x]))]
#             print(redeem_codes,'in loop')
#             flag =True
#             break
#     if flag:
#         return redeem_codes
#
#     for x in range(len(uc_multiples)-1,-1,-1):
#         # print(x)
#         # if UC_alloted%UC_Coins[x]==0:
#         #     print(UC_Coins[x],UC_alloted%UC_Coins[x],UC_alloted)
#         #     redeem_codes = []
#         #     redeem_codes = [UC_Coins[x] for z in range(int(UC_alloted/UC_Coins[x]))]
#         #     print(redeem_codes,'in loop')
#         #     break
#         if UC_alloted-UC_Coins[x]<0:
#             continue
#         UC_alloted -= UC_Coins[x]
#         redeem_codes.append(UC_Coins[x])
#     return redeem_codes



from itertools import combinations

def required_redeem_codes(target_sum, numbers):
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            if sum(combo) == target_sum:
                return combo
    return None

uc_multiples = [60, 325, 660, 1800, 3850, 8100]
# target_sum = 720

# result = find_combination(target_sum, uc_multiples)

# if result:
#     print(f"Combination found: {result}")
# else:
#     print("No combination found.")






# Log In
def log_in():
    login_btn = driver.find_element(By.XPATH,"//div[@class='MobileNav_sign_in__qA2oK']").click()

    iframe  = driver.find_element(By.ID,"login-iframe")
    driver.switch_to.frame(iframe)

    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@placeholder='Please enter your email account']").send_keys('4@buymondo.com')
    driver.find_element(By.XPATH,"//input[@placeholder='Enter password']").send_keys('sa123456')

    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='btn sign-in-btn']").click()
    driver.switch_to.default_content()
    time.sleep(6.3)

    cookie_close = driver.find_elements(By.XPATH,"//div[@class='PopTitle_2_close_btn__+3O9n']//i[@class='i-midas:close icon']")
    if cookie_close:
        driver.find_element(By.XPATH,
                            "//div[@class='PopTitle_2_close_btn__+3O9n']//i[@class='i-midas:close icon']").click()
        time.sleep(1.1)




log_in()


uc_multiples = [60,325,660,1800,3850,8100]

# loop for id's
while True:
    # print()
    id = str(input('Enter Id : ')).strip()
    UC_alloted = str(input('Enter UC alloted : ')).strip()
    UC_alloted = int(UC_alloted)

    for i in range(1):


        input_id(id)

        required_codes = required_redeem_codes(UC_alloted,uc_multiples)
        print(required_codes)


        for l in range(len(required_codes)):
            for n in range(len(df_input)-1):
                temp_code = df_input['Code '+str(required_codes[l])][n]
                if type(temp_code)==type('s'):
                    time.sleep(3)
                    # uc_code = df_input['Code ' + str(UC)][y]


                    #
                    driver.find_element(By.XPATH, "//input[@placeholder='Please enter a redeem code']").clear()
                    time.sleep(1.4)
                    driver.find_element(By.XPATH, "//input[@placeholder='Please enter a redeem code']").send_keys(temp_code)
                    time.sleep(2)



                    driver.find_element(By.XPATH,"//div[contains(@class,'RedeemGiftBox_btn_box__yNyi-')]//div[contains(@class,'Button_btn_wrap__utZqk')]//div[contains(@class,'Button_btn__P0ibl Button_btn_primary__1ncdM')]//div//div[contains(text(),'OK')]").click()
                    time.sleep(1.5)
                    driver.find_element(By.XPATH, "//div[contains(text(),'Submit')]").click()


                    df_input.at[n,'Code ' + str(required_codes[l])] =  ""
                    data = df_input
                    # print(data)
                    print("nth Number of redeem code",n)
                    data.to_excel(input_path)
                    break

    print()
    print()

    #     Enter Redeem code




# time.sleep(5)





import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
import time
#
# browser = "chrome"
#
# if browser == "chrome":
driver = webdriver.Chrome(ChromeDriverManager().install())
# elif browser == "firefox":
#     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# elif browser == "safari":
#     driver = webdriver.Safari()
# else:
#     print("enter valid browser name")

driver.implicitly_wait(10)
driver.get("https://www.facebook.com")
print(driver.title)
create = driver.find_element(By.ID, "u_0_2").click()

first_name = driver.find_element(By.ID, "u_1_b")
sur_name = driver.find_element(By.ID, "u_1_d")
mobile = driver.find_element(By.ID, "u_1_g")
password = driver.find_element(By.ID, "password_step_input")
# day = driver.find_element(By.ID, "day")
# y = Select(day)

workbook = xlrd.open_workbook("face.xlsx")
sheet = workbook.sheet_by_name("fb")

rowcount = sheet.nrows
columncount = sheet.ncols
# print(rowcount)
# print(columncount)

for x in range(1, rowcount):
    firstname = sheet.cell_value(x, 0)
    surname = sheet.cell_value(x, 1)
    mobilenumber = sheet.cell_value(x, 2)
    passcode = sheet.cell_value(x, 3)
    # divas = sheet.cell_value(x, 4)

    first_name.send_keys(firstname)
    sur_name.send_keys(surname)
    mobile.send_keys(mobilenumber)
    password.send_keys(passcode)
    # y.select_by_value(divas)
    # print(firstname+" "+surname)

    time.sleep(4000)
# driver.quit()

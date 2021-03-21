import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

#
# browser = "chrome"
# #
# if browser == "chrome":
options = webdriver.ChromeOptions()
options.headless= True

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# elif browser == "firefox":
#     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# elif browser == "safari":
#     driver = webdriver.Safari()
# else:
#     print("enter valid browser name")

driver.implicitly_wait(10)
driver.get("https://www.slideshare.net")
print(driver.title)
login = driver.find_element(By.ID, "login").click()
email = driver.find_element(By.ID, "user_login").send_keys("k.dabbu@gmail.com")
password = driver.find_element(By.ID, "user_password").send_keys("ArunSlide1")
remember = driver.find_element(By.ID, "remember").click()
enter = driver.find_element(By.XPATH, "//*[@id='login_from_loginpage']/span[1]").click()
explore = driver.find_element(By.XPATH, "//*[@id='main-nav']/div[2]/div/div/ul/li[2]/strong/a").click()

driver.implicitly_wait(10)
# driver.get_screenshot_as_file('ss2.png')
profile = driver.find_element(By.XPATH, "//*[@id='main-nav']/nav/section/ul[1]/li[2]/a")
# driver.get_screenshot_as_file('ssqwe.png')
driver.implicitly_wait(10)
#
S = lambda X: driver.execute_script("return document.body.parentNode.scroll" + X)
driver.set_window_size(S("Width"), S("Height"))
driver.find_element_by_tag_name("body").screenshot("full23.png");
act_chains = ActionChains(driver)
act_chains.move_to_element(profile).perform()
logout = driver.find_element(By.XPATH, "//*[@id='user-dropdown']/li[17]/a").click()

# first_name = driver.find_element(By.ID, "u_1_b")
# sur_name = driver.find_element(By.ID, "u_1_d")
# mobile = driver.find_element(By.ID, "u_1_g")
# password = driver.find_element(By.ID, "password_step_input")
# day = driver.find_element(By.ID, "day")
# p = Select(day)
#
# month = driver.find_element(By.ID, "month")
# q = Select(month)
#
# year = driver.find_element(By.ID, "year")
# r = Select(year)
#
# female_gender = driver.find_element(By.ID, "u_1_2")
# male_gender = driver.find_element(By.ID, "u_1_3")
#
# workbook = xlrd.open_workbook("face.xlsx")
# sheet = workbook.sheet_by_name("fb")
#
# rowcount = sheet.nrows
# columncount = sheet.ncols
# # print(rowcount)
# # print(columncount)
#
# for x in range(1, rowcount):
#     firstname = sheet.cell_value(x, 0)
#     surname = sheet.cell_value(x, 1)
#     mobilenumber = sheet.cell_value(x, 2)
#     passcode = sheet.cell_value(x, 3)
#     divas = sheet.cell_value(x, 4)
#     tingal = sheet.cell_value(x, 5)
#     varsh = sheet.cell_value(x, 6)
#
#     first_name.send_keys(firstname)
#     sur_name.send_keys(surname)
#     mobile.send_keys(mobilenumber)
#     password.send_keys(passcode)
#     p.select_by_value(divas)
#     q.select_by_value(tingal)
#     r.select_by_value(varsh)
#
#     linga = sheet.cell_value(x, 7)
#     if linga == "female":
#         female_gender.click()
#     else:
#         male_gender.click()
#     # print(firstname+" "+surname)

time.sleep(5)
driver.quit()

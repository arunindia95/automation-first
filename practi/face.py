import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
import time

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
# create = driver.find_element(By.ID, "u_0_2_yA").click()
create = driver.find_element(By.XPATH, "//a[contains(@id,'u_0_2')]").click()
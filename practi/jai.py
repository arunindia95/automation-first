from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import time

browser= "Chrome"

if browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser =="firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser == "safari":
    driver = webdriver.Safari()
else:
    print("valid br ")

driver.implicitly_wait(10)
driver.get("https:/www.facebook.com")

'''
signup= driver.find_element(By.ID,"u_0_2")
signup.click()
username= driver.find_element(By.ID,"u_1_b").send_keys("Surya")
surname= driver.find_element(By.NAME,"lastname").send_keys("India")
email= driver.find_element(By.ID,"u_1_g").send_keys("surya@gmail.com")
reenter_email= driver.find_element(By.ID,"u_1_j").send_keys("surya@gmail.com")
password= driver.find_element(By.ID,"password_step_input").send_keys("Surya123@")

birthday= driver.find_element(By.ID,"day")
y= Select(birthday)
y.select_by_value("23")
birthmonth= driver.find_element(By.ID,"month")
y=Select(birthmonth)
y.select_by_visible_text("Jun")
birthyear= driver.find_element(By.ID,"year")
y=Select(birthyear)
y.select_by_visible_text("1995")

gender= driver.find_element(By.ID,'u_1_5').click()

time.sleep(10)
driver.quit()
'''
'''
page= driver.find_element(By.LINK_TEXT,"Create a Page").click()

time.sleep(10)
driver.quit()
'''

act_ch= ActionChains(driver)
imag= driver.find_element(By.TAG_NAME,"img")

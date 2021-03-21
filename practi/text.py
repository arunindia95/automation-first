import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions

# username = input('Enter your Username ')
# password = input('Enter your Password ')
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.facebook.com")
username = input('Enter your Username ')
password = input('Enter your Password ')
user = driver.find_element(By.ID,"email").send_keys(username)
# get_source = driver.page_source
# search_text= "people"
# print(search_text in get_source)
# tetx = driver.find_element(By.XPATH, "/html/body").text
# # print(driver.find_element_by_xpath("/html/body").text)
# print(tetx)
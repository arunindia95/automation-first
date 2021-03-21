import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# options= Webdriver.ChromeOptions()
# options.add_arguement(“--incognito”)
# driver= webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.implicitly_wait(10)
driver.maximize_window()
google = "https://www.google.com"
# driver.get("('https://www.google.com', 'google')")
driver.get(google)
# driver.execute_script("window.open('https://www.facebook.com')","new window")
# driver.execute_script("window.open('about:blank')","new window")
driver.execute_script("window.open('https://www.facebook.com', 'fb')", "")
driver.execute_script("window.open('https://www.instagram.com','insta')", "third")
# driver.switch_to.window(driver.window_handles[0])
driver.switch_to.window(" ")

# Lets open https://www.bing.com/ in the second tab
# driver.execute_script("window.open('about:blank',
#                       'secondtab');")
# driver.switch_to.window("secondtab")
# driver.get('https://www.bing.com/')


time.sleep(10)
driver.quit()

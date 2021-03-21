import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://sqengineer.com/practice-sites/practice-tables-selenium')
# link = driver.find_elements(By.XPATH,"//*[@id='table1']/tbody/tr[1]/th[3]")
link = driver.find_elements(By.XPATH, "//*[@id='table1']/tbody/tr/td")
n = 0
for x in link:
    if n % 3== 2:
        print(x.text)
    n = n + 1

# table = driver.find_element(By.XPATH, "//*[@id='table1']/tbody")
# for table in range(12):
#     if table % 3 == 0:
#         print(table)
# rows = 1 + len(driver.find_elements(By.XPATH, "//*[@id='table1']/tbody/tr"))
# cols = len(driver.find_elements(By.XPATH, "//*[@id='table1']/tbody/tr/td"))

driver.quit()

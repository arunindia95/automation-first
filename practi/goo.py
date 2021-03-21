import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.google.com")
google = driver.find_element(By.XPATH,"//input[@class='gLFyf gsfi']").send_keys("selenium")
# suggestions = driver.find_elements(By.XPATH, "//li[contains(@role, 'presentation')]")
# for x in suggestions:
#     print(x.text)
suggestions = driver.find_elements(By.XPATH, "//div[@class='sbl1']//span[contains(text(),'selenium')]")
# suggestions = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div[1]/div[2]/div[2]/ul/li[1]")

print(len(suggestions))
for x in suggestions:
    print(x.text)
    # time.sleep(5)

# suggestions[8].click()
print("we are clicking on", suggestions[3].text)
suggestions[3].click()

linklist = driver.find_elements(By.TAG_NAME,"a")
print(len(linklist))
for y in linklist:
    print(y.text)
    print(y.get_attribute("href"))
# print(suggestions)
    # if (x.text == "selenium ide"):
    #     x.click()
    #     break
# time.sleep(5)
driver.quit()
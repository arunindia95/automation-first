import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://guide.blazemeter.com/hc/en-us")
cats = driver.find_elements(By.XPATH, "//ul[@id='categories']/li")
print(len(cats))
m= []
# k= cats.sort()
# for x in k:
#     print(x.text)
for x in cats:
    res = m.append(x.text)
    print(m.sort())

    # k = x.text
    # print(m.append(k))
    # print(x.text)

time.sleep(5)
driver.quit()

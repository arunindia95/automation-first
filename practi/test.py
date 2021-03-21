import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

options= webdriver.ChromeOptions()
options.add_argument("--incognito")
driver= webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://prefeitura.pbh.gov.br/saude/licitacao/pregao-eletronico-151-2020")
time.sleep(5)
pubdate = driver.find_element(By.CSS_SELECTOR,"span[class='col-sm-6 lbl-licitacao']").text
print(pubdate)
# driver.quit()
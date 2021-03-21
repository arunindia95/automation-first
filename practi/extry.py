from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import xlrd
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://www.facebook.com")
create = driver.find_element(By.ID, "u_0_2").click()
first_name = driver.find_element(By.NAME, "firstname")
last_name = driver.find_element(By.NAME, "lastname")

workbook = xlrd.open_workbook("face.xlsx")
sheet = workbook.sheet_by_name("fb")

rowcount = sheet.nrows
columncount = sheet.ncols


for x in range(1, rowcount):
    firstname= sheet.cell_value(x,0)
    surname= sheet.cell_value(x,1)

    first_name.send_keys(firstname)
    last_name.send_keys(surname)

    time.sleep(100)





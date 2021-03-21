import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time



# browser_name= "Chrome"
# if browser_name== "Chrome":
#     driver= webdriver.Chrome(ChromeDriverManager().install())
# elif browser_name== "Firefox":
#     driver= webdriver.Firefox(GeckoDriverManager().install())
# elif browser_name== "Safari":
#     driver= webdriver.Safari()
# else:
#     print("Enter valid browser")


workbook = xlrd.open_workbook("face.xlsx")
sheet = workbook.sheet_by_name("fb")

rowcount = sheet.nrows
columncount = sheet.ncols
# print(rowcount)
# print(columncount)

for x in range(1, rowcount):
    firstname = sheet.cell_value(x, 0)
    surname = sheet.cell_value(x, 1)
    mobilenumber = sheet.cell_value(x, 2)
    passcode = sheet.cell_value(x, 3)

    print(firstname)
import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browser = "chrome"

if browser == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser == "safari":
    driver = webdriver.Safari()
else:
    print("enter valid browser name")

driver.implicitly_wait(10)
driver.get("https://www.slideshare.net")
print(driver.title)
login = driver.find_element(By.ID, "login").click()
email = driver.find_element(By.ID, "user_login")
password = driver.find_element(By.ID, "user_password")
remember = driver.find_element(By.ID, "remember")

workbook = xlrd.open_workbook("slide.xlsx")
sheet = workbook.sheet_by_name("credi")
rowcount = sheet.nrows
colcount = sheet.ncols

for x in range(1, rowcount):
    user = sheet.cell_value(x, 0)
    passcode = sheet.cell_value(x, 1)

    email.send_keys(user)
    password.send_keys(passcode)

enter = driver.find_element(By.XPATH, "//*[@id='login_from_loginpage']/span[1]").click()
# explore = driver.find_element(By.XPATH, "//*[@id='main-nav']/div[2]/div/div/ul/li[2]/strong/a").click()
# home = driver.find_element(By.XPATH, "//*[@id='main-nav']/div[2]/div/div/ul/li[1]/strong/a").click()
# profile = driver.find_element(By.XPATH, "//*[@id='main-nav']/nav/section/ul[1]/li[2]/a")
dropbox = driver.find_element(By.XPATH, "//*[@id='hp-featured']/div[2]/div/ul[1]/li[3]/div/a/img").click()
comment = driver.find_element(By.XPATH, "//*[@id='postComment']/div/div[2]/div/div[1]/input")

workbook = xlrd.open_workbook("comm.xlsx")
sheet = workbook.sheet_by_name("msg")
rowcount = sheet.nrows
colcount = sheet.ncols


for x in range(1, rowcount):
    comments = sheet.cell_value(x, 0)

    comment.clear()
    comment.send_keys(comments)
    post = driver.find_element(By.XPATH, "//*[@id='postComment']/div/div[2]/div/div[2]/input").click()

delet= driver.find_element(By.XPATH,"//*[@id='comment-51786336']/div/div[2]/span[1]/span/a").clear()

act_chains = ActionChains(driver)
act_chains.move_to_element(profile).perform()
logout = driver.find_element(By.XPATH, "//*[@id='user-dropdown']/li[17]/a").click()

time.sleep(5)
driver.quit()

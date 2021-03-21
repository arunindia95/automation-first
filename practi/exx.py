import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


driver= webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get("https://www.gmail.com")
driver.manage().window().fullscreen();


# sign_in= driver.find_element(By.LINK_TEXT,"Sign in")
# email= driver.find_element(By.ID,"identifierId").send_keys("Arun.konagutti23@gmail.com")
# create_acc= driver.find_element(By.XPATH,"//*[@id='ow312']/span/span").click()
# act_chains= ActionChains(driver)
myself = driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/div[2]").click()
# //*[@id="yDmH0d"]/div[5]/div/div/span[2]
# act_chains.move_to_element(myself).perform()
time.sleep(10)
driver.quit()

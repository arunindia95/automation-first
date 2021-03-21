import xlrd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://www.makemytrip.com")
# login = driver.find_elemnts(By.CSS_SELECTOR,"li.makeFlex.hrtlCenter.font10.makeRelative.lhUser").click()
# login = driver.find_elemnts(By.LINK_TEXT,"Login or Create Account").click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-cy='account']")))
scroll = driver.execute_script("window.scrollBy(0,1000)", "")
login = driver.find_element(By.CSS_SELECTOR, "li.makeFlex.hrtlCenter.font10.makeRelative.lhUser").click()
user = driver.find_element(By.ID, "username").send_keys("Arun.konagutti23@gmail.com")
conti = driver.find_element(By.CSS_SELECTOR, "button.capText.font16").click()
passcode = driver.find_element(By.ID, "password").send_keys("ArunTrip1@")
# logon = driver.find_element(By.CSS_SELECTOR, "button[data-cy='login']").click()

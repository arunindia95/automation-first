from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

# options= webdriver.ChromeOptions()
# options.add_argument("--incognito")
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.google.com")
# driver.nevgate().to("https://www.google.co.in/imghp?hl=en&tab=wi&ogbl").click()
# # enter = driver.find_element(By.XPATH, "//*[@id="rso"]/div[1]/div/div[2]/div/div[6]/div/g-more-link/a/div").send_keys("Arun")
# seach = driver.find_element(By.NAME, "btnK").click()
# images= driver.find_element(By.LINK_TEXT,"Images").click()
# driver.execute_script("window.open('http://www.facebook.com','new window')")
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(10)
driver.quit()
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")

    yield
    driver.quit()

def test_google_title(init_driver):
    assert driver.title == "Google"

def test_google_url(init_driver):
    assert driver.url == "www.google.com"



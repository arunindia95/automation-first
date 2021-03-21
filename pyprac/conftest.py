import pytest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def init_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver

    yield
    ch_driver.quit()


import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def init_ch_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver

    yield
    ch_driver.quit()


@pytest.mark.usefixtures("init_ch_driver")
class Base_Chrome_Test:
    pass


class Test_Google(Base_Chrome_Test):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"


@pytest.fixture(scope="class")
def init_driver(request):
    Ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = Ch_driver

    yield
    Ch_driver.quit()


@pytest.mark.usefixtures("init_driver")
class Base_Test():
    pass


class Test_google(Base_Test):
    def Test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"

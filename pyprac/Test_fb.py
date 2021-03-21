from selenium import webdriver
import pytest
import time


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestFb(BaseTest):
    def test_title(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://wwww.facebook.com")
        assert self.driver.title == "facebook"

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestGoo1(BaseTest):
    @pytest.mark.parametrize("username, password",

                             [("surya.vijaypur23@gmail.com", "SuryaInsta1"),
                              ("arun.konagutti@gmail.com", "asdfhuhuh")]
                             )
    def test_facebook(self, username, password):
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.instagram.com")
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        self.driver.close()
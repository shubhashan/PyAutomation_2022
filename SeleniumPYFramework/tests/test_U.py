#if you want to group the scripts according to keyname you can use as below ex: Smoke test cases
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOneU(BaseClass):
    def test_e2eu(self):
        # we are assigning the driver created as pass to homepage driver
        homepage = HomePage(self.driver)
        print("INFO: Wait for page to load")
        self.driver.implicitly_wait(9)
        homepage.shopItems().click()
        p = self.verifyLink("iphone")
        


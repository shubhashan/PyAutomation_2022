#if you want to group the scripts according to keyname you can use as below ex: Smoke test cases
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne1(BaseClass):
    def test_e2e1(self):
        #we are assigning the driver created as pass to homepage driver
        homepage= HomePage(self.driver)
        print("INFO: Wait for page to load")
        self.driver.implicitly_wait(9)
        homepage.shopItems().click()



#creating one more test case to try to add iphone click

class TestOne2(BaseClass):
    def test_e2e2(self):
        #we are assigning the driver created as pass to homepage driver
        homepage= HomePage(self.driver)
        print("INFO: Wait for page to load")
        self.driver.implicitly_wait(9)
        homepage.shopItems().click()
        checkOut= CheckOutPage(self.driver)
        cards= checkOut.getCardTitles()
        print(cards)



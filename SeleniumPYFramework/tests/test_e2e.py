#if you want to group the scripts according to keyname you can use as below ex: Smoke test cases
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_1(self):
        print("1 case")
        self.driver.title

    def test_e2e(self):
        #driver=setup
        print("INFO: Wait for page to load")
        self.driver.implicitly_wait(9)
        print("INFO: Google successfully opened in browser")
        s=self.driver.find_element_by_name("q")
        s.send_keys("Synerzip")
        print("INFO: Hit ENTER")
        s.send_keys(Keys.ENTER)
        print("INFO: Enter Synerzip and serach in google")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_partial_link_text("excellarate").click()
        print("INFO: Clcking on the official Excellarate site")
        self.driver.implicitly_wait(10)
        print("INFO: %s"%self.driver.title)
        print("INFO: %s"%self.driver.current_url)
        assert self.driver.current_url == "https://www.excellarate.com/"


        self.driver.close()
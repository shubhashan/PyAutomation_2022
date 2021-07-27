#if you want to group the scripts according to keyname you can use as below ex: Smoke test cases
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClassOne


class TestTwo(BaseClassOne):
    def test_OneClass(self,name1): #Here you have to provide the name of the fixture to pass the params
        print(name[0])
        print(name[1])
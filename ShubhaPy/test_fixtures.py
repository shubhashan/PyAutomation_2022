import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_fixture(test_openBrowser):
    print("Inside demo")
    print(test_openBrowser)
    #since the fixture "test_openBrowser" returns te driver object store it inn variable and do furtheractions
    driver=test_openBrowser
    print("-----------------")
    print(driver.current_url)
    print("--------------")
    driver.get("https://facebook.com")
    driver.implicitly_wait(5)




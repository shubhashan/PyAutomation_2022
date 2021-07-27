import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
import re


@pytest.fixture()
def test_openBrowser():
    print("INFO: Inside fixture")
    path = "C:\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.google.com")
    driver.implicitly_wait(5)
    #return the driver object so that the specific test script can make use of it can do further actions
    return(driver)
    #yield
    #print("----Closing all browser instances-----")
    #driver.close()

@pytest.fixture()
def setup():
    print("-----------------------")
    print("Setup fixture")
    print("-----------------------")

@pytest.fixture(scope="class")
def ClassFix():
    print("-----------------------")
    print("Before ..Fixture...")
    yield
    print("-----------------------")
    print("After ......Class....Fixture")

#parameterised fixtures
@pytest.fixture(params=["chrome",'firefox'])
def DiffBrowsers(request):
    return request.param

@pytest.fixture(params=[("chrome","ABC","XYZ"),('firefox','AAAWWWW')])
def DiffBrowsers1(request):
    return request.param


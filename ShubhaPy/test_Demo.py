
#if you want to group the scripts according to keyname you can use as below ex: Smoke test cases
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
import re

#@pytest.mark.skip
def test_browserLogin1():
    path="C:\\chromedriver.exe"
    driver=webdriver.Chrome(path)
    driver.get("https://www.google.com")
    print("INFO: Wait for page to load")
    driver.implicitly_wait(9)
    print("INFO: Google successfully opened in browser")
    s=driver.find_element_by_name("q")
    s.send_keys("Synerzip")
    print("INFO: Hit ENTER")
    s.send_keys(Keys.ENTER)

    print("INFO: Enter Synerzip and serach in google")
    driver.implicitly_wait(5)
    driver.find_element_by_partial_link_text("excellarate").click()
    print("INFO: Clcking on the official Excellarate site")
    driver.implicitly_wait(10)
    print("INFO: %s"%driver.title)
    print("INFO: %s"%driver.current_url)
    #if driver.current_url != "https://www.excellarate.com/"
    assert driver.current_url != "https://www.excellarate.com/"
    driver.close()

@pytest.mark.sanity
def test_browserLogin():
    path="C:\\chromedriver.exe"
    driver=webdriver.Chrome(path)
    driver.get("https://www.google.com")
    print("INFO: Wait for page to load")
    driver.implicitly_wait(9)
    print("INFO: Google successfully opened in browser")
    s=driver.find_element_by_name("q")
    s.send_keys("Synerzip")
    print("INFO: Hit ENTER")
    s.send_keys(Keys.ENTER)

    print("INFO: Enter Synerzip and serach in google")
    driver.implicitly_wait(5)
    driver.find_element_by_partial_link_text("excellarate").click()
    print("INFO: Clcking on the official Excellarate site")
    driver.implicitly_wait(10)
    print("INFO: %s"%driver.title)
    print("INFO: %s"%driver.current_url)
    assert driver.current_url == "https://www.excellarate.com/"

    driver.close()

def test_hello():
    print("Hello")
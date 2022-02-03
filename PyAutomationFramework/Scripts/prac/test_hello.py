from selenium import webdriver
from selenium.webdriver.common.by import By

chromeDriverPath = "C:\\chromedriver.exe"

driver=webdriver.Chrome(chromeDriverPath)
driver.get("https://www.nopcommerce.com/en/login?returnUrl=%2Fen")
driver.implicitly_wait(5)
xpathUsername="//input[@id='Username']"
driver.find_element_by_xpath(xpathUsername).send_keys("githubuser87")
driver.find_element_by_id("Password").send_keys("Freebsd@123")
xpathLoginBtn="//input[@value='Log in']"
driver.find_element_by_xpath(xpathLoginBtn).click()
driver.set_page_load_timeout(10)
URL=driver.current_url
print(URL)

driver.find_element(By.CSS_SELECTOR("")




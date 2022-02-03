from selenium import webdriver
from selenium.webdriver.support.select import Select

chromeDriverPath = "C:\\chromedriver.exe"

driver = webdriver.Chrome(chromeDriverPath)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# Alternatively yu can use find_element_by_id(exampleFormControlSelect1)
d = Select(driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']"))
driver.implicitly_wait(5)
d.select_by_visible_text("Female")
driver.implicitly_wait(5)
d.select_by_index(0)

driver.g
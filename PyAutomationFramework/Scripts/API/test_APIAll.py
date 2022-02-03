from selenium import  webdriver





chromeDriverPath = "C:\\chromedriver.exe"

driver=webdriver.Chrome(chromeDriverPath)
driver.get("https://www.nopcommerce.com/en")
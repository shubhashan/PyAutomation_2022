from selenium import webdriver
from selenium.webdriver import ActionChains

chromeDriverPath = "C:\\chromedriver.exe"

driver = webdriver.Chrome(chromeDriverPath)
driver.get("https://www.nopcommerce.com/en/")
driver.maximize_window()
driver.implicitly_wait(2)
cssIcon = ".ico-user"
Icon = driver.find_element_by_css_selector(cssIcon)
actions = ActionChains(driver)
actions.move_to_element(Icon).click().perform()
driver.implicitly_wait(5)
xpathLogin = "//a[contains(text(),'Log in')]"
driver.find_element_by_xpath(xpathLogin).click()
driver.implicitly_wait(5)
LoginURL=driver.current_url
print(LoginURL)
assert LoginURL == "https://www.nopcommerce.com/en/login?returnUrl=%2Fen%2F"
driver.implicitly_wait(5)
xpathUsername="//input[@id='Username']"
driver.find_element_by_xpath(xpathUsername).send_keys("githubuser87")
driver.find_element_by_id("Password").send_keys("Freebsd@123")
xpathLoginBtn="//input[@value='Log in']"
driver.find_element_by_xpath(xpathLoginBtn).click()
driver.set_page_load_timeout(10)
URL=driver.current_url
print(URL)

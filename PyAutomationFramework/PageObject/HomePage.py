from selenium.webdriver.common.by import By


class HomePage:
    LogoutXpath = "//a[text()='Logout']"

    # Create constructor
    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.LogoutXpath)

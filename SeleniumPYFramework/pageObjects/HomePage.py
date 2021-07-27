from selenium.webdriver.common.by import By


class HomePage:
    #create constructor to pass the driver instance from the test script to the function here
    def __init__(self,driver):
        self.driver = driver


    #open tuple wherein you mention the type of locator and then value of attribute (locator,value)
    shop = (By.CSS_SELECTOR,"a[href*='shop']")

    def shopItems(self):
        #you need to provide * for the variable, then it will deserialise the variable and treats it as a tuple
        #ex:
        return self.driver.find_element(*HomePage.shop)
        #it will treat as driver.find_element_by_css_selector("a[href*='shop']")

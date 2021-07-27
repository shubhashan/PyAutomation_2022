from selenium.webdriver.common.by import By


class CheckOutPage:
    # create constructor to pass the driver instance from the test script to the function here
    def __init__(self, driver):
        self.driver = driver

    # open tuple wherein you mention the type of locator and then value of attribute (locator,value)
    cardtitle=(By.CSS_SELECTOR,".card-title a")

    def getCardTitles(self):
        # you need to provide * for the variable, then it will deserialise the variable and treats it as a tuple
        # ex:
        return self.driver.find_elements(*CheckOutPage.cardtitle)
        # it will treat as driver.find_element_by_css_selector("a[href*='shop']")
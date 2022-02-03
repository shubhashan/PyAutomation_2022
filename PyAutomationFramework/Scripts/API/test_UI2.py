from utilities.Utils import *
from selenium import webdriver

@pytest.mark.UITests
@pytest.mark.usefixtures("setup")
class TestUIOne1(UtilClassOne):
    def test_uiTC2(self, log):
        log.info("testing test_uiTC2, Login to nopcommerce")
        self.driver.implicitly_wait(5)
        log.info("INFO: Google successfully opened in browser")
        url = self.getConfig("test_uiTC2", "url")
        self.driver.get(url)
        self.driver.implicitly_wait(2)
        cssIcon = self.getConfig("test_uiTC2", "cssIcon")
        Icon = self.driver.find_element_by_css_selector(cssIcon)
        # create object for actionchains to perform mouse actions
        actions = ActionChains(self.driver)
        # Hover on the icon and click
        actions.move_to_element(Icon).click().perform()
        self.driver.implicitly_wait(5)
        xpathLogin = self.getConfig("test_uiTC2", "xpathLogin")
        self.driver.find_element_by_xpath(xpathLogin).click()
        self.driver.implicitly_wait(5)
        LoginURL = self.driver.current_url
        log.info(LoginURL)
        VerifyURL = self.getConfig("test_uiTC2", "VerifyURL")
        assert LoginURL == VerifyURL
        self.driver.implicitly_wait(5)
        xpathUsername =self.getConfig("test_uiTC2", "xpathUsername")
        self.driver.find_element_by_xpath(xpathUsername).send_keys("githubuser87")
        self.driver.find_element_by_id("Password").send_keys("Freebsd@123")
        xpathLoginBtn = "//input[@value='Log in']"
        self.driver.find_element_by_xpath(xpathLoginBtn).click()
        self.driver.set_page_load_timeout(10)
        URL = self.driver.current_url
        print(URL)

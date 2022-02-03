from utilities.Utils import *
from selenium import webdriver

@pytest.mark.UITests
@pytest.mark.usefixtures("setup")
class TestUIOne(UtilClassOne):
    def test_uiTC1(self, log):
        log.info("testing test_uiTC1, searching for Synerzip in google and opening the official website")
        self.driver.implicitly_wait(9)
        log.info("INFO: Google successfully opened in browser")
        googleSearchBtn = self.getConfig("test_uiTC1", "googleSearchBtn")
        s = self.driver.find_element_by_name(googleSearchBtn)
        searchWord = self.getConfig("test_uiTC1", "searchWord")
        s.send_keys(searchWord)
        log.info("INFO: Hit ENTER")
        s.send_keys(Keys.ENTER)
        log.info("INFO: Enter %s and search in google" % searchWord)
        self.driver.implicitly_wait(5)
        textLinktoclick = self.getConfig("test_uiTC1", "textLinktoclick")
        self.driver.find_element_by_partial_link_text(textLinktoclick).click()
        Wurl=self.driver.current_url
        PageURL = self.getConfig("test_uiTC1", "PageURL")
        assert Wurl == PageURL , log.error("Excellarate page did not load, TEST CASE FAILED")


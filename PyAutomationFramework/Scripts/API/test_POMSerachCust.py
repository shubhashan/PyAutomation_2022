import time

from utilities.Utils import *


@pytest.mark.usefixtures("setup")
class TestPOMOne(UtilClassOne):
    def test_POM_searchName(self, log):
        loginURL = self.getConfig("test_POM_login", "loginURL")
        email = self.getConfig("test_POM_login", "email")
        password = self.getConfig("test_POM_login", "password")
        log.info("Launching the browser for %s" % loginURL)
        self.driver.get(loginURL)
        self.driver.implicitly_wait(2)
        log.info("Enter Email")
        # create object for LoginPage class
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(email)
        log.info("Enter password")
        self.lp.enterPassword(password)
        self.lp.driver.implicitly_wait(5)
        # self.lp.driver.clickRememberMe()
        log.info("Click on Login")
        self.lp.clickLogin()
        self.lp.driver.implicitly_wait(6)
        # create object for customers class
        self.cust = Customers(self.driver)
        self.cust.clickOnCustomers()
        self.cust.clickOnInnerCustomersMenu()
        time.sleep(3)
        # create class for searchcustomer page
        self.SC = searchCustomers(self.driver)
        self.SC.searchbyFname("Victoria")
        self.SC.clickOnSearch()
        time.sleep(5)
        flags = self.SC.searchTablebyname("Victoria Terces")
        log.info("Name search")
        log.info(flags)
        time.sleep(2)
        self.HP = HomePage(self.driver)
        self.HP.clickLogout()



import time

from utilities.Utils import *


@pytest.mark.usefixtures("setup")
class TestPOM2One(UtilClassOne):
    def test_POM_login2(self, log):
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
        time.sleep(3)
        email1 = "steve_gates@nopCommerce.com"
        self.SC.searchbyemail(email1)
        time.sleep(3)
        self.SC.clickOnSearch()
        time.sleep(2)
        flags = self.SC.searchTablebyEmail(email1)
        log.info("Email search")
        self.SC.clickEditBtn()
        self.EC = editCustomerInfo(self.driver)
        time.sleep(5)
        '''
        self.EC.clickSendEmail()
        time.sleep(2)
        self.EC.enterSubject("Hello subject One test for Edit")
        self.EC.enterEmailbody("Sending email as a part of Edit flow ")
        time.sleep(2)
        self.EC.clickOnInnerEmail()
        text = self.EC.checkAlertBoxText()
        log.info(text)
        time.sleep(5)
        '''
        self.EC.editCustomerPwd()
        self.EC.clickChangePwd()
        text = self.EC.checkAlertBoxText()
        log.info(text)
        time.sleep(2)
        self.EC.clickEditSaveButton()
        textnew=self.EC.checkAlertBoxText()
        log.info(textnew)

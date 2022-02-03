import time

from utilities.Utils import *

@pytest.mark.usefixtures("setup")
class TestPOMOne(UtilClassOne):
    def test_POM_login(self,log):
        loginURL = self.getConfig("test_POM_login", "loginURL")
        email = self.getConfig("test_POM_login", "email")
        password = self.getConfig("test_POM_login", "password")
        log.info("Launching the browser for %s" % loginURL)
        self.driver.get(loginURL)
        self.driver.implicitly_wait(2)
        log.info("Enter Email")
        #create object for LoginPage class
        self.lp=LoginPage(self.driver)
        self.lp.enterEmail(email)
        log.info("Enter password")
        self.lp.enterPassword(password)
        self.lp.driver.implicitly_wait(5)
        #self.lp.driver.clickRememberMe()
        log.info("Click on Login")
        self.lp.clickLogin()
        self.lp.driver.implicitly_wait(6)
        #create object for customers class
        self.cust = Customers(self.driver)
        self.cust.clickOnCustomers()
        self.cust.clickOnInnerCustomersMenu()
        time.sleep(3)
        self.cust.clickAddNew()
        time.sleep(3)
        self.cust.enterCustEmail()
        time.sleep(2)
        self.cust.enterCustPassword("pass123")
        self.cust.enterFirstName("Johnathan")
        self.cust.enterLastName("Smith")
        self.cust.checkGender()
        self.cust.enterDOB("7/7/2000")
        self.cust.enterCompany("Apple")
        time.sleep(3)
        self.cust.checkTaxExempt()
        self.cust.selectNewsletter()
        self.cust.selectCustroles('Vendors')
        self.cust.selectVendor('Vendor 1')
        self.cust.addAdminComment("Adding new customer")
        time.sleep(3)
        self.cust.clickSaveButton()
        time.sleep(8)
        text=self.cust.checkForAlertText()
        log.info(text)
        time.sleep(2)
        #self.cust.gobackToCustomerList()
        #time.sleep(3)

        #create class for searchcustomer page
        self.SC=searchCustomers(self.driver)
        self.SC.searchbyFname("Johnathan")
        self.SC.clickOnSearch()
        time.sleep(2)
        flags=self.SC.searchTablebyname("Johnathan Smith")
        log.info(flags)








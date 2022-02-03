import random
import string
import time
from selenium.webdriver.support.ui import Select


class Customers:
    CustomersMenuXpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    onlineCustomerXpath="//p[normalize-space()='Online customers']"
    customerInnerItemXpath = "//a[@href='/Admin/Customer/List']//p[text()=' Customers']"
    addNewBtnXpath = "//a[contains(@href,'Create')]"
    textEmailID = "Email"
    textPasswordID = "Password"
    FirstNameID = "FirstName"
    LastNameXpath = "//input[@id='LastName']"
    GenderMaleID = "Gender_Male"
    GenderFemaleID = "Gender_Female"
    DOBxpath = "//input[@id='DateOfBirth']"
    CompanyId = "Company"
    TaxExemptXpath = "//input[@id='IsTaxExempt']"
    VendorDropDownXpath = "//select[@id='VendorId']"
    ActiveId = "Active"
    NewsletterXpath = "//div[@class='input-group-append']//div[@role='listbox']"
    CustomerRolesXpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    CustRegisteredXpath = "//li[text()='Registered']"
    CustAdministratorsXpath = "//li[text()='Administrators']"
    CustForumModeratorsXpath = "//li[text()='Forum Moderators']"
    CustGuestsXpath = "//li[text()='Guests']"
    CustVendorsXpath = "//li[text() = 'Vendors']"
    AdminCommentXpath = "//textarea[@id='AdminComment']"
    SaveXpath = "//button[@name='save']"
    listboxDeleteButtonXpath = "//span[@title='delete']"
    yourStoreXpath = "//li[contains(.,'Your store name')]"
    testStorexpath = "//li[contains(.,'Test store 2')]"
    textalertXpath = "//div[@class ='alert alert-success alert-dismissable']"
    closebuttonXpath = "//button[@ data-dismiss='alert']"
    backToCustLinkXpath="//a[text()='back to customer list']"

    # Create constructor
    def __init__(self, driver):
        self.driver = driver

    # Since email Id must be unique everytime, using a random generator function
    def randomG(self, size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def clickOnCustomers(self):
        self.driver.find_element_by_xpath(self.CustomersMenuXpath).click()

    def clickOnInnerCustomersMenu(self):
        self.driver.find_element_by_xpath(self.customerInnerItemXpath).click()

    def clickAddNew(self):
        self.driver.find_element_by_xpath(self.addNewBtnXpath).click()

    def enterCustEmail(self):
        E = self.randomG()
        email = E + '@gmail.com'
        #print(email)
        self.driver.find_element_by_id(self.textEmailID).clear()
        self.driver.find_element_by_id(self.textEmailID).send_keys(email)

    def enterCustPassword(self, Custpassword):
        self.driver.find_element_by_id(self.textPasswordID).clear()
        self.driver.find_element_by_id(self.textPasswordID).send_keys(Custpassword)

    def enterFirstName(self, firstname):
        self.driver.find_element_by_id(self.FirstNameID).clear()
        self.driver.find_element_by_id(self.FirstNameID).send_keys(firstname)

    def enterLastName(self, lastname):
        self.driver.find_element_by_xpath(self.LastNameXpath).clear()
        self.driver.find_element_by_xpath(self.LastNameXpath).send_keys(lastname)

    def checkGender(self, gender='Male'):
        if gender == 'Male':
            self.driver.find_element_by_id(self.GenderMaleID).click()
        else:
            self.driver.find_element_by_id(self.GenderFemaleID).click()

    def enterDOB(self, DOB):
        self.driver.find_element_by_xpath(self.DOBxpath).clear()
        self.driver.find_element_by_xpath(self.DOBxpath).send_keys(DOB)

    def enterCompany(self, company):
        self.driver.find_element_by_id(self.CompanyId).clear()
        self.driver.find_element_by_id(self.CompanyId).send_keys(company)

    def checkTaxExempt(self, status='check'):
        checkBoxTax = self.driver.find_element_by_xpath(self.TaxExemptXpath)
        checkstatus = checkBoxTax.is_selected()
        if status == 'check':
            if checkstatus != 'True':
                checkBoxTax.click()
        if status == 'uncheck':
            if checkstatus == 'True':
                checkBoxTax.click()

    def selectVendor(self, vendor):
        dropDownVendor = Select(self.driver.find_element_by_xpath(self.VendorDropDownXpath))
        dropDownVendor.select_by_visible_text(vendor)

    def selectCustroles(self, role='Guests'):
        self.driver.find_element_by_xpath(self.CustomerRolesXpath)
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.CustRegisteredXpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.CustVendorsXpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.CustAdministratorsXpath)
        elif role == 'Forum':
            self.listitem = self.driver.find_element_by_xpath(self.CustForumModeratorsXpath)
        elif role == 'Guests':
            self.driver.find_element_by_xpath(self.listboxDeleteButtonXpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.CustGuestsXpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectNewsletter(self, store='TestStore'):
        self.driver.find_element_by_xpath(self.NewsletterXpath).click()
        if store == 'TestStore':
            self.box = self.driver.find_element_by_xpath(self.testStorexpath)
        elif store == 'YourStore':
            self.box = self.driver.find_element_by_xpath(self.yourStoreXpath)
        self.box.click()
        # self.driver.execute_script("arguments[0].click();", self.box)

    def selectActive(self):
        s = self.driver.find_element_by_id(self.ActiveId).is_selected()
        if s != 'True':
            self.driver.find_element_by_id(self.ActiveId).click()

    def addAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.AdminCommentXpath).send_keys(comment)

    def clickSaveButton(self):
        self.driver.find_element_by_xpath(self.SaveXpath).click()

    def checkForAlertText(self):
        textBox=self.driver.find_element_by_xpath(self.textalertXpath)
        return textBox.text

    def gobackToCustomerList(self):
        self.driver.find_element_by_xpath(self.backToCustLinkXpath).click()



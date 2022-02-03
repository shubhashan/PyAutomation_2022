import random
import string

from PageObject.Cutomers import Customers


class editCustomerInfo:
    saveContinueXpath = "//button[@name='save-continue']"
    saveBtnXpath = "//button[@name='save']"
    sendEmailXpath = "//button[@data-toggle='modal']"
    deleteBtnXpath = "//span[@id='customer-delete']"
    textEmailID = "Email"
    textPasswordID = "Password"
    changePWDXpath = "//button[@name='changepassword']"
    FirstNameID = "FirstName"
    LastNameXpath = "//input[@id='LastName']"
    CompanyId = "Company"
    alertTextXpath = "//div[contains(@class,'alert-success')]"
    subjectXpath = "//input[@id='SendEmail_Subject']"
    emailBodyXpath = "//textarea[@id='SendEmail_Body']"
    sendImmedXpath = "//input[@id='SendEmail_SendImmediately']"
    sendEmailInnerXpath = "//button[contains(text(),'Send email')]"

    # Create constructor
    def __init__(self, driver):
        self.driver = driver

    def randomPWD(self, size=12, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def editCustomerPwd(self):
        # accessing the random generator function to create unique password everytime for each test case
        password = self.randomPWD()
        #print(password)
        self.driver.find_element_by_id(self.textPasswordID).clear()
        self.driver.find_element_by_id(self.textPasswordID).send_keys(password)

    def clickChangePwd(self):
        self.driver.find_element_by_xpath(self.changePWDXpath).click()

    def checkAlertBoxText(self):
        textbox = self.driver.find_element_by_xpath(self.alertTextXpath)
        return textbox.text

    def editCustomerLname(self, lname):
        self.driver.find_element_by_xpath(self.LastNameXpath).clear()
        self.driver.find_element_by_xpath(self.LastNameXpath).send_keys(lname)

    def clickEditSaveButton(self):
        self.driver.find_element_by_xpath(self.saveBtnXpath).click()

    def clickSendEmail(self):
        self.driver.find_element_by_xpath(self.sendEmailXpath).click()

    def enterSubject(self, subjectText):
        self.driver.find_element_by_xpath(self.subjectXpath).clear()
        self.driver.find_element_by_xpath(self.subjectXpath).send_keys(subjectText)

    def enterEmailbody(self, text):
        self.driver.find_element_by_xpath(self.emailBodyXpath).clear()
        self.driver.find_element_by_xpath(self.emailBodyXpath).send_keys(text)

    def checksendImmediate(self, status='check'):
        checkBoxTax = self.driver.find_element_by_xpath(self.sendImmedXpath)
        checkstatus = checkBoxTax.is_selected()
        if status == 'check':
            if checkstatus != 'True':
                checkBoxTax.click()
        if status == 'uncheck':
            if checkstatus == 'True':
                checkBoxTax.click()

    def clickOnInnerEmail(self):
        self.driver.find_element_by_xpath(self.sendEmailInnerXpath).click()

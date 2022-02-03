from selenium import webdriver

class LoginPage:
    textbox_emailID = "Email"
    textbox_passwordID = "Password"
    LoginXpath = "//button[@type='submit']"
    RememberMeXpath="//input[@id='RememberMe']"

    #Create constructor
    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self, email):
        # since class variables you need to use "self.textbox_emailID" etc...
        self.driver.find_element_by_id(self.textbox_emailID).clear()
        self.driver.find_element_by_id(self.textbox_emailID).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.textbox_passwordID).clear()
        self.driver.find_element_by_id(self.textbox_passwordID).send_keys(password)

    def clickRememberMe(self):
        RememberMe = self.driver.find_element_by_xpath(self.RememberMeXpath)
        status = self.checkstatusRememberMeBox()
        if not status:
            RememberMe.click()

    def checkstatusRememberMeBox(self):
        RememberMe = self.driver.find_element_by_xpath(self.RememberMeXpath)
        status = RememberMe.is_selected()
        return status


    def clickLogin(self):
        self.driver.find_element_by_xpath(self.LoginXpath).click()


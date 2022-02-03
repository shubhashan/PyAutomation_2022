class searchCustomers:
    searchEmailid = "SearchEmail"
    searchFirstnameId = "SearchFirstName"
    searchLastnameId = "SearchLastName"
    DOBMonthXpath = "//select[@id='SearchMonthOfBirth']"
    DOBdayXpath = "//select[@id='SearchDayOfBirth']"
    searchBtnXpath = "//button[@id='search-customers']"
    searchCompanyXpath = "//input[@id='SearchCompany']"
    searchIPxpath = "//input[@id='SearchIpAddress']"
    rolelBoxXpath = "//div[@role='listbox']"
    rolelBoxGuestsXpath = "//li[text()='Guests']"
    rolelBoxVendorsXpath = "//li[text() = 'Vendors']"
    rolelBoxAdministratorsXpath = "//li[text() = 'Administrators']"
    rolelBoxForumModeratorsXpath = "//li[text()='Forum Moderators']"
    rolelBoxRegisteredXpath = "//li[text()='Registered']"
    searchCustTableXpath = "//table[@id='customers-grid']"
    searchTablerowsXpath = "//table[@id='customers-grid']//tbody/tr"
    serachTablecolumnsXpath = "//table[@id='customers-grid']//tbody/tr/td"
    editBtnCss = ".fa-pencil-alt"
    refreshBtnXpath = "//i[contains(@class,'fa-sync-alt')]"

    # Create constructor
    def __init__(self, driver):
        self.driver = driver

    def searchbyemail(self, email):
        self.driver.find_element_by_id(self.searchEmailid).clear()
        self.driver.find_element_by_id(self.searchEmailid).send_keys(email)

    def searchbyFname(self, Fname):
        self.driver.find_element_by_id(self.searchFirstnameId).clear()
        self.driver.find_element_by_id(self.searchFirstnameId).send_keys(Fname)

    def searchbyLname(self, Lname):
        self.driver.find_element_by_id(self.searchLastnameId).clear()
        self.driver.find_element_by_id(self.searchLastnameId).send_keys(Lname)

    def clickOnSearch(self):
        self.driver.find_element_by_xpath(self.searchBtnXpath).click()

    def noOfRows(self):
        Rows = self.driver.find_elements_by_xpath(self.searchTablerowsXpath)
        return len(Rows)

    def noOfColumns(self):
        cols = self.driver.find_elements_by_xpath(self.serachTablecolumnsXpath)
        return len(cols)



    def searchTablebyEmail(self, email):
        flag = False
        table = self.driver.find_element_by_xpath(self.searchCustTableXpath)
        for r in range(1, self.noOfRows() + 1):
            celldata = table.find_element_by_xpath(
                "//table[@id='customers-grid']//tbody//tr[" + str(r) + "]//td[2]").text
            if email == celldata:
                flag = True
                break
        return flag

    def searchTablebyname(self, name):
        flag = False
        table = self.driver.find_element_by_xpath(self.searchCustTableXpath)
        for r in range(1, self.noOfRows() + 1):
            celldata = table.find_element_by_xpath(
                "//table[@id='customers-grid']//tbody//tr[" + str(r) + "]//td[3]").text
            if name == celldata:
                flag = True
                break
        return flag


    def clickEditBtn(self):
        self.driver.find_element_by_css_selector(self.editBtnCss).click()





import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLink(self,text):
        ele = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.LINK_TEXT),text)


@pytest.fixture(params=[("ABC","XYZ")])
def name1(request):
    return request.param

@pytest.mark.usefixtures("name1")
class BaseClassOne:

    pass
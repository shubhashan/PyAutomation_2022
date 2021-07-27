
import requests
import pytest

#practice test scripts
#HTTP GET method tests:

#1. DELETE response pass and looking for a particular name pass
from utilities.Utils import UtilClassOne


@pytest.mark.httpGET
@pytest.mark.httpWithAuth
@pytest.mark.APITests
class TestgetAuth(UtilClassOne):

    def test_getAuthTC1(self):
        log = self.loggerC("test_getAuthTC1")
        log.info("===== Start 'GET' method testing with auth enabled but fails")
        url = self.getConfig("test_getAuthTC1", "url")
        user = self.getConfig("test_getAuthTC1", "user")
        pwd = self.getConfig("test_getAuthTC1", "pwd")
        log.info("testing for url %s" % url)
        # providing the auth while doing GET
        res = requests.get(url, auth=(user, pwd))
        log.info("The response is : %s " %res)
        jres= res.json()
        log.info("The JSON response is :  %s" %jres)
        assert (res.status_code == 401), log.error("Accessing resource without authentication successful  ====== TEST CASE FAILED=====")
        if res.status_code == 401:
            log.info("Accessing resource without authentication unsuccessful ")
            log.info("=======TEST CASE PASSED=========")

    def test_getAuthTC2(self):
        log = self.loggerC("test_getAuthTC2")
        log.info("===== Start 'GET' method testing with basic auth")
        url = self.getConfig("test_getAuthTC2", "url")
        user = self.getConfig("test_getAuthTC2", "user")
        pwd = self.getConfig("test_getAuthTC2", "pwd")
        log.info("testing for url %s" % url)
        #providing the auth while doing GET
        res = requests.get(url, auth=(user,pwd))
        log.info("The response is : %s " %res)
        jres = res.json()
        log.info("==================================")
        log.info("The JSON response is :  %s" %jres)
        log.info("==================================")
        assert (res.status_code == 200), log.error("User authentication failed  ====== TEST CASE FAILED=====")
        if res.status_code == 200:
            log.info("User authentication passed")
            log.info("=======TEST CASE PASSED=========")





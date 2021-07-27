from utilities.Utils import *
import requests
import pytest

#practice test scripts
#HTTP GET method tests:

#1. DELETE response pass and looking for a particular name pass



@pytest.mark.httpGET
@pytest.mark.httpRedirect
@pytest.mark.APITests
class TestgetRedirect(UtilClassOne):
    def test_getRedirectTC1(self):
        log = self.loggerC("test_getRedirectTC1")
        log.info("===== Start 'GET' method testing with redirection")
        url = self.getConfig("test_getRedirectTC1", "url")
        log.info("testing redirection for url %s" % url)
        ###=======Redirection 3XX codes...
        print("======REDIRECTION=====")
        res = requests.get(url)
        log.info("===The response history ===")
        log.info(res.history)
        log.info("The  response is :  %s" % res)
        log.info("The response content is ========")
        log.info(res.text)

        #jres= res.json()

        assert (res.status_code == 200), log.error("Error , TEST CASE FAILED")
        if res.status_code == 200:
            log.info("Redirection works as expected")
            log.info("=======TEST CASE PASSED=========")

    def test_getRedirectTC2(self):
        log = self.loggerC("test_getRedirectTC2")
        log.info("===== Start 'GET' method testing with redirection set to false")
        #using the same URL for both the test cases
        url = self.getConfig("test_getRedirectTC1", "url")
        log.info("testing redirection for url %s" % url)
        ###=======Redirection 3XX codes...
        print("======REDIRECTION=====")
        res=requests.get(url, allow_redirects=False)
        log.info("===The response history ===")
        log.info(res.history)
        log.info("The  response is :  %s" % res)
        log.info("The response content is ========")
        log.info(res.text)
        #jres= res.json()
        assert (res.status_code != 200), log.error("Error , TEST CASE FAILED")
        if res.status_code != 200:
            log.info("Redirection set to false works as expected")
            log.info("=======TEST CASE PASSED=========")


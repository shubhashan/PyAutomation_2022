

import requests
import pytest

#practice test scripts
#HTTP GET method tests:

#1. DELETE response pass and looking for a particular name pass
from utilities.Utils import UtilClassOne


@pytest.mark.httpDELETE
@pytest.mark.APITests
class TestDELETEReq(UtilClassOne):
    def test_deleteReqP1(self):
        log = self.loggerC("test_deleteReqP1")
        log.info("===== Start 'DELETE' method testing")
        url=self.getConfig("test_deleteReqP1", "url")
        log.info("testing for url %s" % url)
        res = requests.delete(url)
        log.info(res)
        assert (res.status_code == 204), "User deletion failed"
        if res.status_code == 204:
            log.info("User deletion passed")
            log.info("=======TEST CASE PASSED=========")
        else:
            log.error("User deletion failed")
            log.error("=======TEST CASE FAILED=========")

    def test_deleteReqP2(self):
        log = self.loggerC("test_deleteReqP2")
        log.info("===== Start DELETE API testing")
        url = self.getConfig("test_deleteReqP2", "url")
        log.info("testing for url %s" % url)
        res=requests.delete(url)
        log.info(res)
        assert (res.status_code == 204), "User deletion failed"
        if res.status_code == 204:
            log.info("User deletion passed")
            log.info("=======TEST CASE PASSED=========")
        else:
            log.error("User deletion failed")
            log.error("=======TEST CASE FAILED=========")






from utilities.Utils import *

# practice test scripts
# HTTP GET method tests:

# 1. DELETE response pass and looking for a particular name pass



@pytest.mark.httpDELETE
@pytest.mark.APITests
class TestDELETEReq(UtilClassOne):
    def test_deleteReqP1(self,log):
        #log = self.loggerC("test_deleteReqP1")
        log.info("===== Start 'DELETE' method testing")
        url =self.getConfig("test_deleteReqP1", "url")
        log.info("testing for url %s" % url)
        res = requests.delete(url)
        log.info(res)
        assert (res.status_code == 204), log.error("User deletion failed, TEST CASE FAILED")
        if res.status_code == 204:
            log.info("User deletion passed")
            log.info("=======TEST CASE PASSED=========")

    def test_deleteReqP2(self,log):
        #log = self.loggerC("test_deleteReqP2")
        log.info("===== Start DELETE API testing")
        url = self.getConfig("test_deleteReqP2", "url")
        log.info("testing for url %s" % url)
        res =requests.delete(url)
        log.info(res)
        assert (res.status_code == 204), log.error("User deletion failed, TEST CASE FAILED")
        if res.status_code == 204:
            log.info("User deletion passed")
            log.info("=======TEST CASE PASSED=========")

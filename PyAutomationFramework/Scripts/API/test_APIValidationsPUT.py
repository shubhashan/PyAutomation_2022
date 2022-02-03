import json

import requests
import pytest
from utilities.Utils import UtilClassOne

# practice test scripts
# HTTP PUT method tests:
# 1. PUT to create user : PASS case

# test PATCH request



@pytest.mark.APITests
class TestPUTReq(UtilClassOne):
    @pytest.mark.httpPUT
    def test_putReqP1(self,log):
        #log = self.loggerC("test_putReqP1")
        log.info("===== Start  'PUT' method testing")
        url = self.getConfig("test_putReqP1", "url")
        log.info("testing for url %s" % url)
        data1 = self.getConfig("test_putReqP1", "data1")
        log.info("testing PUT with data  :  %s" % data1)

        res = requests.put(url, data=data1)
        log.info(res)
        # Assert for the correct status code
        assert res.status_code == 200, log.error("Status is not 200, error creating user , ==== TEST CASE FAILED======")
        # we need the response in json format
        jRes = res.json()
        log.info(jRes)
        if res.status_code == 200:
            log.info("Update doing PUT successful")
            log.info("==== TEST CASE PASSED======")

    @pytest.mark.httpPATCH
    def test_patchReqP1(self,log):
        #log = self.loggerC("test_patchReqP1")
        log.info("===== Start  'PATCH' method testing")
        url = self.getConfig("test_patchReqP1", "url")
        log.info("testing for url %s" % url)
        data1 = self.getConfig("test_patchReqP1", "data1")
        log.info("testing PATCH update for data %s" % data1)
        res = requests.patch(url, data=data1)
        log.info(res)
        # Assert for the correct status code
        assert res.status_code == 200, log.error("Status is not 200, error creating user , ==== TEST CASE FAILED===")
        # we need the response in json format
        jRes = res.json()
        log.info("========== JSON response======")
        log.info(jRes)

        # ==try with a new data

        data2 = self.getConfig("test_patchReqP1", "data2")
        log.info("testing for data %s" % data2)

        res = requests.patch(url, data=data2)
        log.info(res)
        # Assert for the correct status code
        assert res.status_code == 200, "Status is not 200, error creating user"
        # we need the response in json format
        jRes = res.json()
        log.info(jRes)
        if res.status_code == 200:
            log.info("Update doing PATCH successful")
            log.info("==== TEST CASE PASSED======")

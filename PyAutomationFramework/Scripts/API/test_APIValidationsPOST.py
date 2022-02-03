import json
import requests
import pytest

# practice test scripts
# HTTP POST method tests:

# 1. POST to create user : PASS case
from utilities.Utils import UtilClassOne


@pytest.mark.httpPOST
#@pytest.mark.TestSuite1
@pytest.mark.APITests
class TestPOSTReq(UtilClassOne):
    def test_postReqP1(self,log):
        #log = self.loggerC("test_postReqP1")
        log.info("===== Start 'POST' method testing")
        url = self.getConfig("test_postReqP1", "url")
        log.info("testing for url %s" % url)
        data1 = self.getConfig("test_postReqP1", "data1")
        log.info("posting data for url : %s" % data1)

        res = requests.post(url, data=data1)
        log.info(res.status_code)
        # Assert for the correct status code
        assert res.status_code == 201, "Status is not 201, error creating user"
        # we need the response in json format
        jRes = res.json()
        log.info("The JSON response====")
        log.info(jRes)

        log.info("===Test again with different data===")
        data2 = self.getConfig("test_postReqP1", "data2")
        log.info("posting data for url : %s" % data2)
        res = requests.post(url, data=data2)
        log.info(res.status_code)
        # we need the response in json format
        jRes = res.json()
        log.info("Data response====")
        log.info(jRes)

    # 2 . POST pass case by sending payload from a file

    def test_postReqP2(self,log):
        #log = self.loggerC("test_postReqP2")
        log.info("===== Start 'POST' method testing")
        url = self.getConfig("test_postReqP2", "url")
        log.info("testing for url %s" % url)
        filePath = self.getConfig("test_postReqP2", "filePath")
        log.info("testing for url %s" % filePath)

        # filePath="C:\\Users\\shubhav\\PycharmProjects\\APITesting\\PayloadFile.json"
        dataFile = open(filePath, "r").read()
        log.info("-------------------------------")
        log.info(dataFile)
        res = requests.post(url, data=json.loads(dataFile))
        log.info(res.status_code)
        # we need the response in json format
        jRes = res.json()
        log.info(jRes)
        # Assert for the correct status code
        assert res.status_code == 201, "Status is not 201, error creating user"
        # we need the response in json format

    # fail case
    def test_postReqP3(self,log):
        #log = self.loggerC("test_postReqP3")
        log.info("===== Start  'GET' method testing")
        url = self.getConfig("test_postReqP3", "url")
        log.info("testing for url %s" % url)
        data1 = self.getConfig("test_postReqP3", "data1")
        log.info("testing data for url %s" % data1)
        res = requests.post(url, data=data1)
        log.info(res)
        jRes = res.json()
        log.info(jRes)
        assert res.status_code == 200, log.error("Status is not 200 token not created,  user not registered")
        log.info(jRes['token'])
        assert token != None, log.error("token not created,  user not registered")

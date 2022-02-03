from utilities.Utils import *
# practice test scripts
# HTTP GET method tests:

# 1. GET response pass and looking for a particular name pass



@pytest.mark.httpGET
@pytest.mark.APITests
class TestGETReq(UtilClassOne):
    def test_getReqP1(self,log):
        #log = self.loggerC("test_getReqP1")
        log.info("===== Start  'GET' method testing")
        url = self.getConfig("test_getReqP1", "url")
        log.info("testing for url %s" % url)
        res = requests.get(url)
        log.info(res)
        assert (res.status_code == 200), "Status code is not 200"
        jsonRes = res.json()
        log.info("======JSON response========")
        log.info(jsonRes)
        log.info("===============")

        # use jsonpath
        log.info("== Verifying the total no of pages is 12")
        assert jsonRes['total'] == 12
        if jsonRes['total'] == 12:
            log.info("Verification passed")
        else:
            log.error("Verification failed")
        log.info(jsonRes['data'][0]["email"])

        assert (jsonRes['data'][0]["email"]).endswith("reqres.in"), "Email is not correct"

        log.info(jsonRes['data'][1]['first_name'])

        assert jsonRes['data'][1]['first_name'] != "ABC", "Name mismatch"

    # 2. GET response pass and looking for a particular name fails

    def test_getReqP2(self,log):
        #log = self.loggerC("test_getReqP2")
        log.info("===== Start  'GET' method testing")
        url = self.getConfig("test_getReqP1", "url")
        log.info("testing for url %s" % url)
        res = requests.get(url)
        log.info(res.status_code)
        jsonRes = res.json()
        log.info("======JSON response========")
        log.info(jsonRes)
        log.info("===============")
        log.info(jsonRes['data'][1]['first_name'])
        assert jsonRes['data'][1]['first_name'] != "ABC", log.error("Looking for name ABC, TEST CASE FAILED")
        log.info("NAme is not same, negative case")
        log.info("==== TEST CASE PASSED")

    # 3. GET response using paramaeters pass case

    def test_getReqP3(self,log):
        #log = self.loggerC("test_getReqP3")
        log.info("===== Start  'GET' method testing")
        url = self.getConfig("test_getReqP3", "url")
        log.info("testing for url %s" % url)
        p = self.getConfig("test_getReqP3", "p")
        print(p)
        # p={'page':2}
        # url="https://reqres.in/api/users"
        # Here you can send the keyvalue as params , here dict p acts like params
        res = requests.get(url, params=p)
        log.info(res.status_code)
        jsonRes = res.json()
        log.info("======JSON response========")
        log.info(jsonRes)
        log.info("===============")
        log.info(jsonRes['data'][1]['first_name'])
        assert jsonRes['data'][1]['first_name'] != "ABC", "Looking for name not  ABC"

    # 4. GET response using paramaeters , response fails

    def test_getReqP4(self,log):
        #log = self.loggerC("test_getReqP4")
        log.info("===== Start  'GET' method testing")
        url = self.getConfig("test_getReqP4", "url")
        log.info("testing for url %s" % url)
        # Url="https://reqres.in/api/users/23"
        # Here you can send the keyvalue as params , here dict p acts like params
        res = requests.get(url)
        log.info(res.status_code)
        log.info(res.text)
        assert res.status_code != 200, log.error("Status is  200, resource  found, TEST CASE FAILED")
        log.info("Accessing invalid response ... Status is %s " %res.status_code)
        log.info("=== TEST CASE PASSED")

    # 4. GET time-out scenario

    def test_getReqP5(self,log):
        #log = self.loggerC("test_getReqP5")
        url = self.getConfig("test_getReqP5", "url")
        log.info("testing for url %s" % url)
        # Url="https://httpbin.org/delay/3"
        # Here you can send the keyvalue as params , here dict p acts like params
        res = requests.get(url, timeout=5)
        log.info(res.status_code)
        assert res.status_code == 200, "Status is not 200,Req  timedout"

    def test_getReqP6(self,log):
        #log = self.loggerC("test_getReqP6")
        url = self.getConfig("test_getReqP5", "url")
        log.info("testing for url %s" % url)
        log.info("The GET method for timeout scenario,  the response times out")

        try:
            res = requests.get(url, timeout=2)
        except requests.exceptions.Timeout as e:
            log.info(e)
            log.info("GET method Time-out occured")

        except:
            log.info("Exception occured")



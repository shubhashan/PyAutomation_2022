import json
import requests
import pytest

# 1. Upload files
from utilities.Utils import UtilClassOne


@pytest.mark.httpPOST
@pytest.mark.APITests
class TestPOSTFileUpload(UtilClassOne):
    def test_postFileUploadTC1(self):
        log = self.loggerC("test_postFileUploadTC1")
        log.info("===== Start 'POST' method testing for file upload")
        url = self.getConfig("test_postFileUploadTC1", "url")
        log.info("testing for url %s" % url)
        #file = self.getConfig("test_postFileUploadTC1", "file")
        fileName = self.getConfig("test_postFileUploadTC1", "fileName")
        mode = self.getConfig("test_postFileUploadTC1", "mode")
        file = {"file": open(fileName, mode)}
        res = requests.post(url)
        jRes = res.json()
        log.info("====Files content before upload====")
        file1 = jRes['files']
        log.info(file1)
        log.info("===== JSON response========")
        log.info(jRes)

        log.info("File to upload is  %s" % file)
        res1 = requests.post(url, files=file)
        jRes1 = res1.json()
        log.info(res1.status_code)
        log.info("====Files content after upload====")
        file2 = jRes1['files']
        log.info(file2)
        log.info("===== JSON response========")
        log.info(jRes1)

        assert file1 != file2, log.error("==== TEST CASE FAILED====")

        log.info("File upload was successful")
        log.info("==== TEST CASE PASSED====")

import pytest
import requests



from _pytest.cacheprovider import Cache
from collections import defaultdict

import _pytest.cacheprovider
import pytest


@pytest.mark.fixture(scope="class")
def loggerC(request):
    # logger will automatically capture the file name when yu give __name__
    logName = inspect.stack()[1][3]
    logObj = logging.getLogger(logName)
    filePath = "logs/fileLogAPItests.log"
    LogHandle = logging.FileHandler(filePath)
    logFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # format for log file message
    LogHandle.setFormatter(logFormat)
    # add the file details where the file logging must be done
    logObj.addHandler(LogHandle)
    # print(debugLevel)

    return request.param


# Fixture for HTTP GET Request
@pytest.mark.fixture(scope="class")
def httpGetReq():
    print(request)
    res = requests.get()
    print(res)
    assert (res.status_code == 200), "Status code is not 200"


@pytest.mark.fixture(scope="class")
def httpDeleteReq():
    print(request)
    res = requests.get()
    print(res)
    assert (res.status_code == 200), "Status code is not 200"


@pytest.mark.fixture(scope="class")
def httpPostReq():
    print(request)
    res = requests.get()
    print(res)
    assert (res.status_code == 200), "Status code is not 200"

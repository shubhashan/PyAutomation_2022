import inspect
import logging
import time
import pytest
from selenium import webdriver

LogFilePath = "..//..//Logs"
ConfigIniFilePath = "..//..//utilities//config.ini"
chromeDriverPath = "C:\\chromedriver.exe"
FirefoxDriverPath = ".."


def pytest_addoption(parser):
    #parser.addoption("--sessionID", action="store", default="1234")
    parser.addoption("--logLevel", action="store", default="DEBUG")
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(autouse=True)
def your_fixture(request, log):
    # print(request.module)
    # print(request.cls)
    testcaseName = request.function.__name__
    log.info("***************   TestCase : '%s' STARTS    *************" % testcaseName)
    log.info("---------------------------------------------------------------------")
    yield
    # log.info("=======================")
    log.info("                           ")
    log.info("***********************       TEST END         ***********************")
    log.info("----------------------------------------------------------------------")


@pytest.fixture(scope="session", autouse=True)
def log(request):
    #logLevel = request.config.getoption("logLevel")
    #sessionID = request.config.getoption("sessionID")
    # name = request.function.__name__
    # logger will automatically capture the file name when yu give __name__
    # session_name = request.config.getoption("session")
    # logName = nameFunc

    logName = inspect.stack()[1][3]
    logObj = logging.getLogger(logName)
    file = time.asctime()
    file = str(file)
    file = file.replace(" ", "_")
    file = file.replace(".", "_")
    timeStamp = file.replace(":", "_")
    logPath = LogFilePath + "\\TESTLOG_" + timeStamp + ".log"
    print(logPath)

    LogHandle = logging.FileHandler(logPath)
    # logFormat = logging.Formatter(
    # " %(asctime)s : %(levelname)s : %(name)s : %(message)s")
    logFormat = logging.Formatter(
        " %(asctime)s : %(levelname)s : %(message)s")  # format for log file message
    LogHandle.setFormatter(logFormat)
    # add the file details where the file logging must be done
    logObj.addHandler(LogHandle)
    # print(debugLevel)

    logObj.setLevel(logging.DEBUG)

    return logObj


@pytest.fixture(scope="class")
def test_openBrowserrequest(log):
    # print("INFO: Inside fixture")
    log.info("Opening the browser")

    driver = webdriver.Chrome(chromeDriverPath)
    driver.get("https://www.google.com")
    driver.implicitly_wait(5)
    # return the driver object so that the specific test script can make use of it can do further actions
    return (driver)
    # yield
    # print("----Closing all browser instances-----")
    # driver.close()

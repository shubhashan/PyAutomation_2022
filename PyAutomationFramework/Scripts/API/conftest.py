import inspect
import logging
import time
import pytest
from selenium import webdriver

LogFilePath = "..//..//Logs"
ConfigIniFilePath = "..//..//utilities//config.ini"
chromeDriverPath = "..//..//chromedriver.exe"
FirefoxDriverPath = "..//..//geckodriver.exe"


# Fixture to get any command line options like which browser to test  etc
def pytest_addoption(parser):
    # parser.addoption("--sessionID", action="store", default="1234")
    parser.addoption("--logLevel", action="store", default="DEBUG")
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(autouse=True)
def your_fixture(request, log):
    # print(request.module)
    # print(request.cls)
    # fucntion that returns the testcase that calls the fixture
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
    # logLevel = request.config.getoption("logLevel")
    # sessionID = request.config.getoption("sessionID")
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
def setup(request, log):
    browser = request.config.getoption("browser")
    log.info("Getting the browser name from the CLI")
    if browser == "chrome":
        driver = webdriver.Chrome(chromeDriverPath)
    elif browser == "firefox":
        #while using firefox gecko driver we need to specify as below, else the webdriver instance doesnt launch
        driver = webdriver.Firefox(executable_path=FirefoxDriverPath)
        # you can implement for other mutiple browsers in same way ex IE etc
    log.info("Opening the browser instance for %s" % browser)
    driver.get("https://www.google.com")
    driver.implicitly_wait(5)
    driver.maximize_window()
    # driver tat yu have intialised here will be connected to the class that uses this fixture driver
    request.cls.driver = driver
    yield
    driver.close()


def pytest_configure(config):
    config._metadata['Project NAme'] = 'Pytest Automation'
    config._metadata['Module'] = 'API/Web UI '
    config._metadata['Author'] = 'Shubha Venkateshan'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)






import pytest
from selenium import webdriver

#command line arguements declaration for pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        path = "C:\\chromedriver.exe"
        driver = webdriver.Chrome(path)
    elif browser_name == "firefox":
        path = "C:\\firefox.exe"
        driver = webdriver.Firefox(path)
        #you can implement for mutiple browsers in same way

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    #driver tat yu have intialised here will be connected to the class that uses this fixture driver
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="class")
def setup1(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        path = "C:\\chromedriver.exe"
        driver = webdriver.Chrome(path)
    elif browser_name == "firefox":
        path = "C:\\firefox.exe"
        driver = webdriver.Firefox(path)
        #you can implement for mutiple browsers in same way

    driver.get("https://www.google.com")
    driver.maximize_window()
    #driver tat yu have intialised here will be connected to the class that uses this fixture driver
    request.cls.driver = driver
    yield
    driver.close()



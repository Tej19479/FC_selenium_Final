import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = None


# @pytest.fixture(scope="class")
# def driver(request):
#     # Initialize the WebDriver
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     print("Called driver:", driver)
#
#     # Set implicit wait
#     driver.implicitly_wait(10)
#
#     # Provide the WebDriver instance to test classes
#     request.cls.driver = driver
#
#     # Teardown - close the WebDriver
#     yield driver
#     driver.close()

#
@pytest.fixture(autouse=True)
def setup(request, browser):
    print("rrrrrrrrrrrrrrrr", browser)
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        print("chrome lunch")
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("firefox")
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("lunch edge")
    # #driver.get(url)
    # driver.maximize_window()
    request.cls.driver = driver
    yield


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser option: chrome, edge, or firefox")
    parser.addoption("--url")

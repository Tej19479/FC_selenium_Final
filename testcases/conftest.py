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
from selenium.webdriver.chrome.options import Options
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


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
@pytest.fixture(autouse=True, scope="class")
def setup(request, browser):
    print("rrrrrrrrrrrrrrrr", browser)
    global driver
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Optional: maximize browser window
        options.add_argument("--disable-extensions")  # Optional: disable extensions
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        print("Chrome launched")
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
    driver.quit()


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

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from chromedriver_py import binary_path

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

driver = None


@pytest.fixture(scope="class", autouse=True)
def setup(request, browser,url):
    global driver
    if browser == "chrome":

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(service=ChromeService(executable_path=binary_path), options=options)
        print("Chrome launched")
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Firefox launched")
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("Edge launched")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser option: chrome, edge, or firefox")
    parser.addoption("--url", action="store", default="http://qclend1.faircent.com", help="url to test")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        global driver
        current_url = driver.current_url
        extra.append(pytest_html.extras.url(current_url))

        xfail = hasattr(report, 'wasxfail')

        if (report.skipped and xfail) or (report.failed and not xfail):
            screenshot_path = os.path.join(os.getcwd(), 'screenshots', f'{item.name}.png')
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            driver.save_screenshot(screenshot_path)
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
            extra.append(pytest_html.extras.image(screenshot_path))

            #here save report and broser name and testcasename
        extra.append(pytest_html.extras.text(f"Test case: {item.name}"))
        extra.append(pytest_html.extras.text(f"Browser: {item.config.getoption('--browser')}"))
        report.extra = extra

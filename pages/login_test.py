import time
import  pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    driver.close()
def test_login(driver):
     print("tets case start")
     login_page=LoginPage(driver)
     login_page.open_page("https://www.faircent.in/user/login")

     login_page.enter_username("a4arvindjh@1990@gmail.com")
     login_page.enter_password("Agam@1990")
     login_page.click_login()
     time.sleep(5)
     assert "https://www.faircent.in/user/login" in driver.current_url


import time
import pytest
from pages.login_page import LoginPage


#@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_login(self):
        print("test case start")
        login_page = LoginPage(self.driver)
        login_page.open_page("https://www.faircent.in/user/login")

        login_page.enter_username("mustaques786@gmail.com")
        login_page.enter_password("techlet@123")
        login_page.click_login()
        time.sleep(5)

        assert "https://www.faircent.in/lender/mlp/investview" in self.driver.current_url

import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Faircentdouble import Lender_dashboard
from pages.home_page import Homepage
from selenium.webdriver.common.by import By

from testcases.conftest import browser


@pytest.mark.usefixtures("setup")
class Test_manul:

    def test_manul(self):
        home_page = Homepage(self.driver)
        home_page.open_page("https://admin.faircent.com/")
        home_page.log_button()
        # home_page.enter_username("mustaques786@gmail.com")  more12@yopmail.com
        home_page.enter_username("tej.pratap.admin@faircent.com")
        home_page.enter_password("tej.pratap.admin@faircent.com")
        home_page.click_login()
        home_page.open_page("https://admin.faircent.com/admins/withdraw/wallet/maually")

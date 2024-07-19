import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Faircentdouble import Lender_dashboard
from pages.home_page import Homepage
from selenium.webdriver.common.by import By

from testcases.conftest import browser


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login(self):
        home_page = Homepage(self.driver)
        home_page.open_page("https://www.faircent.in/")
        home_page.log_button()
        # home_page.enter_username("mustaques786@gmail.com")  more12@yopmail.com
        home_page.enter_username("Tej.pratap@faircent.com")
        home_page.enter_password("Tej@1234")
        home_page.click_login()
        home_page.Lend_Screen_click()

        time.sleep(5)

        home_page.Fd_plan_section("24months")
        time.sleep(5)

        home_page.enter_investment_amount(27000)
        time.sleep(5)

        home_page.toggle_rinvest_slider(True)
        time.sleep(5)
        home_page.mlp_Dashboard()
        time.sleep(5)

        #home_page.mlp_lend_screens()
        home_page.mlp_investment_plan_click("36Months")
        time.sleep(5)

        home_page.mlp_enter_investment_amount(25000)
        time.sleep(5)
        home_page.use_escrow_mlp(True)
        home_page.submit_investment()
        # time.sleep(20)
        # locator = (By.XPATH, "//a[text()='LENDING OVERVIEW ']")
        # home_page.mlp_lender_overview_screen()
        #
        # time.sleep(9)
        # home_page.enter_investment_amount(25000)
        # home_page.use_escrow(False)
        # home_page.submit_investment()
        # time.sleep(1)
        # home_page.investment_continue_button()
        # WebDriverWait(self.driver, 10).until(
        #     EC.url_contains("https://qclend2.faircent.com/lender/escrow/payment_escrow")
        # )
        # assert "https://qclend2.faircent.com/lender/escrow/payment_escrow" in self.driver.current_url

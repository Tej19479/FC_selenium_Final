import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pages.home_page import Homepage


@pytest.mark.usefixtures("setup")
class TestManualWithdrawn:

    def test_manual_withdrawn(self):
        home_page = Homepage(self.driver)

        # Log in to the system
        home_page.log_button()
        home_page.enter_username("tej.pratap.admin@faircent.com")
        home_page.enter_password("tej.pratap.admin@faircent.com")
        # home_page.enter_username("Fc_admin")
        # home_page.enter_password("techlet@123")

        home_page.click_login()
        # Open the manual withdrawal page in a new tab
        withdrawal_data = [
            {
                "investment_id": 1000015017,
                "uid": 120820,
                "amount": 56347.54
            },
            {
                "investment_id": 1000068199,
                "uid": 560889,
                "amount": 384602.21
            },
            {
                "investment_id": 1000104264,
                "uid": 828421,
                "amount": 1932.77
            },
            {
                "investment_id": 1000117710,
                "uid": 1073933,
                "amount": 62269.13
            },
            {
                "investment_id": 1000165881,
                "uid": 3535961,
                "amount": 110959.43
            },
            {
                "investment_id": 1000170071,
                "uid": 3674105,
                "amount": 110959.43
            },
            {
                "investment_id": 1000176216,
                "uid": 3842496,
                "amount": 401754.14
            },
            {
                "investment_id": 1000176462,
                "uid": 3847934,
                "amount": 105863.01
            },
            {
                "investment_id": 1000179436,
                "uid": 3919305,
                "amount": 118783.2
            },
            {
                "investment_id": 1000181940,
                "uid": 4000686,
                "amount": 125269.42
            },
            {
                "investment_id": 1000183354,
                "uid": 4054814,
                "amount": 137876.71
            },
            {
                "investment_id": 1000184556,
                "uid": 4090845,
                "amount": 137876.71
            },
            {
                "investment_id": 1000186483,
                "uid": 4168567,
                "amount": 464942.86
            },
            {
                "investment_id": 1000199861,
                "uid": 4418740,
                "amount": 81534.25
            },
            {
                "investment_id": 1000201963,
                "uid": 4432881,
                "amount": 44728.76
            },
            {
                "investment_id": 1000202033,
                "uid": 4433635,
                "amount": 28032.88
            },
            {
                "investment_id": 1000207251,
                "uid": 4471550,
                "amount": 10136.99
            },
            {
                "investment_id": 1000231606,
                "uid": 4635564,
                "amount": 108493.15
            },
            {
                "investment_id": 1000252950,
                "uid": 4799647,
                "amount": 89268.49
            },
            {
                "investment_id": 1000254761,
                "uid": 4817960,
                "amount": 87452.06
            },
            {
                "investment_id": 1000259311,
                "uid": 4875207,
                "amount": 78345.21
            }
        ]

        # Open the manual withdrawal page in a new tab and perform the tasks
        for data in withdrawal_data:
            self._open_new_tab(home_page, f'''https://admin.faircent.com/admins/escrow_passbook/{data["uid"]}''')
            # Locate the element
            # Extract the text content

            self._open_new_tab(home_page, "https://admin.faircent.com/admins/withdraw/wallet/maually")

            # Get the current URL and verify
            current_url = self.driver.current_url
            if current_url == "https://admin.faircent.com/admins/withdraw/wallet/maually":
                time.sleep(10)
                # Perform the tasks with the given data
                self._perform_withdrawal(data["investment_id"], data["amount"])
                self._open_new_tab(home_page, f'''https://admin.faircent.com/admins/escrow_passbook/{data["uid"]}''')

            else:
                print(f"Unexpected URL: {current_url}")

            # Close the tab and switch back to the previous one if needed
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def _open_new_tab(self, home_page, url):
        """
        Helper method to open a new tab and navigate to the given URL.
        """
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the latest tab
        home_page.open_page(url)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))  # Wait until the URL is fully loaded

    def _perform_withdrawal(self, investment_id_value, amount_value):
        """
        Perform the withdrawal process with given investment ID and amount.
        """
        investment_id = self.driver.find_element(By.ID, "edit-inv-id")
        investment_id.send_keys(investment_id_value)

        enter_amount = self.driver.find_element(By.ID, "edit-amount")
        enter_amount.clear()  # Clear any pre-existing value

        checkbox = self.driver.find_element(By.ID, "edit-all-amount")
        withdrawn_submit = self.driver.find_element(By.ID, "edit-submit")
        use = False
        if amount_value and float(amount_value) > 0:
            use = True
        if use and not checkbox.is_selected():
            if checkbox.is_selected():
                checkbox.click()
            enter_amount.send_keys(amount_value)

            withdrawn_submit.click()
        else:
            checkbox.click()
            time.sleep(10)
            withdrawn_submit.click()

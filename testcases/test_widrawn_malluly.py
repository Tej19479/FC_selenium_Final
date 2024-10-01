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
            {"uid": 4740445, "investment_id": 1000246893, "amount": 71506.86},
            {"uid": 4789807, "investment_id": 1000251254, "amount": 85150.68},
            {"uid": 4804387, "investment_id": 1000253356, "amount": 88767.12},
            {"uid": 4820695, "investment_id": 1000254997, "amount": 55561.65},
            {"uid": 4843276, "investment_id": 1000256127, "amount": 86136.99},
            {"uid": 5102848, "investment_id": 1000283467, "amount": 59835.61},
            {"uid": 5205229, "investment_id": 1000293660, "amount": 46356.16},
            {"uid": 5253242, "investment_id": 1000297451, "amount": 40767.12},
            {"uid": 5374934, "investment_id": 1000304232, "amount": 26630.14},
            {"uid": 5403152, "investment_id": 1000306334, "amount": 26301.37},
            {"uid": 5407841, "investment_id": 1000306942, "amount": 26301.36},
            {"uid": 5480926, "investment_id": 1000314017, "amount": 12602.74},
            {"uid": 5488179, "investment_id": 1000314392, "amount": 12821.92},
            {"uid": 5567031, "investment_id": 1000319499, "amount": 4602.74},

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
            withdrawn_submit.click()

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
        #home_page.enter_username("Fc_admin")
        #home_page.enter_password("techlet@123")
        #query for investment dta check
        #select uid,unique_user_id as investment_id,(wallet-locked_amount) as amount from cent_virtual_account where unique_user_id in (1000213431,1000138302) and (wallet-locked_amount)>0

        home_page.click_login()
        # Open the manual withdrawal page in a new tab
        withdrawal_data = [
            {"investment_id": "1000257828", "amount": "305650.68", "uid": 4864135},

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
            use=True
        if use and not checkbox.is_selected():
            if checkbox.is_selected():
                checkbox.click()
            enter_amount.send_keys(amount_value)
            time.sleep(10)

            withdrawn_submit.click()
        else:
            checkbox.click()
            time.sleep(10)
            withdrawn_submit.click()

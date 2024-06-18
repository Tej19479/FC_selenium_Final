from selenium.webdriver.common.by import By
from utilities.utilities import Utilities


class Lend:
    def __init__(self, driver):
        self.driver = driver
        print(self.driver,"dddddddddddddddddddddddddddddddddd")
        self.MLP_Dashboard_locator = (By.XPATH, "(//a[@href='/lender/mlp/investview'])[1]")
        self.MLP_lend_screen = (By.XPATH, "//a[normalize-space(text())='LEND ']")
        self.MLP_lender_overview_screen_locator = (By.XPATH, "//a[text()='LENDING OVERVIEW ']")
        self.MLP_36Months_radio = (By.XPATH, "//input[@value='MLP36']")
        self.MLP_18Months_radio = (By.XPATH, "//input[@value='MLP18']")
        self.enter_amount_locator = (By.ID, "new_inevstment_amount")
        self.click_lend_button = (By.XPATH, "(//button[@class])[5]")
        self.use_escrow_checkbox = (By.ID, "use_escraw_balance")
        self.MLP_investment_button = (By.XPATH, "//button[normalize-space()='LEND']")
        self.MLP_investment_borrower_pupop_locator = (By.ID, "edit-submit")

    # def open_page(self, url: str):
    #     print("url", url)
    #     print("self driver", self.driver)
    #     self.driver.get(url)

    def mlp_lend_screens(self):
        print(self.MLP_lend_screen)
        # self.driver.find_element(*self.MLP_lend_screen).click()
        Utilities.click_element(self.driver, self.MLP_lend_screen)

    def mlp_lender_overview_screen(self):
        Utilities.mouseHover(self.driver, self.MLP_lender_overview_screen_locator)
        Utilities.click_element(self.driver, self.MLP_lender_overview_screen_locator)

    def mlp_investment_plan_click(self, data: str):
        print(data)
        if data == "18Months":

            self.driver.find_element(*self.MLP_18Months_radio).click()

        elif data == "36Months":

            self.driver.find_element(*self.MLP_36Months_radio).click()
           # Utilities.mouseHover(self.driver, self.driver.find_element(*self.MLP_36Months_radio))

    def mlp_enter_investment_amount(self, amount: int):
        try:
            # Convert amount to string
            amount_str = str(amount)

            # Locate the element
            element = self.driver.find_element(*self.enter_amount_locator)

            # Clear any pre-existing text in the input field
            element.clear()

            # Enter the amount
            element.send_keys(amount_str)

            # Logging the action for confirmation
            print(f"Entered amount: {amount_str}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_lend(self):
        self.driver.find_element(*self.click_lend_button).click()

    def use_escrow(self, use: bool):
        checkbox = self.driver.find_element(*self.use_escrow_checkbox)
        if use and not checkbox.is_selected():
            checkbox.click()
        elif not use and checkbox.is_selected():
            checkbox.click()

    def submit_investment(self):
        Utilities.click_element(self.driver, self.MLP_investment_button)

    def investment_continue_button(self):
        Utilities.click_element(self.driver, self.MLP_investment_borrower_pupop_locator)

    def mlp_Dashboard(self):
        Utilities.click_element(self.driver, self.MLP_Dashboard_locator)

from selenium.webdriver.common.by import By
from utilities.utilities import Utilities


class Lender_dashboard:
    def __init__(self, driver):  # Corrected the constructor method
        print("Lender dashboard calling")
        self.driver = driver
        self.Faircent_double_open_locator = (By.XPATH, "//a[@href='/fsigp/investView']")
        self.Faircent_12Month_plan_locator = (By.XPATH, "//label[text()='12 Month Plan']")
        self.Faircent_6Month_plan_locator = (By.XPATH, "//label[text()='6 Month Plan']")
        self.Faircent_3Month_plan_locator = (By.XPATH, "//label[text()='3 Month Plan']")
        self.Faircent_24Month_plan_locator = (By.XPATH, "//label[text()='24 Month Plan']")
        self.Faircent_36Month_plan_locator = (By.XPATH, "//label[text()='36 Month Plan']")
        self.Enter_amount_locator = (By.ID, "edit-investment-amount")
        self.Use_Escrow_locator = (By.ID, "use_escraw_balance")
        self.Rinvest_slider_locator = (By.XPATH, "(//span[@class='slider round'])[2]")  # Corrected this locator
        self.Continue_locator = (By.XPATH, "//button[normalize-space(text())='Continue']")
        self.Fundview_locator = (By.XPATH, "//a[normalize-space(text())='Funding Overview']")

        print("Locator initialized:", self.Faircent_double_open_locator)

    def Lend_Screen_click(self):
        # print("Clicking Faircent double open locator")
        # ll = (By.XPATH, "//a[@href='/fsigp/investView']")

        Utilities.click_element(self.driver, self.Faircent_double_open_locator)
        # self.driver.find_element(self.Faircent_double_open_locator).click()

    def Fd_plan_section(self, plan_name: str):
        print(f"Selecting FD plan: {plan_name}")
        if plan_name.replace(" ", "").lower() == "12months":
            self.driver.find_element(*self.Faircent_12Month_plan_locator).click()
        elif plan_name.replace(" ", "").lower() == "6months":
            self.driver.find_element(*self.Faircent_6Month_plan_locator).click()
        elif plan_name.replace(" ", "").lower() == "3months":
            self.driver.find_element(*self.Faircent_3Month_plan_locator).click()
        elif plan_name.replace(" ", "").lower() == "24months":
            self.driver.find_element(*self.Faircent_24Month_plan_locator).click()
        elif plan_name.replace(" ", "").lower() == "36months":
            self.driver.find_element(*self.Faircent_36Month_plan_locator).click()

    def enter_investment_amount(self, amount: int):
        print(f"Entering investment amount: {amount}")
        self.driver.find_element(*self.Enter_amount_locator).send_keys(amount)

    def use_escrow(self, use: bool):
        print(f"Setting use escrow to: {use}")
        checkbox = self.driver.find_element(*self.Use_Escrow_locator)
        if use and not checkbox.is_selected():
            checkbox.click()
        elif not use and checkbox.is_selected():
            checkbox.click()

    def toggle_rinvest_slider(self, use: bool):  # Renamed the method to avoid conflict
        print(f"Setting reinvest slider to: {use}")
        slider = self.driver.find_element(*self.Rinvest_slider_locator)
        if use and not slider.is_selected():
            slider.click()
        elif not use and slider.is_selected():
            slider.click()

    def submit_investment(self):
        print("Submitting investment")
        Utilities.click_element(self.driver, self.Continue_locator)

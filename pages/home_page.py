from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.Faircentdouble import Lender_dashboard
from pages.mlp_investmentPage import Lend


class Homepage(LoginPage, Lender_dashboard,Lend):
    def __init__(self, driver):
        LoginPage.__init__(self,driver)
        Lender_dashboard.__init__(self,driver)
        Lend.__init__(self,driver)

        self.driver = driver
        self.home_login_button = (By.XPATH, '(//a[text()="Log In"])[1]')

    def open_page(self, url):
        print("url", url)
        print("self driver", self.driver)
        self.driver.maximize_window()

        self.driver.get(url)

    def log_button(self):
        self.driver.find_element(*self.home_login_button).click()

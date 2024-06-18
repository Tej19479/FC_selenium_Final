from selenium.webdriver.common.by import By

from utilities.utilities import Utilities


class LoginPage:

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_textbox = (By.ID, "edit-name")
        self.password_textbox = (By.ID, "edit-pass")
        self.login_button = (By.ID, "edit-submit")

    # def open_page(self, url):
    #     print("url", url)
    #     print("self driver", self.driver)
    #     self.driver.get(url)

    def enter_username(self, username):
        Utilities.mouseHover(self.driver, self.username_textbox)

        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)
        Utilities.mouseHover(self.driver, self.password_textbox)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

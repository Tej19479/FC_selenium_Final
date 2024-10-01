from selenium.webdriver.common.by import By

class Scrollbar:
    def __init__(self, driver):
        self.driver = driver
        self.scrollbar_xpath = (By.XPATH, '''//div[@class="container container-responsive home_new"]''')

    def get_url(self, url: str):
        self.driver.get(url)

    def get_scroll_height(self):
        print("Click")
        scroll_height = self.driver.find_element(*self.scrollbar_xpath).get_attribute('scrollHeight')
        scroll_offset = self.driver.find_element(*self.scrollbar_xpath).get_attribute('offsetHeight')
        print("Scroll Height:", scroll_height, "Offset Height:", scroll_offset)

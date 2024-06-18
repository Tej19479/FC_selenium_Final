import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class Utilities:

    @staticmethod
    def click_element(driver, locator):
        print("jjjjjjjjjjjjjjj", locator)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll into view and try again
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            element.click()

    @staticmethod
    def mouseHover(driver, locator):
        '''if not isinstance(element, WebElement):
            raise AttributeError("mouseHover requires a WebElement")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(9)'''
        print("mouse over", locator)

        try:
            wait = WebDriverWait(driver, 10)
            element_to_hover = wait.until(EC.visibility_of_element_located(locator))
            print("element_to_hover        ",element_to_hover)
            # Pass the locator as a tuple, e.g., (By.XPATH, 'your/xpath') Replace with the correct XPath
        except Exception as e:
            print(f"Error locating element: {e}")
            driver.quit()
            raise

        actions = ActionChains(driver)
        actions.move_to_element(element_to_hover).perform()
    # assert driver.find_element(By.ID, "move-status").text == "hovered

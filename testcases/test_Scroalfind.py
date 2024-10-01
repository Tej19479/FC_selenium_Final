import pytest
from FC_selenium_Final.pages.Scrollable import Scrollbar


@pytest.mark.usefixtures("setup")
class TestScroll:
    def test_scroable(self):
        scrollbar = Scrollbar(self.driver)
        print("Hello")
        scrollbar.get_scroll_height()

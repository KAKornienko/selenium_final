from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, selector, value):
        try:
            self.browser.find_element(selector, value)
        except NoSuchElementException:
            return False
        return True

from .base_page import BasePage
from .locators import ResultPageLocators


class ResultPage(BasePage):
    def should_be_result_url(self):
        assert 'search' in self.browser.current_url, 'Страница с результатами поиска не открылась'

    def first_result_link_test(self, expected_link):
        first_result = self.browser.find_element(*ResultPageLocators.FIRST_RESULT)
        first_link = first_result.get_attribute('href')
        assert expected_link in first_link, f'Первая ссылка не ведёт на {expected_link}'

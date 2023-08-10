from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_search_field(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD), 'Поля поиска нет'

    def search_field_enter(self, search_value):
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys(search_value)

    def should_be_suggests(self):
        assert self.is_element_present(*MainPageLocators.SUGGESTS), 'Таблицы с подсказками нет'

    def go_to_search_result(self):
        search_btn = self.browser.find_element(*MainPageLocators.SEARCH_BTN)
        search_btn.click()

    def should_be_menu(self):
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.click()
        assert self.is_element_present(*MainPageLocators.MENU), 'Кнопка меню отстутсвует'

    def go_to_images(self):
        menu = self.browser.find_element(*MainPageLocators.MENU)
        menu.click()
        images_btn = self.browser.find_element(*MainPageLocators.IMAGES)
        images_btn.click()

from .base_page import BasePage
from .locators import ImagesPageLocators


class ImagesPage(BasePage):
    def should_be_images_page(self):
        assert 'https://ya.ru/images/' == self.browser.current_url, 'Страница с картинками не открылась'

    def open_first_category(self):
        first_category = self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY)
        first_category.click()
        return first_category.text

    def should_be_category_name_in_search_field(self, category_name):
        search_input = self.browser.find_element(*ImagesPageLocators.SEARCH_INPUT)
        search_input_name = search_input.get_attribute('value')
        assert category_name == search_input_name, 'Название категории не отображается в поле поиска'

    def open_first_image(self):
        first_image = self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE)
        first_image.click()

    def should_be_opened_image(self):
        assert 'img_url' in self.browser.current_url, 'Картинка не открылась'
        return self.browser.current_url

    def push_next_btn(self):
        next_btn = self.browser.find_element(*ImagesPageLocators.NEXT_BTN)
        next_btn.click()

    def should_be_image_change(self, first_image_url):
        assert self.browser.current_url != first_image_url, 'Картинка не сменилась'

    def push_back_btn(self):
        back_btn = self.browser.find_element(*ImagesPageLocators.BACK_BTN)
        back_btn.click()

    def should_be_the_first_image(self, first_image_url):
        assert self.browser.current_url == first_image_url, 'Картинка не вернулась на первую'

from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, '#text')
    SUGGESTS = (By.CSS_SELECTOR, '.mini-suggest__item')
    SEARCH_BTN = (By.CSS_SELECTOR, '.search3__button')
    MENU = (By.CSS_SELECTOR, '[title="Все сервисы"]')
    IMAGES = (By.CSS_SELECTOR, '[aria-label="Картинки"]')


class ResultPageLocators():
    FIRST_RESULT = (By.CSS_SELECTOR, '[accesskey="1"]')


class ImagesPageLocators():
    FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
    SEARCH_INPUT = (By.CSS_SELECTOR, '.input__control.mini-suggest__input')
    FIRST_IMAGE = (By.CSS_SELECTOR, '.serp-item_pos_0')
    NEXT_BTN = (By.CSS_SELECTOR, '.CircleButton_type_next')
    BACK_BTN = (By.CSS_SELECTOR, '.CircleButton_type_prev')

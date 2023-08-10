from .pages.main_page import MainPage
from .pages.result_page import ResultPage
from .pages.images_page import ImagesPage
import time


def test_guest_uses_search_field(browser):
    link = 'https://ya.ru/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_field()
    page.search_field_enter('Тензор')
    page.should_be_suggests()
    page.go_to_search_result()
    result_page = ResultPage(browser, browser.current_url)
    result_page.should_be_result_url()
    browser.implicitly_wait(1)
    result_page.first_result_link_test('tensor.ru')


def test_guest_uses_img_service(browser):
    link = 'https://ya.ru/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_menu()
    page.go_to_images()
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[-1])
    images_page = ImagesPage(browser, browser.current_url)
    images_page.should_be_images_page()
    first_category_name = images_page.open_first_category()
    images_page.should_be_category_name_in_search_field(first_category_name)
    images_page.open_first_image()
    time.sleep(1)
    first_image_url = images_page.should_be_opened_image()
    images_page.push_next_btn()
    time.sleep(1)
    images_page.should_be_image_change(first_image_url)
    images_page.push_back_btn()
    time.sleep(1)
    images_page.should_be_the_first_image(first_image_url)

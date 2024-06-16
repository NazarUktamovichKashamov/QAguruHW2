import pytest
from selene import browser, be, have


@pytest.fixture
def set_browser_size():
    browser.driver.set_window_size(1920, 1080)


@pytest.mark.usefixtures("set_browser_size")


def test_sum():
    browser.open('https://vk.com')
    browser.element('[id="index_email"]').type('example_phonenumber').press_enter()
    browser.element('[data-test-id="other-verification-methods"]').click()
    browser.element('[data-test-id="verificationMethod_password"]').click()
    browser.element('[name="password"]').type('example_password').press_enter()
    browser.element('[id="l_pr"]').click()
    browser.element('[id="owner_page_name"]').should(have.text('Назар'))


@pytest.mark.usefixtures("set_browser_size")


def test_sum1():
    browser.open('https:/bing.com')
    browser.element('[name="q"]').type('rweuvhbwerivbnwdeuicwjniujvhberiyuhiowgdbeebfvcerverfevbfvbetrbbnr').press_enter()
    browser.element('[id="b_results"]').should(have.text('Не удалось найти ни одного результата'))

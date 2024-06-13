import pytest
from selene import browser, be, have


@pytest.fixture
def set_browser_size():
    browser.driver.set_window_size(400, 400)


@pytest.mark.usefixtures("set_browser_size")


def test_sum():
    browser.open('https://vk.com')
    browser.element('[id="index_email"]').type('1').press_enter()
    browser.element('[data-test-id="other-verification-methods"]').click()
    browser.element('[data-test-id="verificationMethod_password"]').click()
    browser.element('[name="password"]').type('1').press_enter()
    browser.element('[id="l_pr"]').click()
    browser.element('[id="owner_page_name"]').should(have.text('Назар'))

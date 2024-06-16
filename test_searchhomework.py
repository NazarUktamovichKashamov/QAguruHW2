import pytest
from selene import browser, have


def test_validsearch():
    browser.open('https:/google.com')
    browser.element('[name=q]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_invalidsearch():
    browser.open('https:/bing.com')
    browser.element('[name="q"]').type('rweuvhbwerivbnwdeuicwjniujvhberiyuhiowgdbeebfvcerverfevbfvbetrbbnr').press_enter()
    browser.element('[id="b_results"]').should(have.text('Не удалось найти ни одного результата для rweuvhbwerivbnwdeuicwjniujvhberiyuhiowgdbeebfvcerverfevbfvbetrbbnr'))

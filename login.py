from pytest_bdd import scenarios, given, then, when, parsers
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 

scenarios('./login.feature')

LOGIN_PAGE = 'localhost:5000/'

@pytest.fixture()
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b


@given(parsers.parse('I navigate to login page'))
def navigateToLoginPage(browser):
    browser.get(LOGIN_PAGE)


@given(parsers.parse('I enter valid {username} and {password}'))
def enterUsernameAndPassword(browser, username, password):
    username_input = browser.find_element(By.ID, "username-input")
    username_input.clear()
    username_input.send_keys(username)
    password_input = browser.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(password)

@when(parsers.parse("I click on Submit button"))
def clickSubmit(browser):
    login_btn = browser.find_element(By.ID, "login-btn")
    login_btn.click()
    browser.implicitly_wait(10)

@then(parsers.parse("login is successful"))
def checkLoginState(browser):
    result_element = browser.find_element(By.ID, "login-result")
    result_text = result_element.get_attribute("innerHTML")
    assert result_text == "Login Successed"
    browser.quit()
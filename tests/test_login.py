from pages.login_page import LoginPage


def test_login_correct_username_and_password(page):
    login = LoginPage(page)
    login.open()

    assert login.h2_text.text_content() == "Login Page"

    login.submit_login(login.correct_username, login.correct_password)
    login.flash_should_contain("You logged into a secure area!")

def test_login_wrong_username(page):
    login = LoginPage(page)
    login.open()

    login.submit_login(login.invalid_username, login.correct_password)
    login.flash_should_contain("Your username is invalid!")

def test_login_wrong_password(page):
    login = LoginPage(page)
    login.open()

    login.submit_login(login.correct_username, login.invalid_password)
    login.flash_should_contain("Your password is invalid! ")

def test_login_and_logout(page):
    login = LoginPage(page)
    login.open()

    assert login.h2_text.text_content() == "Login Page"

    login.submit_login(login.correct_username, login.correct_password)
    login.flash_should_contain("You logged into a secure area!")

    login.submit_logout()
    login.flash_should_contain("You logged out of the secure area!")
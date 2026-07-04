from pages.login_page import LoginPage


def test_login_correct_username_and_password(page):
    login = LoginPage(page)
    login.open()

    assert login.h2_text.text_content() == "Login Page"



def test_login_wrong_username_and_password(page):
    pass

def test_login_and_logout(page):
    pass

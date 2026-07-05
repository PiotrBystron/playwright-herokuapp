from playwright.sync_api import Page


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.h2_text = page.locator("h2")
        self.flash_message = page.locator("#flash")

        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        
        self.login_button = page.locator(".radius")
        self.logout_button = page.locator(".button.secondary.radius")

        self.correct_username = "tomsmith"
        self.correct_password = "SuperSecretPassword!"

        self.invalid_username = "test"
        self.invalid_password = "123!"

    def open(self):
        self.page.goto(self.URL)

    def get_flash_text(self):
        return self.flash_message.text_content()
    
    def flash_should_contain(self, text: str):
        from playwright.sync_api import expect
        expect(self.flash_message).to_contain_text(text)

    def submit_login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def submit_logout(self):
        self.logout_button.click()
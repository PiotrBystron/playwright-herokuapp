from playwright.sync_api import Page


class LoginPage:

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.h2_text = page.locator("h2")


    def open(self):
        self.page.goto(self.URL)

from playwright.sync_api import Page, expect


class KeyPressesPage:
    URL = "https://the-internet.herokuapp.com/key_presses"

    def __init__(self, page: Page):
        self.page = page
        self.target = page.locator("#target")
        self.result = page.locator("#result")

    def open(self):
        self.page.goto(self.URL)

    def press_key(self, key: str):
        self.target.press(key)

    def result_should_have_text(self, text: str):
        expect(self.result).to_have_text(text)
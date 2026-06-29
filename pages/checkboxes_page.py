from playwright.sync_api import Page


class CheckboxesPage:

    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, page: Page):
        self.page = page

        self.checkbox1 = page.locator("input[type='checkbox']").nth(0)
        self.checkbox2 = page.locator("input[type='checkbox']").nth(1)

    def open(self):
        self.page.goto(self.URL)

    def check_first(self):
        self.checkbox1.check()

    def uncheck_second(self):
        self.checkbox2.uncheck()

    def is_first_checked(self):
        return self.checkbox1.is_checked()

    def is_second_checked(self):
        return self.checkbox2.is_checked()
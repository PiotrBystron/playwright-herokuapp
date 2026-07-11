from playwright.sync_api import Page, expect


class DropdownPage:

    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, page: Page):
        self.page = page

        self.dropdown = page.get_by_role("combobox")

    def open(self):
        self.page.goto(self.URL)

    def select_option(self, value: str):
        self.dropdown.select_option(value)

    def selected_value_should_be(self, value: str):
        expect(self.dropdown).to_have_value(value)

    def get_selected_value(self):
        return self.dropdown.input_value()
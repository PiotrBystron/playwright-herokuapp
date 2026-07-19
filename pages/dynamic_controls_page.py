from playwright.sync_api import Page, expect
import pytest


class DynamicControlsPage:

    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    def __init__(self, page: Page):
        self.page = page

        self.input = page.locator("input[type='text']")

        self.checkbox = page.get_by_role("checkbox")

        self.remove_button = page.get_by_role("button", name="Remove")
        self.add_button = page.get_by_role("button", name="Add")

        self.enable_button = page.get_by_role("button", name="Enable")
        self.disable_button = page.get_by_role("button", name="Disable")

        self.message = page.locator("#message")

    def open(self):
        self.page.goto(self.URL)

    # Checkbox

    def remove_checkbox(self):
        self.remove_button.click()

    def add_checkbox(self):
        self.add_button.click()

    def checkbox_should_be_visible(self):
        expect(self.checkbox).to_be_visible()

    def checkbox_should_be_hidden(self):
        expect(self.checkbox).to_be_hidden()

    # Input

    def enable_input(self):
        self.enable_button.click()

    def disable_input(self):
        self.disable_button.click()

    def input_should_be_enabled(self):
        expect(self.input).to_be_enabled()

    def input_should_be_disabled(self):
        expect(self.input).to_be_disabled()

    def fill_input(self, text: str):
        self.input.fill(text)

    def input_should_have_value(self, text: str):
        expect(self.input).to_have_value(text)

    def input_should_not_accept_text(self, text: str):
        with pytest.raises(Exception):
            self.input.fill(text, timeout=500)

    # Message

    def message_should_contain(self, text: str):
        expect(self.message).to_contain_text(text)
from playwright.sync_api import Page, expect


class JavaScriptAlertsPage:
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def __init__(self, page: Page):
        self.page = page

        self.js_alert_button = page.get_by_role(
            "button",
            name="Click for JS Alert"
        )

        self.js_confirm_button = page.get_by_role(
            "button",
            name="Click for JS Confirm"
        )

        self.js_prompt_button = page.get_by_role(
            "button",
            name="Click for JS Prompt"
        )

        self.result = page.locator("#result")

    def open(self):
        self.page.goto(self.URL)

    def click_js_alert(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.js_alert_button.click()

    def click_js_confirm_ok(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.js_confirm_button.click()

    def click_js_confirm_cancel(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.js_confirm_button.click()

    def click_js_prompt(self, text: str):
        self.page.once(
            "dialog",
            lambda dialog: dialog.accept(text)
        )
        self.js_prompt_button.click()

    def result_should_have_text(self, text: str):
        expect(self.result).to_have_text(text)
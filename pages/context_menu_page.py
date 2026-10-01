from playwright.sync_api import Page


class ContextMenuPage:
    URL = "https://the-internet.herokuapp.com/context_menu"

    def __init__(self, page: Page):
        self.page = page
        self.hot_spot = page.locator("#hot-spot")

    def open(self):
        self.page.goto(self.URL)

    def click_context_menu(self):
        message = None

        def handle_dialog(dialog):
            nonlocal message
            message = dialog.message
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.hot_spot.click(button="right")
        return message
from playwright.sync_api import Page, expect


class WindowsPage:
    URL = "https://the-internet.herokuapp.com/windows"

    def __init__(self, page: Page):
        self.page = page
        self.click_here_link = page.get_by_role(
            "link",
            name="Click Here"
        )

    def open(self):
        self.page.goto(self.URL)

    def open_new_window(self):
        with self.page.expect_popup() as popup_info:
            self.click_here_link.click()
        return popup_info.value
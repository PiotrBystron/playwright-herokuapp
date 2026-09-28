from playwright.sync_api import Page


class StatusCodesPage:
    URL = "https://the-internet.herokuapp.com/status_codes"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def click_status_code(self, code: str):
        with self.page.expect_response(
            f"**/status_codes/{code}"
        ) as response_info:
            self.page.get_by_role(
                "link",
                name=code
            ).click()
        return response_info.value
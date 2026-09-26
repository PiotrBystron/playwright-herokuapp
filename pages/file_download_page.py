from playwright.sync_api import Page


class FileDownloadPage:
    URL = "https://the-internet.herokuapp.com/download"

    def __init__(self, page: Page):
        self.page = page
        self.files = page.locator("#content a")

    def open(self):
        self.page.goto(self.URL)

    def download_file(self, filename: str):
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name=filename).click()
        return download_info.value
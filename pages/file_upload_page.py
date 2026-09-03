from playwright.sync_api import Page, expect


class FileUploadPage:
    URL = "https://the-internet.herokuapp.com/upload"

    def __init__(self, page: Page):
        self.page = page

        self.file_input = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")

        self.uploaded_header = page.get_by_role("heading", name="File Uploaded!")
        self.uploaded_file = page.locator("#uploaded-files")

    def open(self):
        self.page.goto(self.URL)

    def upload_file(self, file_path: str):
        self.file_input.set_input_files(file_path)
        self.upload_button.click()

    def uploaded_header_should_be_visible(self):
        expect(self.uploaded_header).to_be_visible()

    def uploaded_file_should_be(self, filename: str):
        expect(self.uploaded_file).to_have_text(filename)

    def click_upload(self):
        self.upload_button.click()

    def upload_result_should_not_be_visible(self):
        expect(self.uploaded_header).not_to_be_visible()
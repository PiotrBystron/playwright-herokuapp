from playwright.sync_api import Page, expect


class DynamicLoadingPage:
    URL_page_1 = "https://the-internet.herokuapp.com/dynamic_loading/1"
    URL_page_2 = "https://the-internet.herokuapp.com/dynamic_loading/2"

    def __init__(self, page: Page):
        self.page = page
        self.start_button = page.get_by_role("button", name="Start")
        self.hello_world = page.locator("#finish h4")
        self.loading = page.locator("#loading")

    def open_page_1(self):
        self.page.goto(self.URL_page_1)

    def open_page_2(self):
        self.page.goto(self.URL_page_2)

    def click_start(self):
        self.start_button.click()

    def hello_world_should_be_visible(self):
        expect(self.hello_world).to_be_visible()

    def hello_world_should_have_text(self, text: str):
        expect(self.hello_world).to_have_text(text)

    def hello_world_should_not_be_visible(self):
        expect(self.hello_world).not_to_be_visible()

    def loading_should_disappear(self):
        expect(self.loading).to_be_hidden(timeout=10000)

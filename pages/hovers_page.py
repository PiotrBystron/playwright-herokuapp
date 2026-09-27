from playwright.sync_api import Page, expect


class HoversPage:
    URL = "https://the-internet.herokuapp.com/hovers"

    def __init__(self, page: Page):
        self.page = page
        self.user_images = page.locator(".figure")
        self.user_names = page.locator(".figcaption h5")
        self.profile_links = page.locator(".figcaption a")

    def open(self):
        self.page.goto(self.URL)

    def hover_user(self, index: int):
        self.user_images.nth(index).hover()

    def user_name_should_be(self, index: int, text: str):
        expect(self.user_names.nth(index)).to_have_text(text)

    def profile_link_should_be_visible(self, index: int):
        expect(self.profile_links.nth(index)).to_be_visible()

    def click_profile(self, index: int):
        self.profile_links.nth(index).click()
from playwright.sync_api import Page


class AddRemoveElementsPage:

    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, page: Page):
        self.page = page
        
        self.add_button = page.get_by_role("button", name="Add Element")
        self.delete_button = page.locator(".added-manually")

    def open(self):
        self.page.goto(self.URL)

    def click_add_button(self):
        self.add_button.click()

    def click_delete_button(self):
        self.delete_button.first.click()

    def is_delete_visible(self):
        return self.delete_button.is_visible()

    def get_delete_count(self):
        return self.delete_button.count()


from playwright.sync_api import Page


class NotificationMessagesPage:
    URL = "https://the-internet.herokuapp.com/notification_message"

    def __init__(self, page: Page):
        self.page = page
        self.click_here = page.get_by_role("link", name="Click here")
        self.notification = page.locator("#flash")

    def open(self):
        self.page.goto(self.URL)

    def click_for_notification(self):
        self.click_here.click()

    def get_notification_text(self):
        # replace method is used to remove "x" (close) element from the notification.
        return self.notification.text_content().replace("×", "").strip()
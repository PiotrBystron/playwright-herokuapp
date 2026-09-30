from pages.notification_messages_page import NotificationMessagesPage


def test_notification_message(page):
    notification = NotificationMessagesPage(page)
    notification.open()
    notification.click_for_notification()
    message = notification.get_notification_text()

    assert message is not None
    assert message.strip() in [
        "Action successful",
        "Action unsuccesful, please try again",
    ]
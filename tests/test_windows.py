from playwright.sync_api import expect
from pages.windows_page import WindowsPage


def test_open_new_window(page):
    windows = WindowsPage(page)
    windows.open()

    new_page = windows.open_new_window()

    expect(
        new_page.get_by_role(
            "heading",
            name="New Window"
        )
    ).to_be_visible()
from pages.context_menu_page import ContextMenuPage


def test_context_menu(page):
    context_menu = ContextMenuPage(page)

    context_menu.open()
    message = context_menu.click_context_menu()
    assert message == "You selected a context menu"
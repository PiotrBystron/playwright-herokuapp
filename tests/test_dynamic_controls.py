from pages.dynamic_controls_page import DynamicControlsPage


def test_remove_checkbox(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.checkbox_should_be_visible()

    dynamic.remove_checkbox()

    dynamic.message_should_contain("It's gone!")
    dynamic.checkbox_should_be_hidden()


def test_add_checkbox(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.remove_checkbox()
    dynamic.message_should_contain("It's gone!")

    dynamic.add_checkbox()

    dynamic.message_should_contain("It's back!")
    dynamic.checkbox_should_be_visible()


def test_enabled_input_should_be_empty(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.enable_input()

    dynamic.message_should_contain("It's enabled!")
    dynamic.input_should_be_enabled()

    dynamic.input_should_have_value("")


def test_enable_input(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.input_should_be_disabled()

    dynamic.enable_input()

    dynamic.message_should_contain("It's enabled!")
    dynamic.input_should_be_enabled()

    dynamic.fill_input("Playwright test")
    dynamic.input_should_have_value("Playwright test")


def test_disable_input(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.enable_input()
    dynamic.message_should_contain("It's enabled!")

    dynamic.disable_input()

    dynamic.message_should_contain("It's disabled!")
    dynamic.input_should_be_disabled()


def test_disabled_input_should_not_accept_text(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.enable_input()
    dynamic.message_should_contain("It's enabled!")

    dynamic.fill_input("Playwright test")

    dynamic.disable_input()
    dynamic.message_should_contain("It's disabled!")

    dynamic.input_should_be_disabled()

    dynamic.input_should_not_accept_text("Playwright 123")
    dynamic.input_should_have_value("Playwright test")


def test_full_dynamic_controls_flow(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.remove_checkbox()
    dynamic.message_should_contain("It's gone!")
    dynamic.checkbox_should_be_hidden()

    dynamic.add_checkbox()
    dynamic.message_should_contain("It's back!")
    dynamic.checkbox_should_be_visible()

    dynamic.enable_input()
    dynamic.message_should_contain("It's enabled!")
    dynamic.input_should_be_enabled()

    dynamic.fill_input("Playwright test")
    dynamic.input_should_have_value("Playwright test")

    dynamic.disable_input()
    dynamic.message_should_contain("It's disabled!")
    dynamic.input_should_be_disabled()


def test_input_value_should_be_preserved_after_reenable(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.enable_input()
    dynamic.fill_input("Playwright test")

    dynamic.disable_input()
    dynamic.message_should_contain("It's disabled!")

    dynamic.enable_input()
    dynamic.message_should_contain("It's enabled!")

    dynamic.input_should_have_value("Playwright test")
    
    dynamic.fill_input("Playwright 1")
    dynamic.input_should_have_value("Playwright 1")


def test_multiple_enable_disable_actions(page):
    dynamic = DynamicControlsPage(page)
    dynamic.open()

    dynamic.enable_input()
    dynamic.input_should_be_enabled()

    dynamic.fill_input("Playwright test")
    
    for _ in range(3):
        dynamic.disable_input()
        dynamic.input_should_be_disabled()

        dynamic.enable_input()
        dynamic.input_should_be_enabled()

    dynamic.input_should_have_value("Playwright test")
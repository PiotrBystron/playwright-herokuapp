from pages.dropdown_page import DropdownPage


def test_select_option_1(page):
    dropdown = DropdownPage(page)
    dropdown.open()

    dropdown.select_option("1")
    dropdown.selected_value_should_be("1")


def test_select_option_2(page):
    dropdown = DropdownPage(page)
    dropdown.open()

    dropdown.select_option("2")
    dropdown.selected_value_should_be("2")


def test_change_selected_option(page):
    dropdown = DropdownPage(page)
    dropdown.open()

    dropdown.select_option("1")
    dropdown.selected_value_should_be("1")

    dropdown.select_option("2")
    dropdown.selected_value_should_be("2")


def test_default_selected_option(page):
    dropdown = DropdownPage(page)
    dropdown.open()

    dropdown.selected_value_should_be("")

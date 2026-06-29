from pages.checkboxes_page import CheckboxesPage


def test_checkboxes(page):
    checkboxes = CheckboxesPage(page)
    checkboxes.open()
    checkboxes.check_first()
    checkboxes.uncheck_second()

    assert checkboxes.is_first_checked()
    assert not checkboxes.is_second_checked()


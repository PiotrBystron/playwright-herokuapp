from pages.add_remove_elements_page import AddRemoveElementsPage


def test_add_remove_elements(page):
    add_remove = AddRemoveElementsPage(page)
    add_remove.open()

    add_remove.click_add_button()
    assert add_remove.is_delete_visible()
    
    add_remove.click_delete_button()
    assert not add_remove.is_delete_visible()


def test_add_10_elements_and_remove(page):
    add_remove = AddRemoveElementsPage(page)
    add_remove.open()

    for _ in range(10):
        add_remove.click_add_button()

    assert add_remove.get_delete_count() == 10

    for _ in range(10):
        add_remove.click_delete_button()

    assert add_remove.get_delete_count() == 0

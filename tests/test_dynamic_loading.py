from pages.dynamic_loading_page import DynamicLoadingPage


def test_hello_world_appears(page):
    dynamic = DynamicLoadingPage(page)
    dynamic.open_page_1()

    dynamic.hello_world_should_not_be_visible()
    
    dynamic.click_start()

    dynamic.loading_should_disappear()
    dynamic.hello_world_should_be_visible()
    dynamic.hello_world_should_have_text("Hello World!")


def test_hello_world_is_rendered_after_start(page):
    dynamic = DynamicLoadingPage(page)
    dynamic.open_page_2()

    dynamic.click_start()

    dynamic.loading_should_disappear()
    dynamic.hello_world_should_be_visible()
    dynamic.hello_world_should_have_text("Hello World!")
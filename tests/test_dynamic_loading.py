from pages.dynamic_loading_page import DynamicLoadingPage


def test_hello_world_appears(page):
    dynamic = DynamicLoadingPage(page)
    dynamic.open()

    dynamic.hello_world_should_not_be_visible()
    
    dynamic.click_start()

    dynamic.loading_should_disappear()
    dynamic.hello_world_should_be_visible()
    dynamic.hello_world_should_have_text("Hello World!")
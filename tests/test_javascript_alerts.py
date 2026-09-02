from pages.javascript_alerts_page import JavaScriptAlertsPage


def test_js_alert(page):
    alerts = JavaScriptAlertsPage(page)
    alerts.open()

    alerts.click_js_alert()
    alerts.result_should_have_text("You successfully clicked an alert")


def test_js_confirm_ok(page):
    alerts = JavaScriptAlertsPage(page)
    alerts.open()

    alerts.click_js_confirm_ok()
    alerts.result_should_have_text("You clicked: Ok")


def test_js_confirm_cancel(page):
    alerts = JavaScriptAlertsPage(page)
    alerts.open()

    alerts.click_js_confirm_cancel()
    alerts.result_should_have_text("You clicked: Cancel")


def test_js_prompt(page):
    alerts = JavaScriptAlertsPage(page)
    alerts.open()

    alerts.click_js_prompt("Playwright")
    alerts.result_should_have_text("You entered: Playwright")
import pytest
from pages.key_presses_page import KeyPressesPage


@pytest.mark.parametrize(
    "key, expected",
    [
        ("a", "A"),
        ("z", "Z"),
        ("1", "1"),
        ("F1", "F1"),
        ("F12", "F12"),
        ("[", "OPEN_BRACKET"),
        ("Tab", "TAB"),
        ("Space", "SPACE"),
        ("Escape", "ESCAPE"),
        ("Delete", "DELETE"),
        ("Control", "CONTROL"),
    ]
)
def test_press_key(page, key, expected):
    key_presses = KeyPressesPage(page)
    key_presses.open()
    key_presses.press_key(key)
    key_presses.result_should_have_text(f"You entered: {expected}")
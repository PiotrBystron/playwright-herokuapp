from pages.hovers_page import HoversPage


def test_hover_user_profile_1(page):
    hovers = HoversPage(page)
    hovers.open()
    hovers.hover_user(0)
    hovers.user_name_should_be(
        0,
        "name: user1"
    )
    hovers.profile_link_should_be_visible(0)

def test_hover_user_profile_2(page):
    hovers = HoversPage(page)
    hovers.open()
    hovers.hover_user(1)
    hovers.user_name_should_be(
        1,
        "name: user2"
    )
    hovers.profile_link_should_be_visible(1)

def test_hover_user_profile_3(page):
    hovers = HoversPage(page)
    hovers.open()
    hovers.hover_user(2)
    hovers.user_name_should_be(
        2,
        "name: user3"
    )
    hovers.profile_link_should_be_visible(2)
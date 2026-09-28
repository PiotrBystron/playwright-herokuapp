import pytest
from pages.status_codes_page import StatusCodesPage


@pytest.mark.parametrize(
    "status_code",
    [
        "200",
        "301",
        "404",
        "500",
    ]
)
def test_status_code_response(page, status_code):
    status = StatusCodesPage(page)
    status.open()

    response = status.click_status_code(status_code)
    assert response.status == int(status_code)
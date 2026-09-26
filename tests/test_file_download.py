from playwright.sync_api import expect
from pages.file_download_page import FileDownloadPage


def test_download_report_txt(page):
    download_page = FileDownloadPage(page)
    download_page.open()

    download = download_page.download_file("report.txt")
    assert download.suggested_filename == "report.txt"

def test_download_icon_png(page):
    download_page = FileDownloadPage(page)
    download_page.open()

    download = download_page.download_file("icon.png")
    assert download.suggested_filename == "icon.png"
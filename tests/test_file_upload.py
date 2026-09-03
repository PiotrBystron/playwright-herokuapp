from pathlib import Path
from pages.file_upload_page import FileUploadPage


def test_upload_txt_file(page):
    upload = FileUploadPage(page)
    upload.open()

    file_path = Path("test_data/upload_test_file.txt")

    upload.upload_file(str(file_path))

    upload.uploaded_header_should_be_visible()
    upload.uploaded_file_should_be("upload_test_file.txt")


def test_upload_without_file(page):
    upload = FileUploadPage(page)
    upload.open()

    upload.click_upload()
    upload.upload_result_should_not_be_visible()
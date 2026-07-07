# UI Tests with Playwright

A sample UI automation project demonstrating web testing using Python, Pytest, and Playwright.

The project uses the public test website:
https://the-internet.herokuapp.com

## Features

- Page Object Model (POM)
- Pytest test framework
- Playwright browser automation
- Clear project structure
- Easy to extend with new test cases

## Test Scenarios

### Checkboxes
- Verify checkbox states
- Check and uncheck checkboxes

### Add/Remove Elements
- Add a single element
- Add multiple elements
- Remove elements
- Verify the number of Delete buttons

### Login
- Successful login
- Invalid username
- Invalid password
- Login and logout flow

## Project Structure

```
playwright-herokuapp/
│
├── pages/
│   ├── add_remove_elements_page.py
│   ├── checkboxes_page.py
│   └── login_page.py
│
├── tests/
│   ├── test_add_remove_elements.py
│   ├── test_checkboxes.py
│   └── test_login.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/PiotrBystron/playwright-herokuapp.git
cd playwright-herokuapp
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Run the tests

Run all tests:

```bash
pytest
```

Run all tests and generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

A detailed test report will be generated as `report.html` in the project directory.

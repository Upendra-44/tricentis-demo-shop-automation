# Tricentis Demo Shop UI Automation

Browser-based UI tests for the public [Tricentis Demo Web Shop](https://demowebshop.tricentis.com/), built with Python, Selenium WebDriver, pytest, and the Page Object Model.

The suite currently covers 15 pytest cases across home page navigation, registration, login, product search, adding a configurable product to the cart, and the initial checkout view. It is a portfolio demonstration against a shared public test site, not a production storefront test system.

## Requirements

- Windows 10/11
- Python 3.10 or later
- Google Chrome

Selenium Manager resolves the matching ChromeDriver automatically. GitHub Actions runs the same suite headlessly on a Windows runner.

## Setup

From PowerShell in the project directory, create a virtual environment and install dependencies:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Using the virtual environment's Python directly avoids needing to change PowerShell's script execution policy to activate it.

## Run Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Run only smoke tests:

```powershell
.\.venv\Scripts\python.exe -m pytest -v -m smoke
```

Run headlessly:

```powershell
$env:HEADLESS = "true"
.\.venv\Scripts\python.exe -m pytest -v
```

Generate a self-contained HTML report:

```powershell
.\.venv\Scripts\python.exe -m pytest -v --html=reports/report.html --self-contained-html
```

Failed tests save screenshots under `screenshots/`. Reports and screenshots are ignored by Git; the CI workflow uploads them as an artifact when available.

## Configuration

Settings can be provided through environment variables or a local `.env` file. Copy `.env.example` to `.env` to start; `.env` is excluded from Git.

| Variable | Default | Description |
| --- | --- | --- |
| `BASE_URL` | `https://demowebshop.tricentis.com` | Demo store URL |
| `HEADLESS` | `false` | Run Chrome without a visible window (`true`/`false`) |
| `EXPLICIT_WAIT` | `12` | Selenium wait timeout in seconds |

## Project Layout

```text
config/       Environment-backed settings
pages/        Page Objects and shared browser actions
tests/        Feature-focused pytest tests
test_data/    Test data, original 56-case workbook, and CSV index
utils/        Test data helpers
reports/      Generated HTML reports (ignored by Git)
screenshots/  Failure screenshots (ignored by Git)
```

## Scope and Limitations

- `test_data/original_test_cases.xlsx` documents 56 scenarios; `test_data/test_case_inventory.csv` provides a CSV index. Only the cases described above are currently automated, so the workbook is not evidence that all scenarios have been tested.
- Registration creates a unique `example.com` test address for each run; it does not use a real mailbox.
- Checkout coverage verifies the cart's checkout terms view and deliberately does not place an order.
- Tests depend on a public shared demo site, internet access, and its current UI. A failure can reflect site availability or a site change, not only a test defect.

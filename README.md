\# SauceDemo E2E Test Suite



\[!\[E2E tests](https://github.com/agawa03/saucedemo-e2e/actions/workflows/tests.yml/badge.svg)](https://github.com/agawa03/saucedemo-e2e/actions/workflows/tests.yml)



Automated UI and API tests built with \*\*Python, pytest, and Playwright\*\*, running in CI across three browsers.







\## What this tests



\- \*\*UI:\*\* \[saucedemo.com](https://www.saucedemo.com), a practice e-commerce site (login, inventory, cart, checkout)

\- \*\*API:\*\* \[JSONPlaceholder](https://jsonplaceholder.typicode.com), a free fake REST API



Both are public practice targets, chosen to demonstrate framework design, CI, and testing habits.



\## Features



\- Page Object Model for maintainable locators and actions

\- Reusable pytest fixtures (`login\_page`, `logged\_in`, `checkout\_page`)

\- Parametrized tests for invalid credentials and checkout validation

\- API tests using Playwright's request context

\- `smoke` and `regression` markers for running test subsets

\- Cross-browser CI matrix (Chromium, Firefox, WebKit)

\- HTML reports published to GitHub Pages

\- Traces and screenshots captured automatically on failure

\- Linting and formatting enforced in CI with ruff



\## Test coverage



| Area      | Tests | What is covered                                          |

|-----------|-------|----------------------------------------------------------|

| Login     | 5     | Valid login, locked-out user, 3 invalid credential cases |

| Inventory | 5     | Product count, sorting by name and price                 |

| Cart      | 4     | Add, add multiple, remove, cart page contents            |

| Checkout  | 5     | Full purchase flow, required-field validation, summary   |

| API       | 7     | GET, POST, PUT, DELETE, 404 handling, query filtering    |

| \*\*Total\*\* | \*\*26\*\* |                                                         |



\## Getting started



```bash

git clone https://github.com/agawa03/saucedemo-e2e.git

cd saucedemo-e2e

python -m venv venv

```



Activate the virtual environment:



```bash

\# Windows

venv\\Scripts\\activate



\# Mac / Linux

source venv/bin/activate

```



Install dependencies and the browser:



```bash

pip install pytest-playwright pytest-html ruff

playwright install chromium

```



\## Usage



```bash

python -m pytest                      # run everything, headless

python -m pytest --headed             # watch the browser

python -m pytest --browser firefox    # choose a browser

python -m pytest -m smoke             # 5 fast critical-path tests

python -m pytest -m regression        # 21 broader tests

ruff check . \&\& ruff format --check . # lint and formatting

```



\## Project structure



```text

pages/        Page objects (login, inventory, checkout)

tests/        UI and API tests

conftest.py   Shared fixtures

pytest.ini    Pytest config and markers

.github/      CI workflow

docs/         README images

```



\## Design decisions



\- \*\*Page Object Model:\*\* locators live in one place, so a UI change means one fix, not many.

\- \*\*Playwright:\*\* built-in auto-waiting reduces flaky tests, and tracing makes failures easy to debug.

\- \*\*Fixtures:\*\* setup (opening the page, logging in) is shared instead of copied into every test.

\- \*\*Markers:\*\* a fast smoke suite for quick feedback, a full regression suite for completeness.

\- \*\*CI matrix:\*\* the same suite runs on three browser engines to catch browser-specific issues.



\## Tech stack



Python, pytest, Playwright, pytest-html, ruff, GitHub Actions


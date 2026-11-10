\# SauceDemo E2E Test Suite



!\[tests](https://github.com/agawa03/saucedemo-e2e/actions/workflows/tests.yml/badge.svg)



End-to-end UI and API tests for \[saucedemo.com](https://www.saucedemo.com), built with Python, pytest, and Playwright.



\*\*Live test reports:\*\* https://agawa03.github.io/saucedemo-e2e/



!\[Test report](docs/report.png)



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



\## Tech stack



Python, pytest, Playwright, pytest-html, ruff, GitHub Actions



\## Project structure



```

pages/        Page objects (login, inventory, checkout)

tests/        UI and API tests

conftest.py   Shared fixtures

pytest.ini    Pytest config and markers

.github/      CI workflow

```



\## Setup



```

git clone https://github.com/agawa03/saucedemo-e2e.git

cd saucedemo-e2e

python -m venv venv

venv\\Scripts\\activate

pip install pytest-playwright pytest-html ruff

playwright install chromium

```



On Mac/Linux, activate with `source venv/bin/activate` instead.



\## Run the tests



```

python -m pytest

python -m pytest --headed

python -m pytest --browser firefox

```



\## Test markers



```

python -m pytest -m smoke

python -m pytest -m regression

```



\## Lint



```

ruff check .

ruff format --check .

```



\## Test coverage



| Area      | Tests                                                          |

|-----------|----------------------------------------------------------------|

| Login     | Valid login, locked-out user, 3 invalid credential cases       |

| Inventory | Product count, sorting by name and price                       |

| Cart      | Add, add multiple, remove, cart page contents                  |

| Checkout  | Full purchase flow, required-field validation, order summary   |

| API       | GET, POST, PUT, DELETE, 404 handling, query filtering          |



26 tests in total.



\## Design decisions



\- \*\*Page Object Model:\*\* locators live in one place, so a UI change means one fix, not many.

\- \*\*Playwright:\*\* built-in auto-waiting reduces flaky tests, and tracing makes failures easy to debug.

\- \*\*Fixtures:\*\* setup (opening the page, logging in) is shared instead of copied into every test.

\- \*\*Markers:\*\* a fast smoke suite for quick feedback, a full regression suite for completeness.

\- \*\*CI matrix:\*\* the same suite runs on three browser engines to catch browser-specific issues.


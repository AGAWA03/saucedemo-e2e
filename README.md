\# SauceDemo E2E Test Suite



!\[tests](https://github.com/agawa03/saucedemo-e2e/actions/workflows/tests.yml/badge.svg)



End-to-end UI tests for \[saucedemo.com](https://www.saucedemo.com), built with Python, pytest, and Playwright.



\## Features



\- Page Object Model for maintainable locators and actions

\- Reusable pytest fixtures (`login\_page`, `logged\_in`)

\- Parametrized login tests covering invalid credentials

\- Traces and screenshots captured automatically on failure

\- CI on GitHub Actions



\## Tech stack



Python, pytest, Playwright



\## Setup



```

git clone https://github.com/agawa03/saucedemo-e2e.git

cd saucedemo-e2e

python -m venv venv

venv\\Scripts\\activate

pip install pytest-playwright

playwright install chromium

```



On Mac/Linux, activate with `source venv/bin/activate` instead.



\## Run the tests



```

python -m pytest

python -m pytest --headed

```



The first command runs headless. The second opens a visible browser.



\## Test coverage



| Area  | Tests                                                    |

|-------|----------------------------------------------------------|

| Login | Valid login, locked-out user, 3 invalid credential cases |

| Cart  | Adding an item updates the cart badge                    |



\## Design decisions



\- \*\*Page Object Model:\*\* locators live in one place, so a UI change means one fix, not many.

\- \*\*Playwright:\*\* built-in auto-waiting reduces flaky tests, and tracing makes failures easy to debug.

\- \*\*Fixtures:\*\* setup (opening the page, logging in) is shared instead of copied into every test.


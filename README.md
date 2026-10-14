# password-app

A strong password generator, used to show what happens *around* the code: documentation generated from docstrings, CI/CD with GitHub Actions, a small web app with Streamlit, and a license.

## Install and run

You need [`uv`](https://docs.astral.sh/uv/). In a terminal (WSL / Mac Terminal / Linux / Git Bash):

```bash
git clone https://github.com/KnuxV/password-app.git
cd password-app
uv sync
uv run strong_password.py     # one memorable password
uv run strength.py            # memorable vs random, with the crack time
uv run pytest                 # the tests, and the examples in the docstrings
```

## Files

- `strong_password.py` — the generator (memorable words or random characters)
- `strength.py` — how strong is a password, with the `zxcvbn` library
- `tests/` — pytest suite
- `data/eff_large_wordlist.txt` — the EFF long wordlist (7776 words)

## Documentation from the docstrings

```bash
uv run pdoc -d google strong_password.py strength.py            # opens the docs in your browser
uv run pdoc -d google strong_password.py strength.py -o site    # writes them as HTML files in site/
```

## CI/CD

`.github/workflows/ci.yml` runs on every push to `main`: **test** → **docs** → **deploy**. If a test fails, the docs are not rebuilt and the site keeps its last good version.

The docs are online at <https://knuxv.github.io/password-app/>. On your own copy, turn it on once: **Settings → Pages → Source: GitHub Actions**.

## The web app

```bash
uv run streamlit run app.py
```

Your browser opens <http://localhost:8501>. Stop the app with `Ctrl+C` in the terminal. `tests/test_app.py` tests the app without a browser, with Streamlit's `AppTest`.

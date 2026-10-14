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

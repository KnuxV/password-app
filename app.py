"""The password generator as a web page, with Streamlit.

```bash
uv run streamlit run app.py
```

Streamlit runs this whole script from top to bottom, and runs it again
every time the user touches a widget.
"""

import streamlit as st

from strength import check_strength
from strong_password import StrongPassword, TypePassword

st.title("Password generator")

# chaque widget rend sa valeur : une variable Python ordinaire
kind = st.radio("Kind", ["memorable", "random"], horizontal=True)
if kind == "memorable":
    length = st.slider("Number of words", min_value=3, max_value=10, value=5)
else:
    length = st.slider("Number of characters", min_value=8, max_value=40, value=16)

password = StrongPassword(length=length, type_p=TypePassword(kind)).generate()
st.code(password, language=None)  # le bloc de code a un bouton « copier »

strength = check_strength(password)
st.metric("Score", f"{strength.score} / 4")
st.write(f"Time to crack it: **{strength.crack_time}**")

# le bouton ne fait rien lui-même : cliquer relance le script, donc un nouveau mot de passe
st.button("Another one")

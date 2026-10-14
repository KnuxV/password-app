from streamlit.testing.v1 import AppTest


# AppTest lance app.py sans navigateur, et laisse lire et toucher les widgets
# (le chemin est relatif à ce fichier de test)
def test_app_shows_a_memorable_password() -> None:
    app = AppTest.from_file("../app.py").run()
    assert not app.exception
    assert len(app.code[0].value.split(" ")) == 5  # 5 mots par défaut


def test_switching_to_random_changes_the_slider() -> None:
    app = AppTest.from_file("../app.py").run()
    app.radio[0].set_value("random").run()
    assert app.slider[0].label == "Number of characters"
    assert len(app.code[0].value) == 16  # 16 caractères par défaut

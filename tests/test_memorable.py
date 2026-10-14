import pytest

from strong_password import StrongPassword, TypePassword, WORD_LIST


# cinq mots → quatre espaces
def test_five_words_four_spaces(memorable_password: str) -> None:
    assert memorable_password.count(" ") == 4


def test_every_word_is_from_the_list(memorable_password: str) -> None:
    assert all(word in WORD_LIST for word in memorable_password.split(" "))


@pytest.mark.parametrize("n_words", [1, 3, 8])
def test_word_count(n_words: int) -> None:
    password = StrongPassword(length=n_words, type_p=TypePassword.MEMORABLE).generate()
    assert len(password.split(" ")) == n_words


def test_wordlist_is_complete() -> None:
    # la liste EFF a 7776 mots : 6 × 6 × 6 × 6 × 6, cinq lancers de dé
    assert len(WORD_LIST) == 7776

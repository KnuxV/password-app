from strength import check_strength


def test_weak_password_scores_zero() -> None:
    assert check_strength("password").score == 0


# une phrase de cinq mots doit avoir la note maximale
def test_five_words_score_four(memorable_password: str) -> None:
    assert check_strength(memorable_password).score == 4

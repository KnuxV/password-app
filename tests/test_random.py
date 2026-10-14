from strong_password import SPECIAL, StrongPassword, TypePassword


def test_length(random_password: str) -> None:
    assert len(random_password) == 12


def test_has_every_kind_of_character(random_password: str) -> None:
    assert any(char.islower() for char in random_password)
    assert any(char.isupper() for char in random_password)
    assert any(char.isdigit() for char in random_password)
    assert any(char in SPECIAL for char in random_password)


def test_two_passwords_differ() -> None:
    generator = StrongPassword(length=16, type_p=TypePassword.RANDOM)
    assert generator.generate() != generator.generate()

import pytest

from strong_password import StrongPassword, TypePassword


# fixtures : un mot de passe neuf pour chaque test qui le demande
@pytest.fixture
def random_password() -> str:
    return StrongPassword(length=12, type_p=TypePassword.RANDOM).generate()


@pytest.fixture
def memorable_password() -> str:
    return StrongPassword(length=5, type_p=TypePassword.MEMORABLE).generate()

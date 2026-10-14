"""Strong password generator.

Two kinds of password:

- **memorable**: random words from the EFF long wordlist (`Stubbed Congress Tiptop`)
- **random**: mixed characters (`aB3$cD9#eF2@`)

Run it:

    uv run strong_password.py

Use it from Python:

>>> generator = StrongPassword(length=4, type_p=TypePassword.MEMORABLE)
>>> password = generator.generate()
>>> len(password.split(" "))
4
"""

import secrets
from enum import StrEnum, auto
from pathlib import Path

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?"
CHAR_SETS: list[str] = [LOWERCASE, UPPERCASE, DIGITS, SPECIAL]
"""The four kinds of character a random password mixes."""

# la liste de mots est à côté de ce fichier : le script marche depuis n'importe quel dossier
WORDLIST_FILE = Path(__file__).parent / "data" / "eff_large_wordlist.txt"
with open(WORDLIST_FILE, encoding="utf-8") as f:
    # chaque ligne est "11111<TAB>abacus" : on garde le mot, avec une majuscule
    WORD_LIST: list[str] = [line.split()[1].capitalize() for line in f]


class TypePassword(StrEnum):
    """The two kinds of password this tool can generate."""

    MEMORABLE = auto()
    """Words from the EFF wordlist: `Stubbed Congress Tiptop`."""
    RANDOM = auto()
    """Mixed characters: `aB3$cD9#eF2@`."""


class StrongPassword:
    """A password generator.

    Args:
        length: number of words (memorable) or characters (random).
        type_p: which kind of password to generate.

    Example:
        >>> StrongPassword(length=3, type_p=TypePassword.MEMORABLE).length
        3
    """

    def __init__(self, length: int, type_p: TypePassword) -> None:
        self.length = length
        self.type_p = type_p

    def generate(self) -> str:
        """Generate a password of the configured type.

        Raises:
            ValueError: if `type_p` is not a known `TypePassword`.
        """
        match self.type_p:
            case TypePassword.MEMORABLE:
                return self.generate_memorable()
            case TypePassword.RANDOM:
                return self.generate_random()
            case _:
                raise ValueError(f"Unknown password type: {self.type_p}")

    def generate_memorable(self) -> str:
        """Pick `length` words from the EFF wordlist (7776 words), capitalised,
        separated by spaces.

        Example:
            >>> password = StrongPassword(3, TypePassword.MEMORABLE).generate_memorable()
            >>> password.count(" ")
            2
        """
        words = [secrets.choice(WORD_LIST) for _ in range(self.length)]
        return " ".join(words)

    def generate_random(self) -> str:
        """Build `length` characters, cycling through the four character sets
        so that each kind is present when `length >= 4`, then shuffle.

        Example:
            >>> password = StrongPassword(16, TypePassword.RANDOM).generate_random()
            >>> len(password)
            16
            >>> any(char.isdigit() for char in password)
            True
        """
        # i % 4 : minuscule, majuscule, chiffre, spécial, minuscule, ...
        password = [secrets.choice(CHAR_SETS[i % 4]) for i in range(self.length)]
        secrets.SystemRandom().shuffle(password)
        return "".join(password)


def main() -> None:
    """Print one memorable password of five words."""
    generator = StrongPassword(length=5, type_p=TypePassword.MEMORABLE)
    print(generator.generate())


if __name__ == "__main__":
    main()

"""How strong is a password? A thin wrapper around `zxcvbn`.

`zxcvbn` is a strength estimator: it looks for words, dates, keyboard patterns
and repeats, and estimates how long an attacker would need to guess the password.

Run it to compare a memorable and a random password:

```bash
uv run strength.py
```
"""

from dataclasses import dataclass

from zxcvbn import zxcvbn

from strong_password import StrongPassword, TypePassword


@dataclass
class Strength:
    """The verdict on one password."""

    score: int
    """From 0 (guessed at once) to 4 (very strong)."""
    crack_time: str
    """Estimated time to crack it offline, in words: `"centuries"`."""


def check_strength(password: str) -> Strength:
    """Score a password with `zxcvbn`.

    Args:
        password: the password to judge.

    Returns:
        Its score (0 to 4) and an estimated crack time.

    Example:
        >>> check_strength("password").score
        0
        >>> check_strength("Stubbed Congress Tiptop Playmate Stagnate").crack_time
        'centuries'
    """
    results = zxcvbn(password)
    # le scénario le plus réaliste : un fichier de mots de passe volé, haché lentement
    crack_time = results["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    return Strength(score=results["score"], crack_time=crack_time)


def main() -> None:
    """Compare a memorable and a random password."""
    for label, generator in [
        ("Memorable, 4 words", StrongPassword(4, TypePassword.MEMORABLE)),
        ("Random, 12 characters", StrongPassword(12, TypePassword.RANDOM)),
    ]:
        password = generator.generate()
        strength = check_strength(password)
        print(f"\n{label}")
        print(f"  password:   {password}")
        print(f"  score:      {strength.score}/4")
        print(f"  crack time: {strength.crack_time}")


if __name__ == "__main__":
    main()

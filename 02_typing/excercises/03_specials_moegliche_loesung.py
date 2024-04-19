# pyright: strict
"""
Aufgabe 1: Type Hints zu "mixed_merge" hinzufügen und mit "mypy --strict 03_specials.py" bzw. "pyright 03_specials.py" überprüfen.

Aufgabe 2: Mindestens drei Beispielaufrufe von "mixed_merge" hinzufügen und ggf. Type Hints anpassen.

Aufgabe 3: Type Hints zu "read_encrypted_file" hinzufügen und mit "mypy --strict 03_specials.py" bzw. "pyright 03_specials.py" überprüfen.

Aufgabe 4: Mindestens je einen Beispielaufruf von "read_encrypted_file" mit und ohne "passphrase" hinzufügen.

Aufgabe 5: Type Hints zu "read_any_file" hinzufügen und mit "mypy --strict 03_specials.py" bzw. "pyright 03_specials.py" überprüfen.

"""

import pathlib
from typing import Any, Literal


def mixed_merge(*args: str | int | float | list[Any] | tuple[Any, ...]) -> str:
    return "".join(map(str, args))


mixed_merge("a", "b", 1, 2)
mixed_merge("a", "b", 1.0, 2.0)
mixed_merge("a", "b", [1, 2], (3, 4))


def read_encrypted_file(file: str | pathlib.Path, passphrase: str | None = None) -> str:
    with open(file, "rt") as f:
        content = f.read()
        if passphrase is not None:
            ...
    return content


read_encrypted_file("03_specials.py")
read_encrypted_file(pathlib.Path(__file__).parent / "03_specials.py", "secret")


def read_any_file(
    file: str | pathlib.Path, mode: Literal["r", "rt", "rb"] = "r"
) -> Any:
    with open(file, mode) as f:
        return f.read()

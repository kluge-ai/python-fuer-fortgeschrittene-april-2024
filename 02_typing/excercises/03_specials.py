# pyright: strict
"""
Aufgabe 1: Type Hints zu "mixed_merge" hinzufügen und mit "mypy --strict 03_specials.py" bzw. "pyright 03_specials.py" überprüfen.

Aufgabe 2: Mindestens drei Beispielaufrufe von "mixed_merge" hinzufügen und ggf. Type Hints anpassen.

Aufgabe 3: Type Hints zu "read_encrypted_file" hinzufügen und mit "mypy --strict 03_specials.py" bzw. "pyright 03_specials.py" überprüfen.

Aufgabe 4: Mindestens je einen Beispielaufruf von "read_encrypted_file" mit und ohne "passphrase" hinzufügen.

Aufgabe 5: Type Hints zu "read_any_file" hinzufügen und mit "mypy --strict 03_specials.py" bzw. "pyright 03_specials.py" überprüfen.

"""

def mixed_merge(*args):
    return "".join(map(str, args))


mixed_merge("a", "b", 1, 2)


def read_encrypted_file(file, passphrase=None):
    with open(file) as f:
        content = f.read()
        if passphrase is not None:
            ...
    return content


def read_any_file(file, mode="r"):
    with open(file, mode) as f:
        return f.read()


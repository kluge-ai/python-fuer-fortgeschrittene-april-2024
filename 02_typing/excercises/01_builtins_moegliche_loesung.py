# pyright: strict
"""
Aufgabe 1: Type Hints hinzufügen und mit "mypy --strict 01_builtins.py" bzw. "pyright 01_builtins.py" überprüfen.

Aufgabe 2: Jeweils mindestens zwei Funktionsaufrufe hinzufügen, die die Typen der Argumente erfüllen.

Aufgabe 3: Jeweils mindestens einen Funktionsaufruf hinzufügen, die die Typen der Argumente nicht erfüllen.
"""


def first_binomial(a: float, b: float) -> float:
    return a**2 + 2 * a * b + b**2


first_binomial(1.0, 2.0)
first_binomial(3.0, 4)
# first_binomial("1", "2")
first_binomial(1.0j, 4 + 2.0j)


def faculty(n: int) -> int:
    if n == 0:
        return 1
    return n * faculty(n - 1)


faculty(0)
faculty(1)
# faculty("1")
faculty(1.0)


def is_even(n: int) -> bool:
    return n % 2 == 0


is_even(2)
is_even(3)
# is_even("2")
is_even(2.0)


def lowercase(text: str) -> str:
    return text.lower()


lowercase("Hello")
lowercase("World")
# lowercase(1)
# lowercase([1.0, 5.0])


def concatenate(*words: str) -> str:
    return " ".join(words)


concatenate("Hello", "World")
concatenate("1", "+", "1", "=", "2")
concatenate(1, "is", "not", "a", "string")
concatenate(1, 2, [3, 4], 5.0, (6, 7, 8))

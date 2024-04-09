# pyright: strict
"""
Aufgabe 1: Type Hints hinzufügen und mit "mypy --strict 01_builtins.py" bzw. "pyright 01_builtins.py" überprüfen.

Aufgabe 2: Jeweils mindestens zwei Funktionsaufrufe hinzufügen, die die Typen der Argumente erfüllen.

Aufgabe 3: Jeweils mindestens einen Funktionsaufruf hinzufügen, die die Typen der Argumente nicht erfüllen.
"""


def first_binomial(a, b):
    return a**2 + 2*a*b + b**2


def faculty(n):
    if n == 0:
        return 1
    return n * faculty(n - 1)


def is_even(n):
    return n % 2 == 0


def lowercase(text):
    return text.lower()


def concatenate(*words):
    return " ".join(words)


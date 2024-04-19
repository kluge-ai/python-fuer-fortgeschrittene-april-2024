# pyright: strict
import math

"""
Bei allen Aufgaben Typen mit "mypy --strict 01_builtins.py" bzw. "pyright 01_builtins.py" überprüfen.

Aufgabe 1: Type Hints zun den Klassen "Shape", "Circle" und "Square" hinzufügen.

Aufgabe 2: Mindestens zwei Aufrufe der Funktionen "total_area" und "total_covered_area" hinzufügen.

Aufgabe 3: Type Hints zu den Funktionen "total_area" und "total_covered_area" hinzufügen.

Aufgabe 4: Type Hints zu der Klasse "SimpleSquare" hinzufügen.

Aufgabe 5: Was passiert, wenn wir den Rückgabetyp von "area" und "circumference" in "Shape" auf "int" ändern?
"""


class Shape:
    def area(self) -> float: ...

    def circumference(self) -> float: ...

    def circumscribed_square(self) -> "Square": ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

    def circumscribed_square(self) -> "Square":
        return Square(2 * self.radius)


class Square(Shape):
    def __init__(self, side_length: float) -> None:
        self.side_length = side_length

    def area(self) -> float:
        return self.side_length**2

    def circumference(self) -> float:
        return 4 * self.side_length

    def circumscribed_square(self) -> "Square":
        return Square(self.side_length)


def total_area(shape1: Shape, shape2: Shape) -> float:
    return shape1.area() + shape2.area()


def total_covered_area(shape1: Shape, shape2: Shape) -> float:
    return shape1.circumscribed_square().area() + shape2.circumscribed_square().area()


class SimpleSquare(Square):
    def __init__(self, side_length: int) -> None:
        super().__init__(side_length)
        self.side_length: int = side_length

    def area(self) -> int:
        return self.side_length**2

    def circumference(self) -> int:
        return 4 * self.side_length

    def circumscribed_square(self) -> "Square":
        return Square(self.side_length)

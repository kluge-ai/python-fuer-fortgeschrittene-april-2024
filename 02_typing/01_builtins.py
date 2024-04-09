

def square(a: int) -> float:
    return a**2

# print(square("abc"))
print(square(12))
print(square(23.23))

squared_2 = square(2)
square(squared_2)


def example(name: str, **kwargs):
    print("kwargs", kwargs)
    a = kwargs["language"]**2

example(name="kilian", language=2, role="speaker")

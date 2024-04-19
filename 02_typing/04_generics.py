import typing

list_of_numbers: list[float] = [1, 2, 3, 4.0]

list_of_numbers.append(1)
list_of_numbers.append(4.5)
# list_of_numbers.append("4.5")


dictionary_with_string_keys: dict[str, typing.Any] = {"a": 1, "b": typing}


class MyContainer[T]:
    def __init__(self, content: T):
        self.content = content

    def get_value(self) -> T:
        return self.content


string_container = MyContainer(content="7")


V = typing.TypeVar("V")


class MyOldContainer(typing.Generic[V]):
    def __init__(self, content: V):
        self.content = content


old_string_container: MyOldContainer[str] = MyOldContainer(content="7")


def double[U: float](number: U) -> U | float:
    return number * 2

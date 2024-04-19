import typing


class MyContainer:
    def __init__(self, content: str) -> None:
        self.content = content

    def empty(self) -> None:
        self.content = ""

    def is_empty(self) -> bool:
        return self.content is None

    @classmethod
    def new(cls) -> "MyContainer":
        return cls("")

    def myself(self) -> typing.Self:
        return self


class LimitedContainer(MyContainer):
    def __init__(self, content: str) -> None:
        super().__init__(content[:6])


class NumberStore:
    def __init__(self, top: int, bottom: int) -> None:
        self.number = top + bottom

    def empty(self) -> None:
        self.number = 0

    def is_empty(self) -> bool:
        return self.number > 0


class CanBeEmptied(typing.Protocol):
    def is_empty(self) -> bool: ...

    def empty(self) -> None: ...


def empty_container(container: CanBeEmptied):
    if not container.is_empty():
        container.empty()


c = MyContainer("bla bla bla")
empty_container(c)

l = LimitedContainer("bla bla bla")
empty_container(l)

o = NumberStore(1, 2)
empty_container(o)

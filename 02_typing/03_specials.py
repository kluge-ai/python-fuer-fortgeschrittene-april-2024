import typing
import pathlib


def read_a_file(fname: str, folder: str | None | pathlib.Path = None):
    if folder is None:
        ...
    else:
        ...


def take_all(anything: typing.Any) -> str:
    ...


def round_a_number(number: float, direction: typing.Literal["up", "down", 1, -1]):
    ...


round_a_number(12.3, "up")
round_a_number(12.3, "down")

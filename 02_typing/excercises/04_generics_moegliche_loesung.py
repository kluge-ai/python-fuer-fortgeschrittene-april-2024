# pyright: strict
"""
Aufgabe: Type Hints hinzufügen und mit "mypy --strict 04_generics.py" bzw. "pyright 04_generics.py" überprüfen.
"""

from typing import Any, Hashable, Iterable, Mapping


def lookup(data: dict[Hashable, Any], key: Hashable) -> Any:
    try:
        return data[key]
    except KeyError:
        return None


lookup({"a": 1, "b": 2}, "a")
lookup({"a": 1, "b": 2}, "c")


example_post = {"title": "Hello, World!", "content": "This is my first post."}


def render(post: Mapping[str, str]) -> str:
    return f"""== {post["title"]} ==
{post["content"]}"""


def make_a_book(posts: Iterable[dict[str, str]]) -> str:
    return "\n\n".join(map(render, posts))

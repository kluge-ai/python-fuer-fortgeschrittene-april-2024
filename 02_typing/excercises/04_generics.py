# pyright: strict
"""
Aufgabe: Type Hints hinzufügen und mit "mypy --strict 04_generics.py" bzw. "pyright 04_generics.py" überprüfen.
"""

def lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return None


lookup({"a": 1, "b": 2}, "a")
lookup({"a": 1, "b": 2}, "c")


example_post = {"title": "Hello, World!", "content": "This is my first post."}


def render(post):
    return f"""== {post["title"]} ==
{post["content"]}"""


def make_a_book(posts):
    return "\n\n".join(map(render, posts))


from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from quail.parser.quail_test_parser import QuailTestParser

import re
from functools import wraps


def get_first_indent(lines: list[str]):
    for line in lines:
        if line.lstrip() and line != line.lstrip():
            return get_indent(line)
    return " " * 4


def get_indent(line: str):
    return line[: line.index(line.strip()[0])]


def apply_indent(indent: str, lines: str | list[str]):
    lines = lines if isinstance(lines, list) else lines.split("\n")
    return "\n".join(indent + line for line in lines) + "\n"


def __indented(func):
    @wraps(func)
    def inner(match: re.Match, test: QuailTestParser):
        indent = get_indent(match.group(1))
        line = func(match, test)
        return apply_indent(indent, line)

    return inner

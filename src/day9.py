"""Day 9: Stream Processing."""

import pytest


def day9(arg, p2=False):
    """Day 9."""
    i = 0
    groups = 0
    max_groups = 0
    garbage = False
    garbage_chars = 0
    while i < len(arg):
        if arg[i] == "!" and garbage:
            i += 2
            continue
        if arg[i] == "<" and not garbage:
            garbage = True
            i += 1
            continue
        if arg[i] == ">":
            garbage = False
        if arg[i] == "{" and not garbage:
            groups += 1
        if arg[i] == "}" and not garbage:
            max_groups += groups
            groups -= 1
        if garbage and arg[i] not in ('>', '!'):
            garbage_chars += 1
        i += 1
    return max_groups if not p2 else garbage_chars


def day9p2(arg):
    """Day 9 part 2."""
    return day9(arg, True)


@pytest.mark.parametrize('data,result', [
    (r"{}", 1),
    (r"{{{}}}", 6),
    (r"{{},{}}", 5),
    (r"{{{},{},{{}}}}", 16),
    (r"{<a>,<a>,<a>,<a>}", 1),
    (r"{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
    (r"{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
    (r"{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)
])
def test_day9(data, result):
    """Test day9."""
    assert day9(data) == result


@pytest.mark.parametrize('data,result', [
    (r"<>", 0),
    (r"<random characters>", 17),
    (r"<<<<>", 3),
    (r"<{!>}>", 2),
    (r"<!!>", 0),
    (r"<!!!>>", 0),
    (r'<{o"i!a,<{i<a>', 10)
])
def test_day9p2(data, result):
    """Test day9 part 2."""
    assert day9p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day9(arg))
        print(day9p2(arg))

"""Day 2: Corruption Checksum."""

import pytest


def sum_divisible(row):
    """Sum up all divisible numbers in a row."""
    result = 0
    values = list(map(int, row.split()))
    for i, r in enumerate(values):
        for j, s in enumerate(values[i + 1:]):
            big, small = max(r, s), min(r, s)
            if big % small == 0:
                result += big / small
    return result


def sum_min_max(row):
    """Sum min and max in a line."""
    values = list(map(int, row.split()))
    return max(values) - min(values)


def day2(arg):
    """Day 2."""
    return sum(sum_min_max(line) for line in arg.splitlines())


def day2p2(arg):
    """Day 2 part 2."""
    return sum(sum_divisible(line) for line in arg.splitlines())


@pytest.mark.parametrize('test_input,expected', [
    ("5 9 2 8", 4),
    ("9 4 7 3", 3),
    ("3 8 6 5", 2),
    ("3 8 6 5 10", 4),
])
def test_divisible(test_input, expected):
    """Test divisible."""
    assert sum_divisible(test_input) == expected, \
        "Input {} produced {} instead of {}.".format(
        test_input,
        sum_divisible(test_input),
        expected
    )


@pytest.mark.parametrize('test_input,expected', [
    ("5 1 9 5", 8),
    ("7 5 3", 4),
    ("2 4 6 8", 6),
])
def test_row(test_input, expected):
    """Test sum of min and max."""
    assert sum_min_max(test_input) == expected, \
        "Input {} produced {} instead of {}.".format(
        test_input,
        sum_min_max(test_input),
        expected
    )


def test_day2():
    """Test day2."""
    sheet = """5 1 9 5
7 5 3
2 4 6 8"""
    assert day2(sheet) == 18


def test_day2p2():
    """Test day2 part 2."""
    sheet = """5 9 2 8
9 4 7 3
3 8 6 5"""
    assert day2p2(sheet) == 9


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day2(arg))
        print(day2p2(arg))

"""Day 1: Inverse Captcha."""

import pytest


def day1(arg):
    """Day 1."""
    arg = arg + arg[0]
    result = sum(int(a) for i, a in enumerate(arg[:-1]) if a == arg[i + 1])
    return str(result)


def day1p2(arg):
    """Day 1 part 2."""
    arg = arg + arg
    result = sum(int(a) for i, a in enumerate(arg[:int(len(arg) / 2)])
                 if a == arg[i + int(len(arg) / 4)])
    return str(result)


@pytest.mark.parametrize('case', [
    "1122 3",
    "1111 4",
    "1234 0",
    "91212129 9",
    "1123345561 10",
    "12312341234 0"
])
def test_day1(case):
    """Test day1."""
    arg, res = case.split(' ')
    assert day1(arg) == res, "Input {} produced {} instead of {}.".format(
        arg,
        day1(arg),
        res
    )


@pytest.mark.parametrize('case', [
    "1212 6",
    "1221 0",
    "123425 4",
    "123123 12",
    "12131415 4"
])
def test_day1p2(case):
    """Test day1 part 2."""
    arg, res = case.split(' ')
    assert day1p2(arg) == res, "Input {} produced {} instead of {}.".format(
        arg,
        day1(arg),
        res
    )


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day1(arg))
        print(day1p2(arg))

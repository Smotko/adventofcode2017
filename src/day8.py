"""Day 8: ???."""

import pytest

from collections import defaultdict


def _greater(a, b):
    return a > b


def _lesser(a, b):
    return a < b


def _greatereq(a, b):
    return a >= b


def _lessereq(a, b):
    return a <= b


def _noteq(a, b):
    return a != b


def _eq(a, b):
    return a == b


def day8(arg, p2=False):
    """Day 8."""
    registers = defaultdict(int)
    cmps = {
        ">": _greater,
        "<": _lesser,
        ">=": _greatereq,
        "<=": _lessereq,
        "!=": _noteq,
        "==": _eq
    }
    ops = {
        "inc": 1,
        "dec": -1
    }
    mx = 0
    for line in arg.split('\n'):
        register, op, amount, _, register2, cmp, val = line.split()
        if cmps[cmp](registers[register2], int(val)):
            registers[register] += int(amount) * ops[op]
        mx = max(mx, registers[register])
    if p2:
        return mx
    return max(registers.values())


def day8p2(arg):
    """Day 8 part 2."""
    return day8(arg, True)


@pytest.mark.parametrize('data,result', [
    ("""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""", 1),
])
def test_day8(data, result):
    """Test day8."""
    assert day8(data) == result


@pytest.mark.parametrize('data,result', [
    ("""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""", 10),

])
def test_day8p2(data, result):
    """Test day8 part 2."""
    assert day8p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day8(arg))
        print(day8p2(arg))

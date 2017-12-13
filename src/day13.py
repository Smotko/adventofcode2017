"""Day 13: ???."""

import pytest
from collections import defaultdict


def check(fws, delay=0, hit=False):
    """Use to check and do sums."""
    sums = 0
    for i in range(max(fws.keys()) + 1):
        if fws[i] == 0:
            continue
        all_pos = (fws[i] - 1) * 2
        if (delay + i) % all_pos == 0:
            sums += i * fws[i]
            if hit:
                return False
    return sums if not hit else True


def day13(arg):
    """Day 13."""
    fws = defaultdict(int)
    for line in arg.split("\n"):
        index, length = map(int, line.split(": "))
        fws[index] = length
    return check(fws)


def day13p2(arg):
    """Day 13 part 2."""
    fws = defaultdict(int)
    for line in arg.split("\n"):
        index, length = map(int, line.split(": "))
        fws[index] = length
    i = 0
    while True:
        if check(fws, i, True):
            return i
        i += 1


@pytest.mark.parametrize('data,result', [
    ("""0: 3
1: 2
4: 4
6: 4""", 24),
])
def test_day13(data, result):
    """Test day13."""
    assert day13(data) == result


@pytest.mark.parametrize('data,result', [
    ("""0: 3
1: 2
4: 4
6: 4""", 10),

])
def test_day13p2(data, result):
    """Test day13 part 2."""
    assert day13p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day13(arg))
        print(day13p2(arg))

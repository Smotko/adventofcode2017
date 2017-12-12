"""Day 11: Hex Ed."""

import pytest


distances = {
    # (x, y , z)
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0)
}


def day11(arg, max_distance=False):
    """Day 11."""
    steps = arg.split(',')
    pos = [0, 0, 0]
    max_dist = 0
    for step in steps:
        for i, v in enumerate(pos):
            pos[i] = v + distances[step][i]
        max_dist = max(max_dist, max(abs(pos[0]), abs(pos[1]), abs(pos[2])))
    dist = max(abs(pos[0]), abs(pos[1]), abs(pos[2]))
    return max_dist if max_distance else dist


def day11p2(arg):
    """Day 11 part 2."""
    return day11(arg, True)


@pytest.mark.parametrize('data,result', [
    ("ne,ne,ne", 3),
    ("ne,ne,sw,sw", 0),
    ("ne,ne,s,s", 2),
    ("se,sw,se,sw,sw", 3),
])
def test_day11(data, result):
    """Test day11."""
    assert day11(data) == result


@pytest.mark.parametrize('data,result', [
    ("ne,ne,ne", 3),
    ("ne,ne,sw,sw", 2),
    ("ne,ne,s,s", 2),
    ("se,sw,se,sw,sw", 3),
])
def test_day11p2(data, result):
    """Test day11 part 2."""
    assert day11p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day11(arg))
        print(day11p2(arg))

"""Day 5: A Maze of Twisty Trampolines, All Alike."""

import pytest


def day5(arg, is_pt2=False):
    """Day 5."""
    instructions = list(map(int, arg.split()))
    current = 0
    steps = 0
    while current < len(instructions):
        offset = instructions[current]
        if offset >= 3 and is_pt2:
            instructions[current] -= 1
        else:
            instructions[current] += 1
        current += offset
        steps += 1
    return steps


def day5p2(arg):
    """Day 5 part 2."""
    return day5(arg, True)


@pytest.mark.parametrize('data,result', [
    ("""0
3
0
1
-3""", 5),
])
def test_day5(data, result):
    """Test day5."""
    assert day5(data) == result


@pytest.mark.parametrize('data,result', [
    ("""0
3
0
1
-3""", 10),
])
def test_day5p2(data, result):
    """Test day5 part 2."""
    assert day5p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day5(arg))
        print(day5p2(arg))

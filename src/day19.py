"""Day 19: ???."""

import pytest


def day19(arg, p2=False):
    """Day 19."""
    args = arg.split("\n")
    args.insert(0, ' ' * len(args[0]))
    args.append(' ' * len(args[0]))
    arr = [[c for c in (' ' + line + ' ')] for line in args]
    start = (0, 0)
    for i in range(len(arr[1])):
        if arr[1][i] == '|':
            start = (1, i)
    seen = []
    current = start
    prev = (0, 0)
    vertical = ((1, 0), (-1, 0))
    horizontal = ((0, 1), (0, -1))
    direction = vertical
    steps = 0
    while True:
        x, y = current
        if arr[x][y].isalpha():
            seen.append(arr[x][y])
        elif arr[x][y] == '+':
            if direction == vertical:
                direction = horizontal
            else:
                direction = vertical
        for dx, dy in direction:
            if arr[x + dx][y + dy].strip() != '' and (x + dx, y + dy) != prev:
                current = (x + dx, y + dy)
                prev = (x, y)
                break
        steps += 1
        if (x, y) == current:
            break
    if p2:
        return steps
    return ''.join(seen)


def day19p2(arg):
    """Day 19 part 2."""
    return day19(arg, True)


@pytest.mark.parametrize('data,result', [
    (
        "     |          \n"
        "     |  +--+    \n"
        "     A  |  C    \n"
        " F---|----E|--+ \n"
        "     |  |  |  D \n"
        "     +B-+  +--+ ", "ABCDEF"),
])
def test_day19(data, result):
    """Test day19."""
    assert day19(data) == result


@pytest.mark.parametrize('data,result', [
    (
        "     |          \n"
        "     |  +--+    \n"
        "     A  |  C    \n"
        " F---|----E|--+ \n"
        "     |  |  |  D \n"
        "     +B-+  +--+ ", 38),

])
def test_day19p2(data, result):
    """Test day19 part 2."""
    assert day19p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read()
        print(day19(arg))
        print(day19p2(arg))

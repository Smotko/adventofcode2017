"""Day 6: ???."""

import pytest


def redistribute(arg):
    """Redistribute memory."""
    arg = list(map(int, arg.split()))
    max_element = max(arg)
    max_index = arg.index(max_element)
    arg[max_index] = 0
    while max_element > 0:
        max_index += 1
        max_index %= len(arg)
        arg[max_index] += 1
        max_element -= 1
    return " ".join(map(str, arg))


def day6(arg, p2=False):
    """Day 6."""
    seen = set()
    seen_index = []
    count = 0
    while arg not in seen:
        seen.add(arg)
        seen_index.append(arg)
        arg = redistribute(arg)
        count += 1
    if p2:
        return count - seen_index.index(arg)
    else:
        return count


def day6p2(arg):
    """Day 6 part 2."""
    return day6(arg, True)


@pytest.mark.parametrize('data,result', [
    ("0 2 7 0", "2 4 1 2"),
    ("2 4 1 2", "3 1 2 3"),
    ("3 1 2 3", "0 2 3 4"),
    ("0 2 3 4", "1 3 4 1")
])
def test_redistribute(data, result):
    """Test day6."""
    print("aa")
    assert redistribute(data) == result


@pytest.mark.parametrize('data,result', [
    ("0 2 7 0", 5),
])
def test_day6(data, result):
    """Test day6."""
    assert day6(data) == result


@pytest.mark.parametrize('data,result', [
    ("0 2 7 0", 4),
])
def test_day6p2(data, result):
    """Test day6 part 2."""
    assert day6p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day6(arg))
        print(day6p2(arg))

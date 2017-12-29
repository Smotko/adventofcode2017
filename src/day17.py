"""Day 17: ???."""

import pytest
from blist import blist


def day17(iterations=3):
    """Day 17."""
    lst = blist([0])
    indx = 0
    lst_insert = 0
    for i in range(1, 2018):
        indx += 1
        indx %= len(lst)
        lst.insert(indx + 1, i)
        lst_insert = indx + 1
        indx += iterations
    return lst[lst_insert + 1]


def day17p2(iterations=3):
    """Day 17 part 2."""
    lst = blist([0])
    indx = 0
    for i in range(1, 50000001):
        indx += 1
        indx %= len(lst)
        lst.insert(indx + 1, i)
        indx += iterations
        if i % 100000 == 0:
            print(i)
    indexxx = lst.index(0)
    print(lst[indexxx - 5:indexxx + 5])
    return lst[lst.index(0) + 1]


@pytest.mark.parametrize('data,result', [
    (3, 638),
])
def test_day17(data, result):
    """Test day17."""
    assert day17(data) == result


@pytest.mark.skip(reason="Too long 😢")
@pytest.mark.parametrize('data,result', [
    (1, None),
])
def test_day17p2(data, result):
    """Test day17 part 2."""
    assert day17p2(data) == result


if __name__ == "__main__":
    print(day17(359))
    print(day17p2(359))

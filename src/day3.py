"""Day 3: Spiral Memory."""

from collections import defaultdict
import pytest


def day3(arg):
    """Day 3."""
    size = 1
    while size ** 2 < arg:
        size += 2
    current_value = size ** 2
    square = size - 1
    if (current_value == arg):
        return square
    offset = 0
    while current_value != arg:
        offset += 1
        current_value -= 1
    step_reduction = offset % square
    if step_reduction > square / 2:
        step_reduction = square - step_reduction
    return square - step_reduction


def sum_neighbours(coordinates, i, j):
    """Sum up all neighbours around i, j of coordinates."""
    return sum(coordinates[(i + sti, j + stj)]
               for stj in range(-1, 2)
               for sti in range(-1, 2))


def day3p2(arg):
    """Day 3 part 2."""
    if arg == 1:
        return 1
    size = 1
    i, j = (0, 1)
    coordinates = defaultdict(int)
    coordinates[(0, 0)] = 1
    while True:
        # Go up the spiral
        while i < size:
            coordinates[(i, j)] = curr = sum_neighbours(coordinates, i, j)
            i += 1
            if curr > arg:
                return curr
        # Go left to the end of the spiral
        while j > -size:
            coordinates[(i, j)] = curr = sum_neighbours(coordinates, i, j)
            j -= 1
            if curr > arg:
                return curr
        # Go down the spiral
        while i > -size:
            coordinates[(i, j)] = curr = sum_neighbours(coordinates, i, j)
            i -= 1
            if curr > arg:
                return curr
        # Go right the spiral
        while j <= size:
            coordinates[(i, j)] = curr = sum_neighbours(coordinates, i, j)
            j += 1
            if curr > arg:
                return curr
        size += 1


@pytest.mark.parametrize('data,steps', [
    (1, 0),
    (2, 1),
    (9, 2),
    (12, 3),
    (22, 3),
    (23, 2),
    (24, 3),
    (25, 4),
    (49, 6),
    (1024, 31),
])
def test_day3(data, steps):
    """Test day3."""
    assert day3(data) == steps


@pytest.mark.parametrize('data,steps', [
    (304, 330),
    (10, 11),
    (805, 806),
    (501, 747),

])
def test_day3p2(data, steps):
    """Test day3 part 2."""
    assert day3p2(data) == steps


if __name__ == "__main__":
    print(day3(368078))
    print(day3p2(368078))

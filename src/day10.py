"""Day 10: Knot Hash."""

import pytest
from functools import reduce


def day10(arg):
    """Day 10."""
    res = knot_hash(list(map(int, arg.split(','))))
    return res[0] * res[1]


def day10p2(arg):
    """Day 10 part 2."""
    inputs = to_ascii(arg) + [17, 31, 73, 47, 23]
    res = knot_hash(inputs, 256, 64)
    return (''.join([format(reduce(
        lambda a, b: a ^ b, res[i * 16:(i + 1) * 16]), '02x')
        for i in range(16)]))


def to_ascii(data):
    """Get list of strings return to bytes."""
    return [ord(i) for i in data]


def knot_hash(lengths, size=256, rounds=1):
    """Knot hash algorithm."""
    list_ = list(range(0, size))
    current_position = 0
    skip_size = 0
    for i in range(rounds):
        for length in lengths:
            to_reverse = []
            flip = range(current_position, current_position + length)
            for i in flip:
                to_reverse.append(list_[i % len(list_)])
            reverse = list(reversed(to_reverse))
            for k, i in enumerate(flip):
                list_[i % len(list_)] = reverse[k]
            current_position += length + skip_size
            skip_size += 1
    return list_


@pytest.mark.parametrize('data,result', [
    ("3,4,1,5", 12),
])
def test_knot_hash(data, result):
    """Test day10."""
    res = knot_hash(list(map(int, data.split(','))), 5)
    assert res[0] * res[1] == result


@pytest.mark.parametrize('data,result', [
    ("1,2,3", "49,44,50,44,51")
])
def test_to_ascii(data, result):
    """Test day10 part 2."""
    assert ','.join(map(str, to_ascii(data))) == result


@pytest.mark.parametrize('data,result', [
    ("", "a2582a3a0e66e6e86e3812dcb672a272"),
    ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
    ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
    ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
])
def test_day10p2(data, result):
    """Test day10 part 2."""
    assert day10p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day10(arg))
        print(day10p2(arg))

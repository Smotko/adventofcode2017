"""Day 14: Disk Defragmentation."""

import pytest

from day10 import day10p2


def to_bin(hx):
    """Bin function."""
    return bin(int(hx, 16))[2:].zfill(len(hx) * 4)


def day14(arg):
    """Day 14."""
    sums = 0
    for i in range(128):
        res = day10p2("{}-{}".format(arg, i))
        sums += to_bin(res).count("1")
    return sums


def mark_connected(i, j, chars, counter):
    """Recursively checks connected chars."""
    if 0 <= i < len(chars) and 0 <= j < len(chars[i]) and chars[i][j] == "1":
        chars[i][j] = counter
        mark_connected(i + 1, j, chars, counter)
        mark_connected(i, j + 1, chars, counter)
        mark_connected(i - 1, j, chars, counter)
        mark_connected(i, j - 1, chars, counter)


def day14p2(arg):
    """Day 14 part 2."""
    chars = [list(to_bin(day10p2("{}-{}".format(arg, i)))) for i in range(128)]
    counter = 0
    for i, val_list in enumerate(chars):
        for j, val in enumerate(val_list):
            if chars[i][j] == '1':
                counter += 1
                mark_connected(i, j, chars, counter)
    return counter


@pytest.mark.parametrize('data,result', [
    ("0", "0000"),
    ("1", "0001"),
    ("00", "00000000"),
    ("01", "00000001"),
])
def test_to_bin(data, result):
    """Test to_bin."""
    assert to_bin(data) == result


@pytest.mark.parametrize('data,result', [
    ("flqrgnkx", 8108),
])
def test_day14(data, result):
    """Test day14."""
    assert day14(data) == result


@pytest.mark.parametrize('data,result', [
    ("flqrgnkx", 1242),

])
def test_day14p2(data, result):
    """Test day14 part 2."""
    assert day14p2(data) == result


if __name__ == "__main__":
        print(day14("hxtvlmkl"))
        print(day14p2("hxtvlmkl"))

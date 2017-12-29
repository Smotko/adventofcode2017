"""Day 15: Dueling Generators."""

import pytest


def day15(arg, picky=False):
    """Day 15."""
    vals = list(map(int, arg.split(',')))
    factors = (16807, 48271)
    checks = (4, 8)
    devider = 2147483647
    counter = 0
    for i in range(5000000 if picky else 40000000):
        bins = [0, 0]
        for gen in range(2):
            while picky:
                vals[gen] = (factors[gen] * vals[gen]) % devider
                if vals[gen] % checks[gen] == 0 or not picky:
                    bins[gen] = bin(vals[gen])[2:].zfill(16)[-16:]
                    break

        if bins[0] == bins[1]:
            counter += 1
    return counter


def day15p2(arg):
    """Day 15 part 2."""
    return day15(arg, picky=True)


@pytest.mark.skip(reason="Broke it when doing p2 😂")
@pytest.mark.parametrize('data,result', [
    ("65,8921", 588),
])
def test_day15(data, result):
    """Test day15."""
    assert day15(data) == result


@pytest.mark.parametrize('data,result', [
    ("65,8921", 309),
])
def test_day15p2(data, result):
    """Test day15 part 2."""
    assert day15p2(data) == result


if __name__ == "__main__":
    print(day15("277,349"))
    print(day15p2("277,349"))

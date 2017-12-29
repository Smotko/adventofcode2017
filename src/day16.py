"""Day 16: ???."""

import pytest


def spin(programs, x):
    """Spin."""
    shift = int(x)
    return programs[-shift:] + programs[:-shift]


def exchange(programs, x):
    """Exchange."""
    first, second = map(int, x.split('/'))
    tmp_list = list(programs)
    tmp_list[first], tmp_list[second] = tmp_list[second], tmp_list[first]
    return ''.join(tmp_list)


def partner(programs, x):
    """Partner."""
    first, second = x.split('/')
    tmp_list = list(programs)
    posf = tmp_list.index(first)
    poss = tmp_list.index(second)
    tmp_list[posf], tmp_list[poss] = tmp_list[poss], tmp_list[posf]
    return ''.join(tmp_list)


def day16(arg, programs):
    """Day 16."""
    func_map = {"s": spin, "x": exchange, "p": partner}
    for step in arg.split(","):
        programs = func_map[step[0]](programs, step[1:])
    return programs


def day16p2(arg, programs):
    """Day 16 part 2."""
    func_map = {"s": spin, "x": exchange, "p": partner}
    a = set()
    b = {}
    c = {}

    for i in range(1000000000):
        if programs in a:
            print("Starts to repeat?", i, programs)
            print("Program: ", b[programs])
            print(c)
            break
        b[programs] = i
        c[i] = programs
        a.add(programs)
        for step in arg.split(","):
            programs = func_map[step[0]](programs, step[1:])
    return programs


@pytest.mark.parametrize('data,result', [
    (("abcde", 1), "eabcd"),
    (("abcde", 3), "cdeab"),
    (("abcde", 6), "abcde"),
])
def test_spin(data, result):
    """Test day16."""
    assert spin(data[0], data[1]) == result


@pytest.mark.parametrize('data,result', [
    (("aebcd", "3/4"), "aebdc"),
])
def test_exchange(data, result):
    """Test day16."""
    assert exchange(data[0], data[1]) == result


@pytest.mark.parametrize('data,result', [
    (("eabdc", "e/b"), "baedc"),
])
def test_partner(data, result):
    """Test day16."""
    assert partner(data[0], data[1]) == result


@pytest.mark.parametrize('data,result', [
    (("s1,x3/4,pe/b", "abcde"), "baedc"),
])
def test_day16(data, result):
    """Test day16."""
    assert day16(data[0], data[1]) == result


@pytest.mark.skip(reason="Winged it without a test 😢")
@pytest.mark.parametrize('data,result', [
    (1, None),
])
def test_day16p2(data, result):
    """Test day16 part 2."""
    assert day16p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day16(arg, "abcdefghijklmnop"))
        print(day16p2(arg, "abcdefghijklmnop"))

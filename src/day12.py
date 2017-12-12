"""Day 12: Digital Plumber."""

import pytest


def day12(arg):
    """Day 12."""
    connected = set()
    visited = set()
    links = {}
    for line in arg.split('\n'):
        program, connections = line.split(' <-> ')
        links[program] = set(connections.split(', '))

    # Connected to 0:
    connected = connected.union(links['0'])

    while len(visited) < len(connected):
        for c in connected:
            if c in visited:
                continue
            else:
                connected = connected.union(links[c])
            visited.add(c)
    return len(connected)


def day12p2(arg):
    """Day 12 part 2."""
    connected = set()
    visited = set()
    links = {}
    for line in arg.split('\n'):
        program, connections = line.split(' <-> ')
        links[program] = set(connections.split(', '))

    groups = 0
    for i in links:
        if i in connected:
            continue
        connected = connected.union(links[i])
        while len(visited) < len(connected):
            for c in connected:
                if c in visited:
                    continue
                else:
                    connected = connected.union(links[c])
                visited.add(c)
        groups += 1
    return groups


@pytest.mark.parametrize('data,result', [
    ("""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""", 6),
])
def test_day12(data, result):
    """Test day12."""
    assert day12(data) == result


@pytest.mark.parametrize('data,result', [
    ("""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
7 <-> 8, 9
8 <-> 7
9 <-> 7""", 3),
])
def test_day12p2(data, result):
    """Test day12 part 2."""
    assert day12p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day12(arg))
        print(day12p2(arg))

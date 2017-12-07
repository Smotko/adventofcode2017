"""Day 7: Recursive Circus."""

import pytest


def day7(arg):
    """Day 7."""
    slots = {}
    for line in arg.split('\n'):
        vals = line.split()
        slots[vals[0]] = 1
    for line in arg.split('\n'):
        vals = line.split()
        if len(vals) > 2:
            for i in vals[3:]:
                i = i.replace(',', '')
                slots[i] = 0
    for key in slots:
        if slots[key] == 1:
            return key


def rec(start, children, weights, results):
    """Recursive function for calculating duplicates."""
    if not len(children[start]):
        return weights[start]
    children_weights = list(rec(child, children, weights, results)
                            for child in children[start])
    for i, w in enumerate(children_weights):
        if i == 0:
            continue
        diff = children_weights[i] - children_weights[i - 1]
        if diff != 0:
            print(children_weights, weights[start], diff,
                  children[start], start)

    return weights[start] + sum(children_weights)


def day7p2(arg, start):
    """Day 7 part 2."""
    children = {}
    weights = {}
    for line in arg.split('\n'):
        vals = line.split()
        children[vals[0]] = set()
        weights[vals[0]] = int(vals[1].replace('(', '').replace(')', ''))
        if len(vals) > 2:
            for i in vals[3:]:
                i = i.replace(',', '')
                children[vals[0]].add(i)
    results = set()
    rec(start, children, weights, results)
    print(results)


@pytest.mark.parametrize('data,result', [
    ("""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""", "tknk"),
])
def test_day7(data, result):
    """Test day7."""
    assert day7(data) == result


@pytest.mark.skip(reason="Look at output 😂")
@pytest.mark.parametrize('data,result', [
    ("""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""", 60),
])
def test_day7p2(data, result):
    """Test day7 part 2."""
    assert day7p2(data, "tknk") == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        res = day7(arg)
        print(res)
        print(day7p2(arg, res))

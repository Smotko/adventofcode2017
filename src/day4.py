"""Day 4: High-Entropy Passphrases."""

import pytest


def is_still_valid(string):
    """Is the string still a valid passphrase."""
    words = string.strip().split()
    added = set()
    for word in words:
        srtd = "".join(sorted(list(word)))
        if srtd in added:
            return False
        added.add(srtd)
    return True


def is_valid(string):
    """Is the string a valid passphrase."""
    words = string.strip().split()
    added = set()
    for word in words:
        if word in added:
            return False
        added.add(word)
    return True


def day4(arg):
    """Day 4."""
    return sum(is_valid(a) for a in arg)


def day4p2(arg):
    """Day 4 part 2."""
    return sum(is_still_valid(a) for a in arg)


@pytest.mark.parametrize('data,result', [
    ("aa bb cc dd ee", True),
    ("aa bb cc dd aa", False),
    ("aa bb cc dd aaa", True),
])
def test_is_valid(data, result):
    """Test is_valid."""
    assert is_valid(data) == result


@pytest.mark.parametrize('data,result', [
    ("abcde fghij", True),
    ("abcde xyz ecdab", False),
    ("a ab abc abd abf abj", True),
    ("iiii oiii ooii oooi oooo", True),
    ("oiii ioii iioi iiio", False)

])
def test_is_still_valid(data, result):
    """Test is_still_valid."""
    assert is_still_valid(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.readlines()
        print(day4(arg))
        print(day4p2(arg))

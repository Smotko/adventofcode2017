"""Day 18: ???."""

import pytest
from collections import defaultdict


class Processor(object):
    """The processor."""

    def __init__(self, p=0):
        """Init the processor."""
        self.registers = defaultdict(int)
        self.registers["p"] = p
        self.pointer = 0
        self.last_played = -1
        self.last_received = -1
        self.queue = []
        self.other = None
        self.num_sent = 0
        self.blocked = False
        self.lines = ""
        self.program = p

    def set_other(self, other):
        """Set other."""
        self.other = other

    def start(self, lines):
        """Start the program."""
        self.lines = lines
        while self.pointer < len(lines):
            line = lines[self.pointer].split()
            # print(lines[self.pointer], self.program)
            getattr(self, line[0])(*line[1:])
            if self.last_received > -1:
                return
            self.pointer += 1

    def _reg_to_val(self, val):
        try:
            return int(val)
        except ValueError:
            return self.registers[val]

    def snd(self, x):
        """Snd command."""
        if not self.other:
            self.last_played = self._reg_to_val(x)
            return
        self.num_sent += 1

        print(self.num_sent, self.program, self.queue[:3])
        self.other.queue.append(self._reg_to_val(x))

    def set(self, x, y):
        """Set command."""
        self.registers[x] = self._reg_to_val(y)

    def add(self, x, y):
        """Add command."""
        self.registers[x] += self._reg_to_val(y)

    def mul(self, x, y):
        """Mul command."""
        self.registers[x] *= self._reg_to_val(y)

    def mod(self, x, y):
        """Mod command."""
        self.registers[x] %= self._reg_to_val(y)

    def rcv(self, x):
        """Rcv command."""
        # if self._reg_to_val(x) == 0:
        #     return
        if not self.other:
            self.last_received = self.last_played
            return
        if self.queue:
            self.registers[x] = self.queue.pop(0)
            return
        self.other.start(self.lines)
        return self.rcv(x)

    def jgz(self, x, y):
        """Jump command."""
        if self._reg_to_val(x) <= 0:
            return
        self.pointer += self._reg_to_val(y) - 1


def day18(arg):
    """Day 18."""
    p = Processor()
    p.start(arg.split('\n'))
    return p.last_received


def day18p2(arg):
    """Day 18 part 2."""
    p1 = Processor(0)
    p2 = Processor(1)
    p1.set_other(p2)
    p2.set_other(p1)
    p1.start(arg.split('\n'))
    return p1.num_sent


@pytest.mark.parametrize('data,result', [
    ("""set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""", 4),
])
def test_day18(data, result):
    """Test day18."""
    assert day18(data) == result


@pytest.mark.skip(reason="Lazy 😢")
@pytest.mark.parametrize('data,result', [
    (1, None),
])
def test_day18p2(data, result):
    """Test day18 part 2."""
    assert day18p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        # print(day18(arg))
        print(day18p2(arg))

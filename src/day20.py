"""Day 20: ???."""

import pytest
from collections import Counter


def parse(x, inpt):
    """Parse."""
    return list(map(int, inpt.replace('{}=<'.format(x), '').replace(
        '>', '').split(',')))


def add(x, y):
    """Add."""
    xa, xb, xc = x
    ya, yb, yc = y
    return xa + ya, xb + yb, xc + yc


def day20(arg):
    """Day 20."""
    particles = []
    for line in arg.split('\n'):
        pos, vel, acl = line.split(', ')
        pos, vel, acl = parse('p', pos), parse('v', vel), parse('a', acl)
        particles.append((pos, vel, acl))
    for _ in range(100):
        for i, (pos, vel, acl) in enumerate(particles):
            pos, vel = add(pos, vel), add(vel, acl)
            particles[i] = pos, vel, acl

    mini = 99999999999999999999999999999999999999999, -1

    for i, (pos, _, _) in enumerate(particles):
        if sum(map(abs, pos)) < mini[0]:
            mini = sum(pos), i
    return mini[1]


def day20p2(arg):
    """Day 20 part 2."""
    particles = []
    for line in arg.split('\n'):
        pos, vel, acl = line.split(', ')
        pos, vel, acl = parse('p', pos), parse('v', vel), parse('a', acl)
        particles.append((pos, vel, acl))
    for attr in range(2000):
        for i, par in enumerate(particles):
            if particles[i] is None:
                continue
            (pos, vel, acl) = par
            vel = add(vel, acl)
            pos = add(pos, vel)
            particles[i] = pos, vel, acl
        collisions = Counter(map(lambda x: x[0] if x is not None else (
            9999999999, 999999999, 9999999999999), particles))

        for i, par in enumerate(particles):
            if particles[i] is None:
                continue
            (pos, vel, acl) = par
            if collisions[pos] > 1:
                particles[i] = None
                print("Destroyed", i)
    cnt = 0
    for particle in particles:
        if particle is not None:
            cnt += 1
    return cnt


@pytest.mark.parametrize('data,result', [
    ("""p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>""", 0),
])
def test_day20(data, result):
    """Test day20."""
    assert day20(data) == result


@pytest.mark.parametrize('data,result', [
    ("""p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""", 1),

])
def test_day20p2(data, result):
    """Test day20 part 2."""
    assert day20p2(data) == result


if __name__ == "__main__":
    with open(__file__.replace(".py", ".txt")) as puzzle:
        arg = puzzle.read().strip()
        print(day20(arg))
        print(day20p2(arg))

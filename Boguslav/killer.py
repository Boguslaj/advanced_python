import sys

sys.setrecursionlimit(10000000)

DEATH = []


def killer(f):
    DEATH.append((f.__name__, f.__hash__))
    f(f)


def overkiller(f):
    print('Start the harvest')
    killer(f)


if __name__ == "__main__":
    overkiller(killer)

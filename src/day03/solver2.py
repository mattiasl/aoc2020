from functools import reduce
from utils.file import read_file


def a(i, dx, dy):
    def xg(mx=len(i[0]), x=0):
        while True:
            x = (x + dx) % mx
            yield x

    return reduce(lambda c, v: c + v, map(lambda c: c, [1 if i[y][x] == '#' else 0 for y, x in zip(range(dy, len(i), dy), xg())]))


def b(i, slopes):
    return reduce(lambda x, y: x * y, map(lambda slope: a(i, *slope), slopes))


i = read_file('day03/1.in').splitlines()
print(a(i, *[3, 1]), b(i, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))


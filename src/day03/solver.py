from utils.file import read_file
from functools import reduce


def a(i, dx, dy):
    trees = 0
    x = 0
    for y in range(dy, len(i), dy):
        x = (x + dx) % len(i[0])
        if i[y][x] == '#':
            trees += 1

    return trees


def b(i, slopes):
    return reduce(lambda x, y: x * y, map(lambda slope: a(i, *slope), slopes))


i = read_file('day03/1.in').splitlines()
print(a(i, *[3, 1]), b(i, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))


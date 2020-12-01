from utils.file import read_file
from itertools import product


def star_a(i):
    return [a * b for a, b in zip(i, [2020 - j for j in i]) if b in i][0]


def star_b(i):
    return [a * b * c for a, b, c in [(a, b, 2020 - (a + b)) for a, b in product(i, i)] if c in i][0]


i = list(map(int, read_file('day01/1.in').splitlines()))
print(star_a(i), star_b(i))


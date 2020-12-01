from utils.file import read_file
from itertools import product


def star_a(i):
    for a in i:
        b = 2020 - a
        if b in i:
            return a * b


def star_b(i):
    for a_plus_b, a_times_b in [(a + b, a * b) for a, b in product(i, i) if a + b < 2020]:
        d = 2020 - a_plus_b
        if d in i:
            return d * a_times_b


i = list(map(int, read_file('day01/1.in').splitlines()))
print(star_a(i), star_b(i))


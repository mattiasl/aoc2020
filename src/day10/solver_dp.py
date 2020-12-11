import time
from collections import Counter
from functools import reduce
from utils.file import read_file


def add_zero_and_max_then_sort(adapters):
    adapters.extend([0, max(adapters) + 3])
    return sorted(adapters)


def star_a(adapters):
    jolts = Counter([adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)])
    return reduce(lambda c, v: c * v, [jolts[i] for i in [1, 3]])


def star_b(adapters):
    p = [0] * len(adapters)
    p[0] = 1
    for i, a, b, c in [(i, i - 1, i - 2, i - 3) for i in range(1, len(adapters))]:
        p[i] = p[a]
        if adapters[i] - adapters[b] <= 2:
            p[i] += p[b]
        if adapters[i] - adapters[c] <= 3:
            p[i] += p[c]

    return p[-1]


data = add_zero_and_max_then_sort(list(map(int, read_file('day10/1.in').splitlines())))
start = time.time()
print(star_a(data), star_b(data))
end = time.time()
print(end - start)

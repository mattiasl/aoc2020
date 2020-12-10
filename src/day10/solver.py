from functools import reduce
from collections import Counter
from utils.file import read_file


def add_zero_and_max_then_sort(adapters):
    adapters.extend([0, max(adapters)+3])
    return sorted(adapters)


def star_a(adapters):
    jolts = Counter([adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)])
    return reduce(lambda c, v: c * v, [jolts[i] for i in [1, 3]])


def star_b(adapters):
    answer = 1
    diff = [x - y for y, x in zip(adapters[:-1], adapters[1:])]
    i = 0
    while i < len(diff):
        perm, jmp = 1, 1
        if diff[i:i+4] == [1, 1, 1, 1]:
            perm, jmp = 7, 3
        elif diff[i:i+3] == [1, 1, 1]:
            perm, jmp = 4, 2
        elif diff[i:i+2] == [1, 1]:
            perm = 2

        answer *= perm
        i += jmp

    return answer


data = add_zero_and_max_then_sort(list(map(int, read_file('day10/1.in').splitlines())))
print(star_a(data), star_b(data))

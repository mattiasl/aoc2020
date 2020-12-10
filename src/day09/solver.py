from itertools import combinations
from utils.file import read_file


def star_a(d, preamble=25):
    q = [int(i) for i in d]
    for start, end in [(i-preamble, i) for i in range(preamble, len(q))]:
        if q[end] not in set(map(sum, (combinations(q[start:end], 2)))):
            return q[end]


def star_b(d, target):
    q = [int(i) for i in d]
    for preamble in range(2, len(q)):
        for numbers in [q[start:end] for start, end in [(i, i+preamble) for i in range(0, len(q)-preamble)]]:
            if sum(numbers) == target:
                return min(numbers) + max(numbers)


data = read_file('day09/1.in').splitlines()
a = star_a(data)
print(a, star_b(data, a))


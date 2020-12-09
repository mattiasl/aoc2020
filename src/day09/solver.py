from itertools import permutations
from utils.file import read_file


def star_a(d, preamble=25):
    q = [int(i) for i in d]
    for i in range(preamble, len(q)):
        if q[i] not in set(map(sum, (permutations(q[i-preamble:i], 2)))):
            return q[i]


def star_b(d, magic_number):
    q = [int(i) for i in d]
    for preamble in range(2, len(q)):
        for i in range(preamble, len(q)):
            candidates = q[i-preamble:i]
            if sum(candidates) == magic_number:
                return min(candidates) + max(candidates)


data = read_file('day09/1.in').splitlines()
a = star_a(data)
print(a, star_b(data, a))


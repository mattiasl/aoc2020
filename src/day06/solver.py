from utils.file import read_file
from functools import reduce
from collections import Counter


def parse(i):
    return list(map(lambda x: x.split('\n'), i))


def star_a(groups):
    return sum(map(lambda x: len(reduce(lambda a, v: a | set(list(v)), x, set())), groups))


def count_questions_everybody_answered_yes(s):
    return len(list(filter(lambda a: a == len(s), reduce(lambda a, v: a + Counter(v), s, Counter({})).values())))


def star_b(groups):
    return reduce(lambda a, v: a + v, map(count_questions_everybody_answered_yes, groups))


data = read_file('day06/1.in').split('\n\n')
print(star_a(parse(data)), star_b(parse(data)))


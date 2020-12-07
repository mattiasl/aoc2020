from utils.file import read_file
import re
from functools import reduce


def to_val(n, b):
    return int(n), f'{b}s'


def parse(rules):
    answer = {}
    for r in rules:
        bag, contents = r.split(' contain ')
        c = contents.split(', ')
        answer[bag] = [] if c[0] == 'no other bags' else [to_val(*re.match('([0-9]+).(.*bag)', x).groups()) for x in c]

    return answer


def can_hold_gold_bag(bag, bags):
    answer = False
    for candidate in bags[bag]:
        if candidate[1] == 'shiny gold bags':
            answer = True
        else:
            answer |= can_hold_gold_bag(candidate[1], bags)

    return answer


def count_bags_in_bag(bag, bags):
    return reduce(lambda a, v: a + (v[0] * count_bags_in_bag(v[1], bags)), bags[bag], 1)


def star_a(bags):
    return sum([1 if can_hold_gold_bag(bag, bags) else 0 for bag in bags.keys()])


def star_b(bags):
    return count_bags_in_bag('shiny gold bags', bags) - 1


data = read_file('day07/1.in').replace('.', '').splitlines()
print(star_a(parse(data)), star_b(parse(data)))


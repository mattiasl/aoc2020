from utils.file import read_file
import re
from functools import reduce


def gen_regex(rule, rules, recur, max_recur=6):
    """Started with max_recur 10 and it gave the correct answer, then it was a matter of binary search until 6 was found
    to be the minimum max_recur that provides the correct answer"""
    if rule in recur.keys():
        if recur[rule] < max_recur:
            recur[rule] += 1
        else:
            return ''

    if re.match('[ab]', rule):
        return rule
    elif re.match(' |', rule):
        alternatives = []
        for or_rule in rule.split(' | '):
            alternatives.append(reduce(lambda a, c: a + gen_regex(rules[c], rules, recur), or_rule.split(' '), ''))
        return '(' + '|'.join(alternatives) + ')'
    else:
        return reduce(lambda a, c: a + gen_regex(rules[c], rules, recur), '')


def make_test(regex):
    def fn(message):
        match = regex.match(message)
        return match and match.span()[0] == 0 and match.span()[1] == len(message)
    return fn


def solve(raw_rules, messages, overrides={}):
    rules = {}
    for line in raw_rules.split('\n'):
        splits = line.split(': ')
        index, rule = splits[0], splits[1]
        rules[index] = rule.strip('\"')

    rules = {**rules, **overrides}
    test = make_test(re.compile(gen_regex(rules['0'], rules, dict.fromkeys(overrides.values(), 0))))
    return reduce(lambda a, c: a + (1 if test(c) else 0), messages.split('\n'), 0)


data = read_file('day19/1.in').split('\n\n')
print(solve(*data), solve(*data, {'8': '42 | 42 8', '11': '42 31 | 42 11 31'}))


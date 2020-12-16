import re
from functools import reduce
from utils.file import read_file


def make_rule(rule):
    m = re.match('([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', rule.split(': ')[1])
    a, b, c, d = [int(m.group(i)) for i in range(1, 5)]
    return lambda x: a <= x <= b or c <= x <= d


def star_a(notes):
    rules = [make_rule(rule) for rule in notes[0].splitlines()]
    nearby_tickets = [map(int, nearby_ticket.split(',')) for nearby_ticket in notes[2].splitlines()[1:]]
    answer = []
    for nearby_ticket in nearby_tickets:
        answer += filter(lambda val: not reduce(lambda a, r: a | r(val), rules, False), nearby_ticket)
    return sum(answer)


def is_valid(nearby_ticket, rules):
    return nearby_ticket == list(filter(lambda val: reduce(lambda a, r: a | r(val), rules, False), nearby_ticket))


def remove_value_from_sets(sets, value):
    for s in sets:
        if value in s:
            s.remove(value)


def star_b(notes):
    rules = [make_rule(rule) for rule in notes[0].splitlines()]
    my_ticket = list(map(int, notes[1].splitlines()[1].split(',')))
    nearby_tickets = [list(map(int, nearby_ticket.split(','))) for nearby_ticket in notes[2].splitlines()[1:]]

    valid_ticket_transposed = list(zip(*filter(lambda ticket: is_valid(ticket, rules), nearby_tickets)))

    rules_matching_all_entries_per_col = []
    for values_for_a_col in valid_ticket_transposed:
        matches_per_rule = set()
        for rule_idx in [i for i, rule in enumerate(rules) if reduce(lambda a, v: a & rule(v), values_for_a_col, True)]:
            matches_per_rule.add(rule_idx)
        rules_matching_all_entries_per_col.append(matches_per_rule)

    mapping = {}
    while len(mapping) < len(rules):
        for i, val in [(i, s.pop()) for i, s in enumerate(rules_matching_all_entries_per_col) if len(s) == 1]:
            mapping[val] = i
            remove_value_from_sets(rules_matching_all_entries_per_col, val)

    answer = 1
    for col in [i for i, row in enumerate(notes[0].splitlines()) if row.startswith('departure')]:
        answer *= my_ticket[mapping[col]]

    return answer


data = read_file('day16/1.in').split('\n\n')
print(star_a(data), star_b(data))


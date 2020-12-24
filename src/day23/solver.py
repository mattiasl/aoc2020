class Cup:
    def __init__(self, label):
        self.label = label
        self.next_cup = None


def pick_n_cups(cup, n=3):
    start_cup, values = cup.next_cup, []
    cur = start_cup
    for i in range(n - 1):
        values.append(cur.label)
        cur = cur.next_cup

    values.append(cur.label)
    cup.next_cup, cur.next_cup = cur.next_cup, None
    return start_cup, values


def insert_picked_cups_at(cup, picked):
    end = picked
    while end.next_cup:
        end = end.next_cup
    end.next_cup, cup.next_cup = cup.next_cup, picked


def crab_cups(moves, additional_cups, inp='952438716'):
    cups, cups_by_label = [], {}
    for i, val in enumerate(list(map(int, inp)) + [x for x in range(10, additional_cups)]):
        cup = Cup(val)
        if i > 0:
            cups[i - 1].next_cup = cup
        cups.append(cup)
        cups_by_label[val] = cup
    # close the circle
    cup.next_cup = cups[0]

    current = cups[0]
    for _ in range(moves):
        picked_cups, picked_values = pick_n_cups(current)
        destination = current.label - 1 if current.label > 1 else len(cups)
        while destination in picked_values:
            destination -= 1
            if destination < 1:
                destination = len(cups)

        insert_picked_cups_at(cups_by_label[destination], picked_cups)
        current = current.next_cup

    return cups_by_label[1]


def star_a():
    cur = crab_cups(100, 0).next_cup
    answer = []
    for _ in range(8):
        answer.append(cur.label)
        cur = cur.next_cup

    return ''.join(map(str, answer))


def star_b():
    cur = crab_cups(10 * 1000 * 1000, 1000001).next_cup
    answer = 1
    for _ in range(2):
        answer *= int(cur.label)
        cur = cur.next_cup

    return answer


print(star_a(), star_b())


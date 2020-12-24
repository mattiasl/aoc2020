from functools import reduce

from utils.file import read_file


def parse(inp):
    decks = []
    for i in range(2):
        q = []
        for card in [cards for cards in inp[i].split('\n')][1:]:
            q.append(int(card))
        decks.append(q)
    return decks


def get_score(deck):
    answer = 0
    for i in range(len(deck), 0, -1):
        answer += i * deck.pop(0)
    return answer


def star_a(decks):
    while not reduce(lambda x, d: x | (len(d) == 0), decks, False):
        a, b = map(lambda x: x.pop(0), decks)
        if a > b:
            decks[0] += [a, b]
        else:
            decks[1] += [b, a]

    return get_score(decks[0] if len(decks[1]) == 0 else decks[1])


def generate_key(deck):
    return ','.join(map(str, deck))


def star_b_solver(decks):
    memory = {0: set(), 1: set()}
    while decks[0] and decks[1]:
        for i, deck in enumerate(decks):
            key = generate_key(deck)
            if key in memory[i]:
                return 0
            memory[i].add(key)

        a, b = map(lambda x: x.pop(0), decks)
        if a <= len(decks[0]) and b <= len(decks[1]):
            winner = star_b_solver([decks[0][:a], decks[1][:b]])
        else:
            if a > b:
                winner = 0
            else:
                winner = 1

        if winner == 0:
            decks[0] += [a, b]
        else:
            decks[1] += [b, a]

    return 0 if len(decks[1]) == 0 else 1


def star_b(decks):
    return get_score(decks[star_b_solver(decks)])


data = read_file('day22/1.in').split('\n\n')
print(star_a(parse(data)), star_b(parse(data)))

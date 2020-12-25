from utils.file import read_file
import re

mapper = {
    'e': (1, -1, 0),
    'w': (-1, 1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'ne': (1, 0, -1),
    'nw': (0, 1, -1)
}


def star_a(inp):
    blacks = set()
    for tile in inp:
        current = (0, 0, 0)
        for move in map(lambda d: mapper[d], re.findall('(se|sw|ne|nw|e|w)', tile)):
            current = tuple(map(lambda x, y: x + y, current, move))
        if current not in blacks:
            blacks.add(current)
        else:
            blacks.remove(current)

    return blacks


def get_adjacent_tiles(tile):
    answer = set()
    for adjacent in mapper.values():
        answer.add(tuple(map(lambda x, y: x + y, tile, adjacent)))
    return answer


def star_b(blacks, days=100):
    for _ in range(days):
        new_blacks = set()
        for black in blacks:
            adjacent = get_adjacent_tiles(black)
            adjacent_blacks = blacks.intersection(adjacent)
            if len(adjacent_blacks) in [1, 2]:
                new_blacks.add(black)
            adjacent_whites = adjacent - blacks
            for adjacent_white in adjacent_whites:
                if len(get_adjacent_tiles(adjacent_white).intersection(blacks)) == 2:
                    new_blacks.add(adjacent_white)

        blacks = new_blacks

    return len(blacks)


data = read_file('day24/1.in').splitlines()
print(len(star_a(data)), star_b(star_a(data)))


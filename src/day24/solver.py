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


def add_tiles(a, b):
    return tuple(map(lambda x, y: x + y, a, b))


def star_a(inp):
    blacks = set()
    for tile in inp:
        current = (0, 0, 0)
        for move in map(lambda d: mapper[d], re.findall('(se|sw|ne|nw|e|w)', tile)):
            current = add_tiles(current, move)
        if current not in blacks:
            blacks.add(current)
        else:
            blacks.remove(current)

    return blacks


def star_b(blacks, days=100):
    def get_adjacent_tiles(tile):
        answer = set()
        for offset in mapper.values():
            answer.add(add_tiles(tile, offset))
        return answer

    for _ in range(days):
        new_blacks = set()
        adjacent_whites = set()
        for black in blacks:
            adjacent = get_adjacent_tiles(black)
            adjacent_blacks = blacks.intersection(adjacent)
            if len(adjacent_blacks) in [1, 2]:
                new_blacks.add(black)
            adjacent_whites |= adjacent

        for adjacent_white in adjacent_whites-blacks:
            if len(get_adjacent_tiles(adjacent_white).intersection(blacks)) == 2:
                new_blacks.add(adjacent_white)

        blacks = new_blacks

    return blacks


data = read_file('day24/1.in').splitlines()
print(len(star_a(data)), len(star_b(star_a(data))))


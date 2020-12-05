from utils.file import read_file


def decode(replacement, s):
    return int(''.join([replacement.get(c, c) for c in s]), 2)


def to_seat(boardingpass):
    return {
        'row': decode({'F': '0', 'B': '1'}, boardingpass[:7]),
        'col': decode({'L': '0', 'R': '1'}, boardingpass[7:])
    }


def to_id(seat):
    return seat['row'] * 8 + seat['col']


def star_a(seats, fn=max):
    return fn([to_id(to_seat(bp)) for bp in seats])


def star_b(seats):
    return (set(range(star_a(seats, min), star_a(seats))) - set(star_a(seats, lambda x: x))).pop()


data = read_file('day05/1.in').splitlines()
print(star_a(data), star_b(data))


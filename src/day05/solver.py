from utils.file import read_file


def decode(replacement, s):
    return int(''.join([replacement.get(c) for c in s]), 2)


def to_seat(boardingpass):
    return {
        'row': decode({'F': '0', 'B': '1'}, boardingpass[:7]),
        'col': decode({'L': '0', 'R': '1'}, boardingpass[7:])
    }


def to_id(seat):
    return seat['row'] * 8 + seat['col']


def star_a(bp, fn=max):
    return fn([to_id(to_seat(b)) for b in bp])


def star_b(bp):
    return (set(range(star_a(bp, min), star_a(bp))) - set(star_a(bp, lambda x: x))).pop()


data = read_file('day05/1.in').splitlines()
print(star_a(data), star_b(data))


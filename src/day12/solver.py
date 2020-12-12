import re
from utils.file import read_file


def mhd(ship_pos):
    return int(abs(ship_pos.real) + abs(ship_pos.imag))


def star_a(navigation_instructions, ship_dir, ship_pos=0+0j):
    for cmd, arg in navigation_instructions:
        if cmd in dirs.keys():
            ship_pos += dirs[cmd] * arg
        elif cmd in rotations.keys():
            ship_dir *= rotations[cmd] ** int(arg / 90)
        else:
            ship_pos += ship_dir * arg
    return mhd(ship_pos)


def star_b(navigation_instructions, waypoint, ship_pos=0+0j):
    for cmd, arg in navigation_instructions:
        if cmd in dirs.keys():
            waypoint += dirs[cmd] * arg
        elif cmd in rotations.keys():
            waypoint *= rotations[cmd] ** int(arg / 90)
        else:
            ship_pos += waypoint * arg
    return mhd(ship_pos)


data = list(map(lambda m: (m.group(1), int(m.group(2))),
                [re.search('([NSEWLRF])([0-9]+)', i) for i in read_file('day12/1.in').splitlines()]))
dirs = {'N': 0 - 1j, 'E': 1 + 0j, 'S': 0 + 1j, 'W': -1 + 0j}
rotations = {'L': 0 - 1j, 'R': 0 + 1j}

print(star_a(data, dirs['E']), star_b(data, 10 - 1j))


import re
from utils.file import read_file


def mhd(ship_pos):
    return int(abs(ship_pos.real) + abs(ship_pos.imag))


def solve(navigation_instructions, compasses, ships=[0+0j, 0+0j]):
    for cmd, arg in navigation_instructions:
        if cmd in dirs.keys():
            ships[0] += dirs[cmd] * arg
            compasses[1] += dirs[cmd] * arg
        elif cmd in rotations.keys():
            compasses[0] *= rotations[cmd] ** int(arg / 90)
            compasses[1] *= rotations[cmd] ** int(arg / 90)
        else:
            ships[0] += compasses[0] * arg
            ships[1] += compasses[1] * arg

    return [mhd(ship) for ship in ships]


data = list(map(lambda m: (m.group(1), int(m.group(2))),
                [re.search('([NSEWLRF])([0-9]+)', i) for i in read_file('day12/1.in').splitlines()]))
dirs = {'N': 0 - 1j, 'E': 1 + 0j, 'S': 0 + 1j, 'W': -1 + 0j}
rotations = {'L': 0 - 1j, 'R': 0 + 1j}

print(*solve(data, [dirs['E'], 10 - 1j]))


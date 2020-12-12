from utils.file import read_file
import re
from functools import reduce


def mhd(ship_pos):
    return int(abs(ship_pos.real) + abs(ship_pos.imag))


def star_a(navigation_instructions, ship_dir, ship_pos=complex(0, 0)):
    for cmd, arg in navigation_instructions:
        if cmd in dirs.keys():
            ship_pos += dirs[cmd] * arg
        elif cmd in rotations.keys():
            ship_dir = reduce(lambda a, _: a * rotations[cmd], range(int(arg / 90)), ship_dir)
        else:
            ship_pos += ship_dir * arg
    return mhd(ship_pos)


def star_b(navigation_instructions, waypoint, ship_pos=complex(0, 0)):
    for cmd, arg in navigation_instructions:
        if cmd in dirs.keys():
            waypoint += dirs[cmd] * arg
        elif cmd in rotations.keys():
            waypoint = reduce(lambda a, _: a * rotations[cmd], range(int(arg / 90)), waypoint)
        else:
            ship_pos += waypoint * arg
    return mhd(ship_pos)


data = list(map(lambda m: (m.group(1), int(m.group(2))),
                [re.search('([NSEWLRF])([0-9]+)', i) for i in read_file('day12/1.in').splitlines()]))
dirs = {'N': complex(0, -1), 'E': complex(1, 0), 'S': complex(0, 1), 'W': complex(-1, 0)}
rotations = {'L': complex(0, -1), 'R': complex(0, 1)}

print(star_a(data, dirs['E']), star_b(data, complex(10, -1)))


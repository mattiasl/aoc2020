from utils.file import read_file
from functools import reduce


def to_string(seat_layout):
    return ''.join(seat_layout)


def get_adjacent_seats(s_l, x, y, mx, my):
    return reduce(lambda c, v: c+s_l[v[0]][v[1]], [(y+b, x+a) for b, a in dirs if 0 <= y+b < my and 0 <= x+a < mx], '')


def get_visible_seat_in_dir(seat_layout, y, x, my, xm, dy, dx):
    if 0 <= y < my and 0 <= x < xm:
        if seat_layout[y][x] is '.':
            return get_visible_seat_in_dir(seat_layout, y + dy, x + dx, my, xm, dy, dx)
        else:
            return seat_layout[y][x]
    else:
        return ''


def get_visible_seats(seat_layout, x, y, mx, my):
    return reduce(lambda c, v: c+get_visible_seat_in_dir(seat_layout, y + v[0], x + v[1], my, mx, *v), dirs, '')


def get_updated_seat_layout(current_seat_layout, mx, my, seat_constraint, fn):
    updated_seat_layout = []
    for y in range(my):
        updated_seat_row = ''
        for x in range(mx):
            accepted_seats = fn(current_seat_layout, x, y, mx, my)
            if current_seat_layout[y][x] == 'L' and accepted_seats.count('#') == 0:
                updated_seat_row += '#'
            elif current_seat_layout[y][x] == '#' and accepted_seats.count('#') >= seat_constraint:
                updated_seat_row += 'L'
            else:
                updated_seat_row += current_seat_layout[y][x]
        updated_seat_layout.append(updated_seat_row)
    return updated_seat_layout


def run(seat_layout, seat_constraint, fn):
    mem = set()
    my, mx = len(seat_layout), len(seat_layout[0])
    seat_layout_string = to_string(seat_layout)
    while seat_layout_string not in mem:
        mem.add(seat_layout_string)
        seat_layout = get_updated_seat_layout(seat_layout, mx, my, seat_constraint, fn)
        seat_layout_string = to_string(seat_layout)
    return seat_layout_string.count('#')


dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
data = read_file('day11/1.in').splitlines()
print(run(data, 4, get_adjacent_seats), run(data, 5, get_visible_seats))

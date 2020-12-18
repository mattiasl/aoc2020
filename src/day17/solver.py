from utils.file import read_file
import itertools
from operator import add


def get_neighbors(cube, dimension):
    answer = set()
    for d in itertools.product([-1, 0, 1], repeat=dimension):
        answer.add(tuple(list(map(add, cube, d))))
    answer.remove(cube)
    return answer


def cycle(active_cubes, dimension):
    answer = set()
    inactive_neigbor_cubes = set()
    for cube in active_cubes:
        neighbors = get_neighbors(cube, dimension)
        if len(active_cubes.intersection(neighbors)) in [2, 3]:
            answer.add(cube)
        inactive_neigbor_cubes |= (neighbors - active_cubes)

    for inactive_cube in inactive_neigbor_cubes:
        if len(active_cubes.intersection(get_neighbors(inactive_cube, dimension))) == 3:
            answer.add(inactive_cube)

    return answer


def solve(initial_state, dimension, cycles=6):
    zeros = [0] * (dimension - 2)
    active_cubes = set()
    for y, row in enumerate(initial_state.splitlines()):
        for x in [x for x, c in enumerate(list(row)) if c == '#']:
            active_cubes.add((x, y, *zeros))

    for _ in range(cycles):
        active_cubes = cycle(active_cubes, dimension)

    return len(active_cubes)


data = read_file('day17/1.in')
print(solve(data, 3), solve(data, 4))


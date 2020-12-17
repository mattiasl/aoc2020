from utils.file import read_file


def get_neighbors_3d(x, y, z):
    answer = set()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx != 0 or dy != 0 or dz != 0:
                    answer.add((x+dx, y+dy, z+dz))
    return answer


def star_a(initial_state):
    z = 0
    active_cubes = set()
    for y, row in enumerate(initial_state.splitlines()):
        for x in [x for x, c in enumerate(list(row)) if c == '#']:
            active_cubes.add((x, y, z))

    for cycle in range(6):
        next_cycle_active_cubes = set()
        inactive_cubes = set()
        for cube in active_cubes:
            neighbors = get_neighbors_3d(*cube)
            if len(active_cubes.intersection(neighbors)) in [2, 3]:
                next_cycle_active_cubes.add(cube)
            inactive_cubes |= (neighbors - active_cubes)

        for inactive_cube in inactive_cubes:
            if len(active_cubes.intersection(get_neighbors_3d(*inactive_cube))) == 3:
                next_cycle_active_cubes.add(inactive_cube)

        active_cubes = next_cycle_active_cubes

    return len(active_cubes)


def get_neighbors_4d(x, y, z, w):
    answer = set()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                        answer.add((x+dx, y+dy, z+dz, w+dw))

    return answer


def star_b(initial_state):
    z, w = 0, 0
    active_cubes = set()
    for y, row in enumerate(initial_state.splitlines()):
        for x in [x for x, c in enumerate(list(row)) if c == '#']:
            active_cubes.add((x, y, z, w))

    for cycle in range(6):
        next_cycle_active_cubes = set()
        inactive_cubes = set()
        for cube in active_cubes:
            neighbors = get_neighbors_4d(*cube)
            if len(active_cubes.intersection(neighbors)) in [2, 3]:
                next_cycle_active_cubes.add(cube)
            inactive_cubes |= (neighbors - active_cubes)

        for inactive_cube in inactive_cubes:
            if len(active_cubes.intersection(get_neighbors_4d(*inactive_cube))) == 3:
                next_cycle_active_cubes.add(inactive_cube)

        active_cubes = next_cycle_active_cubes

    return len(active_cubes)


data = read_file('day17/1.in')
print(star_a(data), star_b(data))


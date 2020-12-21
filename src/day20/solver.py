from utils.file import read_file
import re
import collections
from functools import reduce


def rotate(part):
    return list(map(lambda r: ''.join(r), list(zip(*part[::-1]))))


def flip(part):
    answer = []
    for row in part:
        answer.append(row[::-1])
    return answer


def get_edges(part):
    up, down = part[0], part[len(part) - 1]
    transposed = rotate(part)
    left, right = transposed[0], transposed[len(transposed) - 1]
    return [up, right, down, left]


def get_reversed_edges(edges):
    return [edge[::-1] for edge in edges]


def get_all_possible_edges(image):
    answer = get_edges(image)
    answer.extend(get_reversed_edges(answer))
    return answer


def parse_tiles(inp):
    tiles = {}
    for tile in inp:
        image_data = tile.splitlines()
        tile_id = re.search('Tile (\\d+):', image_data[0]).group(1)
        tiles[tile_id] = image_data[1:]
    return tiles


def classify_tiles(tiles):
    all_edges = []
    for _, tile in tiles.items():
        all_edges.extend(get_all_possible_edges(tile))
    counter = collections.Counter(all_edges)

    edges, corners, centers = [], [], []
    for tile_id, tile in tiles.items():
        number_of_single_matching_edges = []
        for edge in get_edges(tile):
            if counter[edge] == 1 and counter[edge[::-1]] == 1:
                number_of_single_matching_edges.append(edge)

        if len(number_of_single_matching_edges) == 2:
            corners.append(tile_id)
        elif len(number_of_single_matching_edges) == 1:
            edges.append(tile_id)
        else:
            centers.append(tile_id)

    return corners, edges, centers, counter


def find_tile_with_matching_edge(tiles, used_tiles, positions, edge_to_tiles, counter, x, y):
    tile_up, tile_left = positions.get((x, y - 1), None), positions.get((x - 1, y), None)
    matching_left_edge = get_edges(tiles[tile_left])[1] if tile_left else None
    matching_top_edge = get_edges(tiles[tile_up])[2] if tile_up else None

    # find a tile with matching edge
    matching_tile_id = None
    if matching_left_edge:
        for c in edge_to_tiles.get(matching_left_edge):
            if c not in used_tiles:
                matching_tile_id = c
    elif matching_top_edge:
        for c in edge_to_tiles.get(matching_top_edge):
            if c not in used_tiles:
                matching_tile_id = c

    partial_image = tiles[matching_tile_id]

    # find rotation/flip
    while True:
        # try all rotations
        for i in range(4):
            up, _, _, left = get_edges(partial_image)
            if (not matching_top_edge and counter[up] == 1 and matching_left_edge == left) or \
                    (not matching_left_edge and counter[left] == 1 and matching_top_edge == up) or \
                    (matching_top_edge == up and matching_left_edge == left):
                tiles[matching_tile_id] = partial_image
                return matching_tile_id
            partial_image = rotate(partial_image)

        # no match, try flipping the image
        partial_image = flip(partial_image)


def merge_tiles_into_image(tiles, positions, size):
    tile_size = len(tiles[positions[(0, 0)]])
    image = []
    for y in range(size):
        rows = [[] for _ in range(tile_size - 2)]
        for x in range(size):
            tile = tiles[positions[(x, y)]]
            for line in range(1, tile_size - 1):
                rows[line - 1].append(tile[line][1:-1])
        for row in rows:
            image.append(''.join(row))
    return image


def is_monster_in_part(part):
    return reduce(lambda a, c: a & True if monster_regex[c].match(part[c]) else False, range(len(monster_regex)), True)


def get_number_of_monsters_in_image(image):
    count = 0
    for row in range(1, len(image) - 1):
        for i in range(0, len(image) - monster_length):
            if is_monster_in_part(
                    [image[row - 1][i:i + monster_length],
                     image[row + 0][i:i + monster_length],
                     image[row + 1][i:i + monster_length]]):
                count += 1
    return count


def star_a(tiles):
    return reduce(lambda a, c: a * int(c), classify_tiles(tiles)[0], 1)


def star_b(tiles):
    corners, edges, _, counter = classify_tiles(tiles)
    current_tile_id = corners[0]
    current_tile = tiles[current_tile_id]
    placed = set()
    positions = { (0, 0): current_tile_id }
    size = int(len(edges) / 4) + 2

    edge_to_tiles = {}
    for tile_id, tile in tiles.items():
        for edge in get_all_possible_edges(tile):
            edge_to_tile = edge_to_tiles.get(edge, set())
            edge_to_tile.add(tile_id)
            edge_to_tiles[edge] = edge_to_tile

    # rotate first tile to correct position
    while True:
        up, _, _, left = get_edges(current_tile)
        if counter[up] == 1 and counter[left] == 1:
            tiles[current_tile_id] = current_tile
            break
        else:
            current_tile = rotate(current_tile)

    placed.add(current_tile_id)
    for y in range(size):
        for x in range(size):
            if x != 0 or y != 0:
                found_tile_id = find_tile_with_matching_edge(tiles, placed, positions, edge_to_tiles, counter, x, y)
                placed.add(found_tile_id)
                positions[(x, y)] = found_tile_id

    image = merge_tiles_into_image(tiles, positions, size)

    monster_count = 0
    for _ in range(2):
        for _ in range(4):
            monster_count += get_number_of_monsters_in_image(image)
            image = rotate(image)

        image = flip(image)

    return reduce(lambda a, line: a + line.count('#'), image, 0) - (monster_count * sea_monster.count('#'))


sea_monster = """\
                  #
#    ##    ##    ###
 #  #  #  #  #  #\
"""
monster_regex = list(map(lambda x: re.compile(x.replace(' ', '.')), sea_monster.splitlines()))
monster_length = max(map(lambda x: len(x), sea_monster.splitlines()))

data = read_file('day20/1.in').split('\n\n')
print(star_a(parse_tiles(data)), star_b(parse_tiles(data)))


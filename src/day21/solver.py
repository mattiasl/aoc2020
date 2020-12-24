from utils.file import read_file


def find_possible_ingredients(allergen, foods):
    answer = []
    for ingredients, allergens in foods.items():
        if allergen in allergens:
            answer.append(set(ingredients))
    return set.intersection(*answer)


def parse(inp):
    allergens = set()
    foods = {}
    for i, food in enumerate(inp):
        current_ingredients, current_allergens = food[0:-1].split(' (contains ')
        current_ingredients = tuple(current_ingredients.split(' '))
        current_allergens = set(current_allergens.split(', '))
        foods[current_ingredients] = current_allergens
        allergens.update(current_allergens)

    return allergens, foods


def solve(inp):
    allergens, foods = parse(inp)

    allergen_to_ingredient_map = {}
    while len(allergen_to_ingredient_map) < len(allergens):
        for allergen in allergens:
            possible_candidates = find_possible_ingredients(allergen, foods) - set(allergen_to_ingredient_map.values())
            if len(possible_candidates) == 1:
                ingredient = possible_candidates.pop()
                allergen_to_ingredient_map[allergen] = ingredient

    part1 = 0
    for current_ingredients in foods.keys():
        part1 += len(set(current_ingredients) - set(allergen_to_ingredient_map.values()))

    part2 = []
    for k in sorted(allergen_to_ingredient_map.keys()):
        part2.append(allergen_to_ingredient_map[k])

    return part1, ','.join(part2)


data = read_file('day21/1.in').split('\n')
print(*solve(data))


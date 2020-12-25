
def star_a(card, door):
    value = 1
    n = 20201227
    loop_size = 0
    while value != card:
        value = (value * 7) % n
        loop_size += 1

    return pow(door, loop_size, n)


print(star_a(*[9789649, 3647239]))


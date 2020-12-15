from utils.file import read_file
import re
import itertools
import time


def get_as_binary(x):
    return format(x, 'b').zfill(36)


def apply_mask_a(mask, value):
    answer = list(get_as_binary(0))
    for bit in range(len(value)):
        answer[bit] = value[bit] if mask[bit] == 'X' else mask[bit]
    return answer


def star_a(program):
    mem = {}
    mask = None
    for line in program:
        if re.search('mask', line):
            mask = re.search('mask = (.*)', line).group(1)
        else:
            m = re.search('mem\\[([0-9]+)] = (.*)', line)
            address, value = m.group(1), m.group(2)
            mem[address] = int(''.join(apply_mask_a(mask, get_as_binary(int(value)))), 2)
    return sum(mem.values())


def get_addresses(result):
    pos = [i for i, c in enumerate(result) if c == 'X']
    answer = []
    for replacement in itertools.product('01', repeat=result.count('X')):
        for i, p in enumerate(pos):
            result[p] = f'{replacement[i]}'
        answer.append(int(''.join(result), 2))
    return answer


def apply_mask_b(mask, value):
    answer = list(get_as_binary(0))
    for bit in range(len(value)):
        answer[bit] = mask[bit] if mask[bit] in ['X', '1'] else value[bit]
    return answer


def star_b(program):
    mem = {}
    mask = None
    for line in program:
        if re.search('mask', line):
            mask = re.search('mask = (.*)', line).group(1)
        else:
            m = re.search('mem\\[([0-9]+)] = (.*)', line)
            address, value = int(m.group(1)), int(m.group(2))
            result = apply_mask_b(mask, get_as_binary(address))
            for address in get_addresses(result):
                mem[address] = value
    return sum(mem.values())


data = read_file('day14/1.in').splitlines()

start = time.time()
print(star_a(data), star_b(data))
end = time.time()
print(end - start)

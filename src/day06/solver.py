from utils.file import read_file


def parse(i):
    return map(lambda x: x.split(), i)


def star_a(groups):
    return sum(map(lambda x: len(set.union(*[set(s) for s in x])), groups))


def star_b(groups):
    return sum(map(lambda x: len(set.intersection(*[set(s) for s in x])), groups))


data = read_file('day06/1.in').split('\n\n')
print(star_a(parse(data)), star_b(parse(data)))


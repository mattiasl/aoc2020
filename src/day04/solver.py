from utils.file import read_file
from functools import reduce
import re


def to_dict(passport):
    return dict(p.split(':') for p in passport)


def verify_passport_a(passport, val=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
    return all(p in passport.keys() for p in val)


def verify_passport_b(passport, val):
    return reduce(lambda c, v: c & v, map(lambda x: bool(val[x](passport[x])), passport.keys()), True)


def to_passports(batch):
    return [to_dict(passport) for passport in map(lambda p: re.split(' |\n', p), batch)]


def star_a(passports):
    return reduce(lambda c, v: c + v, map(verify_passport_a, passports))


def star_b(passports):
    val = {
        'byr': lambda byr: 1920 <= int(byr) <= 2002,
        'iyr': lambda issue_year: 2010 <= int(issue_year) <= 2020,
        'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
        'hgt': lambda hgt: re.match(r'^((59|6[0-9]|7[0-6])in)|(1([5-8][0-9]|9[0-3])cm)$', hgt),
        'hcl': lambda hcl: re.match(r'^#[0-9a-f]{6}$', hcl),
        'ecl': lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda pid: re.match(r'^[0-9]{9}$', pid),
        'cid': lambda cid: True
    }
    return reduce(lambda c, v: c + v, map(lambda p: verify_passport_b(p, val), filter(verify_passport_a, passports)))


data = read_file('day04/1.in').split('\n\n')
print(star_a(to_passports(data)), star_b(to_passports(data)))


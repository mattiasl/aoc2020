from utils.file import read_file
import re


def is_valid(verify_function, policy, password):
    return verify_function(re.split(' |-', policy), password)


def is_valid_a(policy, password):
    return int(policy[0]) <= password.count(policy[2]) <= int(policy[1])


def is_valid_b(policy, password):
    return len([i for i in map(int, policy[0:2]) if password[i - 1] == policy[2]]) == 1


def count_valid_passwords(passwords, verify_function):
    return len([pw for pw in passwords if is_valid(verify_function, *pw.split(': '))])


i = read_file('day02/1.in').splitlines()
print(count_valid_passwords(i, is_valid_a), count_valid_passwords(i, is_valid_b))


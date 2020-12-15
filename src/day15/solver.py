from utils.file import read_file
import time


def star_a(numbers, target):
    all_spoken = {}
    for turn, number in enumerate(numbers, 1):
        all_spoken[number] = turn

    most_recently_spoken = numbers[-1]
    for turn in range(len(all_spoken), target):
        if most_recently_spoken not in all_spoken.keys():
            all_spoken[most_recently_spoken], most_recently_spoken = turn, 0
        else:
            all_spoken[most_recently_spoken], most_recently_spoken = turn, turn - all_spoken[most_recently_spoken]

    return most_recently_spoken


data = list(map(int, read_file('day15/1.in').split(',')))
start = time.time()
print(star_a(data, 2020), star_a(data, 30000000))
end = time.time()
print(end - start)

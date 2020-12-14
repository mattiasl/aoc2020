from utils.file import read_file


def star_a(notes):
    earliest = int(notes[0])
    departures = list(map(lambda x: int(x), filter(lambda y: y is not 'x', notes[1].split(','))))

    m = None
    departure = None
    for dep in departures:
        diff = dep - (earliest % dep)
        if not m or diff < m:
            m = diff
            departure = dep

    return m * departure


def star_b(notes):
    departures = list(map(lambda x: 0 if x is 'x' else int(x), notes[1].split(',')))

    departures_and_offsets = []
    tmp = 0
    for departure in range(len(departures)):
        dep = departures[departure]
        if dep != 0 and tmp > 0:
            departures_and_offsets.append(-tmp)
            tmp = 0
            departures_and_offsets.append(dep)
        elif dep == 0:
            tmp += 1
        else:
            departures_and_offsets.append(dep)

    print(departures_and_offsets)

    time, current_cycle = departures_and_offsets[0], departures_and_offsets[0]
    departure_offset = 1
    for departure in departures_and_offsets[1:]:
        # less than zero => offset and not a real departure
        if departure < 0:
            # offsets are negative: offset - (-offset)
            departure_offset -= departure
            continue

        while (time + departure_offset) % departure != 0:
            time += current_cycle

        current_cycle *= departure
        departure_offset += 1

    return time


data = read_file('day13/1.in').splitlines()
print(star_a(data), star_b(data))


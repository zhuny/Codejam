import collections


def get_int():
    return int(input())

def get_line():
    return input().strip()

def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def get_neighbor(pos, r, c):
    x, y = pos
    if x > 0:
        yield x-1, y
    if y > 0:
        yield x, y-1
    if x+1 < r:
        yield x+1, y
    if y+1 < c:
        yield x, y+1


def get_offices(plate):
    offices = set()
    for i, row in enumerate(plate):
        for j, val in enumerate(row):
            if val == '1':
                offices.add((i, j))
    return offices


def build_distance(offices, R, C):
    distance_map = {}
    distance = 0

    if len(offices) == 0:
        big = (R+C)*2
        for i in range(R):
            for j in range(C):
                distance_map[i, j] = big
        return distance_map

    while len(distance_map) < R*C:
        next_offices = set()
        for office in offices:
            distance_map[office] = distance
        for office in offices:
            for neighbor in get_neighbor(office, R, C):
                if neighbor not in distance_map:
                    next_offices.add(neighbor)
        offices = next_offices
        distance += 1

    return distance_map


def is_all_cover(distance, R, C, limit):
    not_reach = []
    for pos, dist in distance.items():
        if dist > limit:
            not_reach.append(pos)

    if len(not_reach) == 0:
        return True

    plus_val = [pos[0]+pos[1] for pos in not_reach]
    plus_val_max = max(plus_val)
    plus_val_min = min(plus_val)
    minus_val = [pos[0]-pos[1] for pos in not_reach]
    minus_val_max = max(minus_val)
    minus_val_min = min(minus_val)

    for pos in not_reach:
        dist = max(
            abs(plus_val_max-pos[0]-pos[1]),
            abs(plus_val_min-pos[0]-pos[1]),
            abs(minus_val_max-pos[0]+pos[1]),
            abs(minus_val_min-pos[0]+pos[1])
        )
        if dist <= limit:
            return True

    return False


def do_one_step():
    R, C = get_ints()
    plate = [get_line() for i in range(R)]

    offices = get_offices(plate)
    distance = build_distance(offices, R, C)

    if len(offices) == R*C:
        return 0
    if is_all_cover(distance, R, C, 1):
        return 1

    start = 1
    end = R+C

    while start+1 < end:
        middle = (start+end)//2
        if is_all_cover(distance, R, C, middle):
            end = middle
        else:
            start = middle

    return end


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


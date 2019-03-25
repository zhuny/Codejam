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


class KeyRange:
    def __init__(self, key):
        self.key_func = key
        self.key_map = collections.defaultdict(set)

    def add(self, value):
        key = self.key_func(value)
        self.key_map[key].add(value)

    def remove(self, value):
        key = self.key_func(value)
        self.key_map[key].discard(value)
        if len(self.key_map[key]) == 0:
            self.key_map.pop(key)

    def max_key(self):
        return max(self.key_map)

    def min_key(self):
        return min(self.key_map)


class RangeSet:
    def __init__(self):
        self.upper = KeyRange(lambda p: p[0]+p[1])
        self.lower = KeyRange(lambda p: p[0]-p[1])
        self.size = 0

    def add(self, pos):
        self.upper.add(pos)
        self.lower.add(pos)
        self.size += 1

    def remove(self, pos):
        self.upper.remove(pos)
        self.lower.remove(pos)
        self.size -= 1

    def total_range(self):
        if self.size <= 1:
            return 0

        upper_min = self.upper.min_key()
        upper_max = self.upper.max_key()
        lower_min = self.lower.min_key()
        lower_max = self.lower.max_key()
        upper_range = upper_max-upper_min
        lower_range = lower_max-lower_min

        offset = (max(upper_range, lower_range)+1)//2
        if upper_range % 2 == 0 and lower_range % 2 == 0:
            upper_mid = (upper_max+upper_min)//2
            lower_mid = (lower_max+lower_min)//2
            if upper_mid % 2 != lower_mid % 2:
                offset += 1
        return offset


def do_one_step():
    R, C = get_ints()
    plate = [get_line() for i in range(R)]

    offices = set()
    distance_remain = RangeSet()
    for r, row in enumerate(plate):
        for c, char in enumerate(row):
            pos = r, c
            if char == '1':
                offices.add(pos)
            else:
                distance_remain.add(pos)

    distance = 0
    offices_new = set(offices)
    while len(offices) < R*C and distance < distance_remain.total_range():
        next_new = set()
        for pos in offices_new:
            for neighbor in get_neighbor(pos, R, C):
                if neighbor not in offices:
                    distance_remain.remove(neighbor)
                    next_new.add(neighbor)
        offices_new = next_new
        offices.update(offices_new)
        distance += 1

    return distance


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


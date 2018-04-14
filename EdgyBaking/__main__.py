import math


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "Interval(%.6f, %.6f)"%(
            self.start,
            self.end
        )

    def __add__(self, other):
        return Interval(
            self.start+other.start,
            self.end+other.end
        )

    def __lt__(self, other):
        return self.start < other.start

    def is_intersect(self, rhs) -> bool:
        if isinstance(rhs, Interval):
            return (
                rhs.start <= self.end and
                self.start <= rhs.end
            )
        else:
            return (
                self.start <= rhs <= self.end
            )

    def union(self, rhs):
        self.start = min(self.start, rhs.start)
        self.end = max(self.end, rhs.end)


class RangeInterval:
    def __init__(self):
        self.interval = [Interval(0, 0)]

    def update(self, interval: Interval):
        self.interval.extend([
            already + interval
            for already in self.interval
        ])

        self.interval.sort()
        new_interval = []
        before = self.interval[0]
        for current in self.interval:
            if before.is_intersect(current):
                before.union(current)
            else:
                new_interval.append(before)
                before = current
        new_interval.append(before)
        self.interval = new_interval

    def left_most(self, number) -> float:
        left = 0
        for interval in self.interval:
            if interval.is_intersect(number):
                return number
            if interval.end < number:
                left = max(interval.end, left)
        return left


def do_one_step() -> float:
    N, P = get_ints()

    start = 0
    inc_sizes = RangeInterval()

    for i in range(N):
        W, H = get_ints()
        start += (W+H)*2
        size = Interval(min(W, H)*2, math.sqrt(W*W+H*H)*2)
        inc_sizes.update(size)

    return start+inc_sizes.left_most(P-start)


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %.7f"%(i, do_one_step()))


if __name__ == "__main__":
    main()



import itertools
import math
from fractions import Fraction


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def do_one_step_or_none_hard():
    n = get_int()
    pairs = [get_ints() for i in range(n)]

    BOUND = 1000
    min_valid = Fraction(1, BOUND)
    max_valid = Fraction(BOUND, 1)

    for p1, p2 in itertools.combinations(pairs, 2):
        d1 = p2[0]-p1[0]
        d2 = p2[1]-p1[1]

        if 0 <= d1 and 0 <= d2:
            continue
        elif d1 < 0 < d2:
            min_valid = max(min_valid, Fraction(d2, -d1))
        elif d2 < 0 < d1:
            max_valid = min(max_valid, Fraction(-d2, d1))
        else:
            return

        if max_valid <= min_valid:
            return

    for i in range(1, BOUND):
        m = min_valid*i
        v, r = divmod(m.numerator, m.denominator)
        v += 1
        if v < max_valid*i:
            return i, v

    # maybe unreachable


def is_sorted(l):
    n = len(l)
    for i in range(1, n):
        if l[i-1] >= l[i]:
            return False
    return True


def do_one_step_or_none():
    BOUND = 200

    n = get_int()
    pairs = [get_ints() for i in range(n)]

    for x in range(1, BOUND):
        for y in range(1, BOUND):
            pairs_weight = [
                px*x+py*y for px, py in pairs
            ]
            if is_sorted(pairs_weight):
                return x, y


def do_one_step():
    answer = do_one_step_or_none()
    if answer is None:
        return "IMPOSSIBLE"
    else:
        return "%s %s" % answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


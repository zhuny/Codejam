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


def max_fraction(num1, num2):
    if is_upper(num1, num2):
        return num2
    else:
        return num1


def min_fraction(num1, num2):
    if is_upper(num1, num2):
        return num1
    else:
        return num2


def is_upper(num1, num2):
    return num1[0]*num2[1] < num1[1]*num2[0]


def conti(my_list):
    before = None
    for e in my_list:
        if before is not None:
            yield before, e
        before = e


def normalize(a):
    d = math.gcd(*a)
    return a[0] // d, a[1] // d


def do_one_step_wrap():
    n = get_int()
    point_list = [get_ints() for i in range(n)]

    lower = 0, 1
    upper = 1, 0

    for p1, p2 in conti(point_list):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        if dx <= 0 and dy <= 0:
            return
        elif dx >= 0 and dy >= 0:
            continue
        elif dx > 0:
            upper = min_fraction(upper, (dx, -dy))
        else:
            lower = max_fraction(lower, (-dx, dy))

    if is_upper(lower, upper):
        lower = normalize(lower)
        upper = normalize(upper)

        for x in range(1, 200):
            p, r = divmod(x*lower[0], lower[1])
            if is_upper((p+1, x), upper):
                return x, p+1

        lower = Fraction(*lower)
        upper = Fraction(*upper)

        average: Fraction = (lower + upper) / 2
        limit = lower.denominator + upper.denominator + 1

        for c in closest(average, limit):
            if lower < c < upper:
                return c.denominator, c.numerator


def closest(frac: Fraction, limit: int):
    sim_list = []
    while limit > 150:
        sim = frac.limit_denominator(limit)
        sim_list.append(sim)
        limit = sim.denominator-1
    sim_list.reverse()
    return sim_list


def do_one_step():
    answer = do_one_step_wrap()
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

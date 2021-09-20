import itertools
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


def do_one_step():
    N = get_int()
    pairs = [get_ints() for i in range(N)]

    unique_swap = set()
    for p1, p2 in itertools.combinations(pairs, 2):
        if p1 > p2:
            p1, p2 = p2, p1

        if p1[0] < p2[0] and p1[1] > p2[1]:
            diff = Fraction(p1[1]-p2[1], p2[0]-p1[0])
            unique_swap.add(diff)

    return len(unique_swap)+1


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


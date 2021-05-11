import itertools


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def far_from(start, end):
    return end is None or start+1 < end


def get_middle(start, end):
    if end is None:
        if start == 0:
            return 1
        else:
            return start * 2
    else:
        return (start + end) // 2


def con_sum(a, b):
    return (a + b) * (b - a + 1) // 2


def all_one(n):
    if n == 0:
        return 0

    start, end = 1, None
    while far_from(start, end):
        middle = get_middle(start, end)
        if con_sum(1, middle) <= n:
            start = middle
        else:
            end = middle

    return start


def con_sum2(a, b):
    if a > b:
        return 0
    if (b - a) % 2 == 1:
        b -= 1
    return (a + b) * (b - a + 2) // 4


def travel(l, r, i):
    start, end = 0, None
    while far_from(start, end):
        middle = get_middle(start, end)
        ll = l - con_sum2(i, i+middle-1)
        rr = r - con_sum2(i+1, i+middle-1)
        if ll < 0 or rr < 0:
            end = middle
        else:
            start = middle

    ii = i+start-1
    return l - con_sum2(i, ii), r - con_sum2(i+1, ii), ii


def do_one_step():
    L, R = get_ints()

    i = all_one(abs(L-R))
    if L > R:
        L -= con_sum(1, i)
    else:
        R -= con_sum(1, i)

    i += 1
    if L >= R:
        L, R, i = travel(L, R, i)
    else:
        R, L, i = travel(R, L, i)

    return f"{i} {L} {R}"


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()

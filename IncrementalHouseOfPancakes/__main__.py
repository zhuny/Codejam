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
        return start * 2
    else:
        return (start + end) // 2


def get_first(n):
    if n == 0:
        return 0

    start, end = 1, None
    while far_from(start, end):
        middle = get_middle(start, end)
        if middle * (middle+1) <= n*2:
            start = middle
        else:
            end = middle

    return start


def do_one_step():
    L, R = get_ints()

    for i in itertools.count(1):
        if L < i and R < i:
            return "%s %s %s" % (i-1, L, R)
        if L >= R:
            L -= i
        else:
            R -= i


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()

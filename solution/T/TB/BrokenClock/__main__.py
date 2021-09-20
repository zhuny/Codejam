import collections
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


def div(x, y, m):
    return (x * pow(y, m*8//30 - 1, m)) % m


def try_to_answer(h, m, s):
    M = 12 * 60 * 60 * (10 ** 9)
    x1 = div(m-h, 11, M)
    x2 = div(s-h, 719, M)
    if x1 == x2:
        return x1


def form_to_time(t):
    t, n = divmod(t, 10**9)
    t, s = divmod(t, 60)
    h, m = divmod(t, 60)
    return h, m, s, n


def do_one_step():
    clock = get_ints()

    for I in itertools.permutations(clock):
        answer = try_to_answer(*I)
        if answer is not None:
            return " ".join(map(str, form_to_time(answer)))


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


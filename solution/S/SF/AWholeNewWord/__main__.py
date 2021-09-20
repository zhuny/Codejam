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


def do_one_step():
    N, L = get_ints()

    words = [
        get_line()
        for i in range(N)
    ]

    word_set = set(words)
    pos_sets = [
        set()
        for i in range(L)
    ]
    for word in words:
        for i, char in enumerate(word):
            pos_sets[i].add(char)

    pos_sets = [list(s) for s in pos_sets]

    for chars in itertools.product(*pos_sets):
        word = "".join(chars)
        if word not in word_set:
            return word

    return '-'


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


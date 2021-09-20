def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [int(i) for i in input().split()]


def get_pos(seq, pos):
    return seq[pos % len(seq)]


def get_pos_all(seqs, pos):
    return [get_pos(seq, pos) for seq in seqs]


def get_better2(possible):
    if "R" not in possible:
        return "S"
    if "P" not in possible:
        return "R"
    if "S" not in possible:
        return "P"


def get_better1(possible):
    if "R" in possible:
        return "P"
    if "P" in possible:
        return "S"
    if "S" in possible:
        return "R"


def do_one_step():
    n = get_int()
    seqs = [get_line() for i in range(n)]
    choose = []
    while seqs and len(choose) < 500:
        i = len(choose)
        whole = set(get_pos_all(seqs, i))
        if len(whole) == 3:
            return "IMPOSSIBLE"
        elif len(whole) == 2:
            better = get_better2(whole)
        elif len(whole) == 1:
            better = get_better1(whole)
        else:
            return "IMPOSSIBLE"

        seqs = [
            seq
            for seq in seqs
            if get_pos(seq, i) == better
        ]
        choose.append(better)

    return "".join(choose)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


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


def group_by_rank(cards):
    d = collections.defaultdict(list)
    for i, card in enumerate(cards):
        d[card[0]].append(i)
    return d


def group_conseq(pos):
    result = collections.defaultdict(list)
    for i, p in enumerate(pos):
        result[p-i].append(p)
    for i, p in sorted(result.items()):
        yield p[0], p[-1]


def action_move(cards, pos):
    g = []
    l = []

    scan = 0
    for start, end in pos:
        g.append(cards[scan:start])
        l.extend(cards[start:end+1])
        scan = end+1

    f_start, f_end = pos[0]
    for s_start, s_end in pos[1:]:
        yield f_end+1, s_start-f_end-1
        f_start, f_end = s_start, s_end

    ge = [e for g_ in reversed(g) for e in g_]
    assert len(cards) == len(ge) + len(l)
    cards[:] = ge + l


def remove_max_rank(cards, max_rank):
    while cards and cards[-1][0] == max_rank:
        cards.pop()


def do_one_step():
    R, S = get_ints()
    cards = [(r, s) for s in range(S) for r in range(R)]
    seq = []

    while cards:
        rank_pos = group_by_rank(cards)
        assert len(cards) <= R*S
        max_rank = max(rank_pos)
        seq.extend(action_move(cards, list(group_conseq(rank_pos[max_rank]))))
        assert len(cards) <= R*S
        remove_max_rank(cards, max_rank)
        assert len(cards) <= R*S

    assert len(seq) == (R-1)*(S-1)
    print(len(seq))
    for a, b in seq:
        print(a, b)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: " % i, end="")
        do_one_step()


if __name__ == "__main__":
    main()


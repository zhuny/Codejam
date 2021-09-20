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


def do_one_step():
    N, K = get_ints()
    position = get_ints()
    color = get_ints()

    group = collections.defaultdict(list)
    for i in range(N):
        group[color[i]].append(position[i])
    for v in group.values():
        v.sort()

    INFTY = sum(position)*2
    bilength = [(0, 0)]  # List of <uni, bi>
    for v in group.values():
        i = len(bilength)-1
        while i >= 0:
            many = bilength[i]
            for j, more in enumerate(v, 1):
                ij = i+j
                if ij <= K:
                    while len(bilength) <= ij:
                        bilength.append((INFTY, INFTY))
                    bilength[ij] = (
                        min(many[0]+more*2, many[1]+more, bilength[ij][0]),
                        min(many[1]+more*2, bilength[ij][1])
                    )
            i -= 1

    return bilength[-1][0]


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


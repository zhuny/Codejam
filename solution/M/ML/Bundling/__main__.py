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


def get_group(words, i):
    g = collections.defaultdict(list)
    for word in words:
        if len(word) > i:
            char = word[i]
        else:
            char = ""
        g[char].append(word)

    return g


def do_one_step():
    N, K = get_ints()

    q = [([get_line() for i in range(N)], 0)]
    score = 0

    while q:
        lines, index = q.pop()
        g = get_group(lines, index)
        for char, line_group in g.items():
            if char and len(line_group) >= K:
                score += len(line_group) // K
                q.append([line_group, index+1])

    return score


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


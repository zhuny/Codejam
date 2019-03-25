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
    N, P = get_ints()
    players = get_ints()
    players.sort()

    befores = []
    before_total = 0
    min_valid = []

    for player in players:
        if len(befores) == P:
            before_total -= befores[0]
            befores.pop(0)
        befores.append(player)
        before_total += player
        if len(befores) == P:
            min_valid.append(player*P-before_total)

    return min(min_valid)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


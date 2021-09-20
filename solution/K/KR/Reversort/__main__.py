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
    n = get_int()
    l = get_ints()

    cost = 0
    for i in range(n-1):
        j = min(range(i, n), key=lambda e: l[e])
        cost += j-i+1
        l[i:j+1] = l[i:j+1][::-1]

    return cost


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


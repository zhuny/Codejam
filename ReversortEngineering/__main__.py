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
    n, c = get_ints()

    if n <= c+1 <= (n*(n+1)//2):
        c -= n-1
        i = n-1
        l = []
        while i > 0:
            if c >= i:
                l.append(i)
                c -= i
            i -= 1

        l.extend([0] * (n-1-len(l)))
        l = [j+1 for j in l]

        l.reverse()
        result = list(range(1, n+1))

        for s, w in enumerate(l, 2):
            start = n-s
            end = start+w
            result[start:end] = result[start:end][::-1]

        return " ".join(map(str, result))

    else:
        return "IMPOSSIBLE"


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


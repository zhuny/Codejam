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
    X, Y, M = get_line().split()
    X, Y = int(X), int(Y)

    for i, char in enumerate(M, 1):
        if char == "N":
            Y += 1
        elif char == "S":
            Y -= 1
        elif char == "E":
            X += 1
        elif char == "W":
            X -= 1

        if abs(X) + abs(Y) <= i:
            return i

    return "IMPOSSIBLE"


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


def get_int():
    return int(input())


def load_info():
    X, Y, symbol = input().split()
    return int(X), int(Y), symbol


def edge_min_cost(x, y, width, char):
    if char == 'J':
        x, y = y, x
    min_cost = 0
    cost = 0
    for i in range(1, width):
        cost += x
        min_cost = min(cost, min_cost)
        x, y = y, x
    return min_cost


def middle_min_cost(x, y, width, start, end):
    if start == end:
        return min(0, (x+y)*(width >> 1))
    else:
        if end == 'C':
            x, y = y, x

        return min(x, x + (x+y) * (width >> 2))


def do_one_step():
    x, y, symbol = load_info()

    before = -1
    before_char = None
    min_cost = 0

    for i, char in enumerate(symbol):
        if char == '?':
            continue

        if before_char is None:
            min_cost += edge_min_cost(x, y, i - before, char)
        else:
            min_cost += middle_min_cost(x, y, i-before, before_char, char)

        before, before_char = i, char

    min_cost += edge_min_cost(y, x, len(symbol)-before, before_char)

    return min_cost


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


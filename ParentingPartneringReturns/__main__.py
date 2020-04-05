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
    N = get_int()
    event = []

    for i in range(N):
        start, end = get_ints()
        event.append((start, 1, i))
        event.append((end, 0, i))

    event.sort()

    assign = [""] * N
    children = set("CJ")

    for time, state, task in event:
        if state == 0:
            children.add(assign[task])
        elif len(children) == 0:
            return "IMPOSSIBLE"
        else:
            assign[task] = children.pop()

    return "".join(assign)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


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
    path = get_line()
    if len(path) != (N-1)*2:
        return ""

    my_path = [
        'S' if p == 'E' else 'E'
        for p in path
    ]
    return "".join(my_path)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


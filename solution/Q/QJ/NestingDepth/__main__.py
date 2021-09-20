def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def move_pan(source, target):
    if source < target:
        return "(" * (target-source)
    elif target < source:
        return ")" * (source-target)
    else:
        return ""


def do_one_step():
    stream = []
    current = 0

    for char in get_line():
        stream.append(move_pan(current, int(char)))
        stream.append(char)
        current = int(char)
    stream.append(move_pan(current, 0))

    return "".join(stream)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


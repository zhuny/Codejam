def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def is_invalid(p1, p2):
    return (
        p1[0] == p2[0] or
        p1[1] == p2[1] or
        p1[0]+p1[1] == p2[0]+p2[1] or
        p1[0]-p1[1] == p2[0]-p2[1]
    )


def travel_path(vs, path):
    if len(vs) == 0:
        return True

    for v in list(vs):
        if path and is_invalid(path[-1], v):
            pass
        else:
            vs.remove(v)
            path.append(v)
            if travel_path(vs, path):
                return True
            path.pop()
            vs.add(v)
    return False


def get_path(R, C):
    s = set([
        (r, c)
        for r in range(1, R + 1)
        for c in range(1, C + 1)
    ])
    path = []
    travel_path(s, path)
    return path


def do_one_step():
    R, C = get_ints()
    path = get_path(R, C)
    stream = []
    if len(path) == R*C:
        stream.append("POSSIBLE")
        for p in path:
            stream.append("%s %s" % p)
    else:
        stream.append("IMPOSSIBLE")

    return "\n".join(stream)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


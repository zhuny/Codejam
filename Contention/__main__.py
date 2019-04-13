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
    N, Q = get_ints()
    lines = [get_ints() for i in range(Q)]

    line_queue = []
    for index, line in enumerate(lines):
        line_queue.append((line[0], True, index))
        line_queue.append((line[1]+1, False, index))
    line_queue.sort()

    many_overlap = set()
    scan = -1
    only_valid = {i: 0 for i in range(Q)}

    for pos, state, custom in line_queue:
        print(scan, pos, state, custom, many_overlap, only_valid)
        if scan < pos:
            if len(many_overlap) == 1:
                for ticket in many_overlap:
                    only_valid[ticket] += pos-scan
            scan = pos

        if state:
            many_overlap.add(custom)
        else:
            many_overlap.remove(custom)

    return min(only_valid.values())


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


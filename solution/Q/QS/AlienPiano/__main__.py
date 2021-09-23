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

    prev_node = None
    prev_direct = None
    prev_count = 0
    answer = 0

    for current_node in get_ints():
        if prev_node is not None and prev_node != current_node:
            current_direct = (current_node > prev_node)
            if prev_direct is None or prev_direct != current_direct:
                prev_direct = current_direct
                prev_count = 1
            else:
                prev_count += 1
            if prev_count == 4:
                answer += 1
                prev_direct = None
        prev_node = current_node

    return answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


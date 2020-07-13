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
    value = get_ints()
    high_record = -1
    is_prev_high = False
    answer = 0

    for v in value:
        if is_prev_high:
            if high_record > v:
                answer += 1
        if high_record < v:
            high_record = v
            is_prev_high = True
        else:
            is_prev_high = False

    if is_prev_high:
        answer += 1

    return answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


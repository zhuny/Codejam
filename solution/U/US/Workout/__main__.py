def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def diff_far(start, end):
    return (
        end is None or
        end - start > 1
    )


def get_middle(start, end):
    if end is None:
        return start*2
    else:
        return (start+end) // 2


def get_needed(nums, diff):
    i = 0
    for n1, n2 in zip(nums[:-1], nums[1:]):
        i += (n2-n1-1) // diff
    return i


def do_one_step():
    N, K = get_ints()
    Ms = get_ints()

    if get_needed(Ms, 1) <= K:
        return 1

    start, end = 1, None
    while diff_far(start, end):
        middle = get_middle(start, end)
        if get_needed(Ms, middle) <= K:
            end = middle
        else:
            start = middle

    return end


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


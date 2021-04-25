import collections


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def is_valid(a, b, needed, start):
    made_from = collections.defaultdict(int, {start: 1})
    needed_dict = collections.defaultdict(int, enumerate(needed))

    top = start

    # print(f"Loop from {start}")
    while top >= 0:
        # print(made_from, needed_dict)
        top_current = made_from.pop(top, 0)
        if top_current >= needed_dict[top]:
            top_current -= needed_dict[top]
            needed_dict[top] = 0
            made_from[top-a] += top_current
            made_from[top-b] += top_current
        else:
            return False
        top -= 1

    return sum(needed_dict.values()) == 0


def so_far(a, b):
    return b is None or a+1 < b


def middle(a, b):
    if b is None:
        return a*2
    else:
        return (a+b) // 2


def do_one_step():
    n, a, b = get_ints()
    needed = get_ints()

    left = 1
    right = None
    while so_far(left, right):
        mid = middle(left, right)
        if mid > 100_000:
            return "IMPOSSIBLE"
        if is_valid(a, b, needed, mid):
            right = mid
        else:
            left = mid

    return right+1


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


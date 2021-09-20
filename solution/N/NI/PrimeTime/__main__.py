import heapq


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def is_far(left, right):
    return right is None or left + 1 < right


def middle(left, right):
    if right is None:
        if left == 0:
            return 1
        else:
            return left * 2
    else:
        return (right + left) >> 1


def min_make_sum(count, numbers):
    return make_sum(count, numbers, False)


def max_make_sum(count, numbers):
    return make_sum(count, numbers, True)


def make_sum(count, numbers, reverse):
    sum_num = 0
    prod_num = 1

    for p, e in sorted(numbers, reverse=reverse):
        used = min(count, e)
        sum_num += used*p
        prod_num *= pow(p, used)
        count -= used
        if count == 0:
            break

    return sum_num + prod_num


def find_sum(count, numbers, target):
    pass


def do_one_step():
    m = get_int()
    numbers = [get_ints() for i in range(m)]

    target = sum(x*y for x, y in numbers)

    heap = []

    for i, pair in enumerate(numbers):
        x = pair[0]
        current = [0] * len(numbers)
        current[i] = 1
        heapq.heappush(
            heap,
            (2*x, x, x, x, current)
        )

    while heap:
        t, sn, pn, max_p, v = heapq.heappop(heap)
        if t == target:
            return pn
        elif target < t:
            return 0

        for i, pair in enumerate(numbers):
            if max_p <= pair[0] and v[i] < pair[1]:
                next_list = list(v)
                next_list[i] += 1
                new_sn = sn + pair[0]
                new_pn = pn * pair[0]
                if new_sn + new_pn <= target:
                    heapq.heappush(
                        heap,
                        (new_sn+new_pn, new_sn, new_pn, pair[0], next_list)
                    )
    return 0


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


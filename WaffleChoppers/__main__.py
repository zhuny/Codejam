import collections


def sum_list(it):
    i = 0
    yield i
    for j in it:
        i += j
        yield i


def divide_list(it, div):
    S = sum(it)
    if S%(div+1) != 0:
        return

    count = S//(div+1)
    div_bound = [None for _ in range(div+2)]
    div_bound[-1] = len(it)

    for i, val in enumerate(sum_list(it)):
        if val % count == 0:
            div_bound[val//count] = i

    if None in div_bound:
        return

    return div_bound


def do_one_step():
    R, C, H, V = get_ints()

    r_count = [0 for _ in range(R)]
    c_count = [0 for _ in range(C)]
    p_count = collections.defaultdict(int)

    for i in range(R):
        for j, char in enumerate(get_line()):
            if char == "@":
                r_count[i] += 1
                c_count[j] += 1
                p_count[i, j] = 1

    S = sum(r_count)

    if S == 0:
        return True

    if S % ((H+1)*(V+1)) != 0:
        return False

    h_div = divide_list(r_count, H)
    c_div = divide_list(c_count, V)

    if h_div is None or c_div is None:
        return False

    check = S // (H+1) // (V+1)
    for h_st, h_en in get_conti(h_div):
        for c_st, c_en in get_conti(c_div):
            check_value = 0
            for i in range(h_st, h_en):
                for j in range(c_st, c_en):
                    check_value += p_count[i, j]
            if check_value != check:
                return False

    return True


def get_conti(it):
    yield from zip(it[:-1], it[1:])


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s:"%i, end=" ")
        if do_one_step():
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")


if __name__ == "__main__":
    main()


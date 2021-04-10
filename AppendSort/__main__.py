def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def length(number):
    return len(str(number))


def all_nine(number_str):
    for char in number_str:
        if char != '9':
            return False
    return True


def append_number(prev, current):
    if prev < current:
        return current, 0

    prev_cut = int(str(prev)[:length(current)])
    extend = length(prev) - length(current)
    if prev_cut < current:
        return current * (10 ** extend), extend
    elif prev_cut == current and not all_nine(str(prev)[length(current):]):
        return prev+1, extend
    else:
        return current * (10 ** (extend+1)), extend+1


def do_one_step():
    n = get_int()

    prev = None
    count = 0
    for x in get_ints():
        if prev is None:
            prev = x
        else:
            nex, appended = append_number(prev, x)
            prev = nex
            count += appended

    return count


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()

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
    prev = ""
    count = 0
    answer_list = []

    n = get_int()
    for char in get_line():
        if prev < char:
            count += 1
        else:
            count = 1
        prev = char
        answer_list.append(count)

    return " ".join(map(str, answer_list))


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


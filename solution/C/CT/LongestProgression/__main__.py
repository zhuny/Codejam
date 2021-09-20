def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def match(num_list, a, b, i):
    return num_list[i] == a*i + b


def travel(num_list, a, b, i):
    while i < len(num_list) and match(num_list, a, b, i):
        i += 1
    return i-1


def do_one_step():
    n = get_int()
    num_list = get_ints()

    return max(
        do_one_list(n, num_list),
        do_one_list(n, list(reversed(num_list)))
    )


def do_one_list(n, num_list):
    i = 1
    answer = min(3, n)
    while i < n:
        a = num_list[i] - num_list[i-1]
        b = num_list[i] - a*i

        j = travel(num_list, a, b, i)
        if j+2 < n and match(num_list, a, b, j+2):
            k = travel(num_list, a, b, j+2)
            answer = max(answer, k-i+2)
        else:
            answer = max(answer, min(n, j+2)-i+1)
        i = j+1

    return answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


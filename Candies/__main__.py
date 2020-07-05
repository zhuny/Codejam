def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def alter_sum(A):
    new_list = []
    alter = 0
    for i in reversed(A):
        alter = i-alter
        new_list.append(alter)
    new_list.reverse()
    return new_list


def alter_twice(A):
    A1 = alter_sum(A)
    A2 = alter_sum(A1)
    A1.append(0)
    A2.append(0)
    return A1, A2


def sign(index):
    if index % 2 == 0:
        return 1
    else:
        return -1


def do_one_step():
    N, Q = get_ints()
    A = get_ints()

    A1, A2 = alter_twice(A)

    query_result = 0

    for i in range(Q):
        command, start, end = get_line().split()
        start, end = int(start), int(end)

        if command == "U":
            A[start-1] = end
            A1, A2 = alter_twice(A)

        elif command == "Q":
            start -= 1
            left_far = A2[end] + A1[end] * (end-start)
            query_result += A2[start] - left_far * sign(start-end)

    return query_result


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


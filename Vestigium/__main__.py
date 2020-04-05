def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def is_duplicate(row):
    check = set()
    for e in row:
        if e in check:
            return True
        check.add(e)
    return False


def transpose(matrix):
    return list(zip(*matrix))


def do_one_step():
    N = get_int()
    matrix = [
        get_ints() for i in range(N)
    ]

    trace = 0
    for i in range(N):
        trace += matrix[i][i]

    row_count = len(list(filter(is_duplicate, matrix)))
    col_count = len(list(filter(is_duplicate, transpose(matrix))))

    return "%s %s %s" % (
        trace,
        row_count,
        col_count
    )


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


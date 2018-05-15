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


def do_one_step():
    N = get_int()
    weights = get_ints()

    length2index = [0]

    for weight in weights:
        N = len(length2index)
        if length2index[-1] <= weight*6:
            length2index.append(length2index[-1]+weight)

        for index in reversed(range(N-1)):
            if length2index[index] <= weight*6:
                length2index[index+1] = min(
                    length2index[index+1],
                    length2index[index] + weight
                )

    return len(length2index)-1


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


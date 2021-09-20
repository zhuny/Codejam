def get_int():
    return int(input())

def get_line():
    return input().strip()

def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def to_int(num_seq):
    i = 0
    for num in num_seq[::-1]:
        i = i*10+num
    return i


def do_one_step():
    N = get_int()
    first = []
    second = []
    while N > 0:
        N, last = divmod(N, 10)
        if last == 4:
            nn = N % 3
            first.append(1+nn)
            second.append(3-nn)
        else:
            if N % 2 == 0:
                first.append(last)
                second.append(0)
            else:
                first.append(0)
                second.append(last)
    return "{} {}".format(to_int(first), to_int(second))


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


def do_one_step():
    length = get_int()
    L = get_ints()

    L1 = L[::2]
    L1.sort()
    L[::2] = L1

    L2 = L[1::2]
    L2.sort()
    L[1::2] = L2

    for i,e in enumerate(L[:-1]):
        if e > L[i+1]:
            print(i)
            break
    else:
        print("OK")


def get_int():
    return int(input())


def get_line():
    return input().split()


def get_ints():
    return [
        int(i)
        for i in get_line()
    ]


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s:"%i, end=" ")
        do_one_step()


if __name__ == "__main__":
    main()


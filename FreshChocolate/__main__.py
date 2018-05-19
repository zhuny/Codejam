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
    N, P = get_ints()
    Gs = collections.Counter([
        g%P for g in get_ints()
    ])
    count = Gs.pop(0, 0)

    if P == 2:
        count += Gs[1]//2
        Gs[1] %= 2
        if Gs[1] == 1:
            count += 1

    elif P == 3:
        A = Gs[1]
        B = Gs[2]

        if abs(A-B)%3 == 2:
            count11 = max(min(A, B)-1, 0)
        else:
            count11 = min(A, B)

        count += count11
        for i in range(1, 3):
            Gs[i] -= count11
            count += Gs[i]//3
            Gs[i] %= 3

        if Gs[1]+Gs[2] > 0:
            count += 1

    return count


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


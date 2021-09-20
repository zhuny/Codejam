def get_int():
    return int(input())

def get_line():
    return input().strip()

def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def get_limit(n):
    for i in range(100):
        if i*(i+1)//2 > n:
            return i


def do_one_step():
    R, B = get_ints()

    count = {}
    count[0, 0] = 0

    r_limit = get_limit(R)
    b_limit = get_limit(B)

    for r1 in range(r_limit+1):
        for b1 in range(b_limit+1):
            if r1+b1 == 0:
                continue

            count_new = {}
            for I, v in count.items():
                r2, b2 = I
                r3, b3 = r1+r2, b1+b2
                if r3 <= R and b3 <= B:
                    count_new[r3, b3] = v+1
            for I, v in count_new.items():
                if I in count:
                    count[I] = max(count[I], v)
                else:
                    count[I] = v

    return count[R, B]


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()
    # v 1.1


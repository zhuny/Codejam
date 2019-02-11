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
    N, L = get_ints()
    C = get_ints()

    befores_need = {}
    upper_half = [0]
    for i in range(1, N):
        p, q = divmod(100*i, N)
        if q*2 >= N:
            for num in upper_half:
                befores_need[num] = i-num
            upper_half = []
        else:
            upper_half.append(i)

    def needed(n):
        return befores_need.get(n, 0)

    befores_need.setdefault(0, 1)

    C.sort(key=needed, reverse=True)

    final = []

    left = N - sum(C)
    while left > 0:
        if C:
            n = needed(C[-1])
            if n <= left:
                left -= n
                final.append(C[-1]+n)
                C.pop()
            else:
                final.extend(C)
                C = []
        else:
            n = needed(0)
            if n <= left:
                left -= n
                final.append(n)
            else:
                final.append(left)
                left = 0
    final.extend(C)

    final_per = []

    for i in final:
        p, q = divmod(100*i, N)
        if q*2 >= N:
            final_per.append(p+1)
        else:
            final_per.append(p)

    print(final)
    return sum(final_per)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


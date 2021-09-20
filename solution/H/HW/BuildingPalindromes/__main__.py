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
    N, Q = get_ints()
    line = get_line()
    alpha_counter = {
        chr(alpha): [0]*(N+1)
        for alpha in range(ord('A'), ord('Z')+1)
    }
    for index, alpha in enumerate(line, 1):
        alpha_counter[alpha][index] = 1
    for counter in alpha_counter.values():
        for index in range(N):
            counter[index+1] += counter[index]
    answer = 0
    for _ in range(Q):
        start, end = get_ints()
        start -= 1
        odd_count = 0
        for counter in alpha_counter.values():
            if (counter[end]-counter[start])%2 == 1:
                odd_count += 1
        if odd_count <= 1:
            answer += 1
    return answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()



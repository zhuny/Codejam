def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def do_one_step():
    N, L = get_ints()

    crypto = get_ints()
    plain = [0]*(L+1)

    for i in range(L-1):
        if crypto[i] != crypto[i+1]:
            plain[i+1] = gcd(crypto[i], crypto[i+1])
            for j in range(i, -1, -1):
                plain[j] = crypto[j]//plain[j+1]
            for j in range(i+1, L):
                plain[j+1] = crypto[j]//plain[j]
            break

    primes = list(set(plain))
    primes.sort()
    assert 0 not in primes
    assert len(primes) == 26

    primes_map = {
        prime: chr(ord('A')+i)
        for i, prime in enumerate(primes)
    }
    return "".join([
        primes_map[num]
        for num in plain
    ])


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def prime(n):
    prime_list = list(range(2, n + 1))
    for i in range(2, n):
        if i * i > n:
            break
        prime_list = [
            p
            for p in prime_list
            if p <= i or i % p != 0
        ]
    return prime_list


def factorization(num, primes):
    f = []
    for p in primes:
        if num == 1:
            break
        po = 0
        while num % p == 0:
            num //= p
            po += 1
        if po > 0:
            f.append((p, po))
    if num == 1:
        return f
    else:
        return []


def valid_factor(factor, pair_dict):
    for p, e in factor:
        if pair_dict.get(p, 0) < e:
            return False
    return True


def do_one_step():
    n = get_int()
    pairs = [get_ints() for i in range(n)]
    pair_dict = dict(pairs)

    pair_sum = sum(x * y for x, y in pairs)
    used_prime = set(x for x, y in pairs)
    primes = [p for p in prime(500) if p in used_prime]

    for num in range(pair_sum, max(pair_sum - 30000, 0), -1):
        factor = factorization(num, primes)
        if len(factor) == 0:
            continue

        factor_sum = sum(x * y for x, y in factor)
        if valid_factor(factor, pair_dict) and num + factor_sum == pair_sum:
            return num

    return 0


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


import sys


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def do_one_step(n, m):
    primes = [12, 5, 7, 11, 13, 17]

    valids = list(range(m))
    valids.reverse()

    for prime in primes:
        num = [prime]*18
        print(*num)
        sys.stdout.flush()
        numbers = sum(get_ints()) % prime
        valids = [
            num for num in valids
            if num % prime == numbers
        ]

    print(valids[0])
    sys.stdout.flush()
    get_ints()


def main():
    t, n, m = get_ints()
    for i in range(1, t+1):
        do_one_step(n, m)


if __name__ == "__main__":
    main()


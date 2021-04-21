def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def sqrt(n):
    x = n // 2
    for i in range(100):
        x = (x*x + n) // (x*2)
    if x*x <= n:
        return x
    else:
        return x-1


def upper(n):
    while True:
        if is_prime(n):
            return n
        n += 1


def lower(n):
    while True:
        if is_prime(n):
            return n
        n -= 1


def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, n, 2):
        if n < i*i:
            break
        if n % i == 0:
            return False
    return True


def do_one_step():
    z = get_int()
    n = sqrt(z)
    n_up = upper(n+1)
    n_down1 = lower(n)
    n_down2 = lower(n_down1-1)

    if n_down1*n_up <= z:
        return n_down1*n_up
    else:
        return n_down1*n_down2


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


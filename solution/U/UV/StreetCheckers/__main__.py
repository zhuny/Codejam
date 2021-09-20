def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class Prime:
    _list = [2, 3, 5, 7, 11, 13]

    @classmethod
    def is_prime(cls, number):
        for p in cls.scan_prime():
            if number % p == 0:
                return False
            if number <= p*p:
                break
        return True

    @classmethod
    def scan_prime(cls):
        yield from cls._list
        last = cls._list[-1]+2

        while True:
            if cls.is_prime(last):
                yield last
                cls._list.append(last)
            last += 2


def is_interesting(number):
    two = 0
    while number % 2 == 0:
        number >>= 1
        two += 1

    if two == 1:
        return True
    elif two > 3:
        return False
    elif two == 3:
        return number == 1
    else:
        return number == 1 or Prime.is_prime(number)


def do_one_step():
    L, R = get_ints()
    count = 0
    for num in range(L, R+1):
        if is_interesting(num):
            count += 1
    return count


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


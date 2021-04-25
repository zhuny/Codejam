import functools
import math
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


def check(digit, size, position_info):
    multiplier, p, index = position_info
    return abs(math.pow(10, size * digit / 9) - multiplier)
    # return abs(p*9 / size - digit)


def do_one_step(number, size):
    # valid_position : List of tuple
    #   - current number multiplier
    #   - 10 to the this is multiplier
    #   - what position block
    valid_position = [(1, 1, index+1) for index in range(number)]

    for _ in range(number*size):
        digit = get_int()
        valid_position.sort()

        min_info = multiplier, p, index = min(
            valid_position,
            key=functools.partial(check, digit, size)
        )
        valid_position.remove(min_info)
        print(index)
        sys.stdout.flush()
        if p < size:
            valid_position.append((multiplier*10, p+1, index))


def main():
    t, n, b, p = get_ints()
    for i in range(t):
        do_one_step(n, b)

    is_correct = get_int()
    # is_correct should be ONE!!


if __name__ == "__main__":
    main()

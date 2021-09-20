import collections
import itertools
from typing import List


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def get_shortage(remains):
    for i, v in enumerate(remains):
        if v < 0:
            return i
    return -1


def is_valid(count, recipe, remains):
    remains = remains[:]
    remains[0] -= count
    recipe = {
        i: v.copy()
        for i, v in recipe.items()
    }

    while True:
        i = get_shortage(remains)
        if i == -1:
            return True
        d = remains[i]
        r = recipe.pop(i)

        if i in r:
            return False

        remains[i] = 0
        for k, v in r.items():
            remains[k] += v*d

        for k1, v1 in recipe.items():
            if i in v1:
                d1 = v1.pop(i)
                for k, v in r.items():
                    v1[k] = v1.get(k, 0)+v*d1


def do_one_step():
    M = get_int()
    recipe = {
        i : {v-1: 1 for v in get_ints()}
        for i in range(M)
    }
    remains = get_ints()
    end = sum(remains)+3
    start = 0

    while start+1 < end:
        mid = (end+start)//2
        if is_valid(mid, recipe, remains):
            start = mid
        else:
            end = mid

    return start


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #{}: {}".format(i, do_one_step()))


if __name__ == "__main__":
    main()


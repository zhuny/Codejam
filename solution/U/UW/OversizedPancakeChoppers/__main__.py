import bisect
import collections
import time
from fractions import Fraction
from math import gcd


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class CakeSize:
    def __init__(self):
        self.body = []
        self.up = []
        self.sorted = False

    def update(self, count, limit):
        self.body.append(count)
        self.sorted = False

    def check_sort(self):
        if self.sorted:
            return
        self.sorted = True

        self.body.sort()
        self.up = []
        s = 0
        for i in self.body:
            s += i
            self.up.append(s)

    def valid(self, count):
        self.check_sort()

        profit = bisect.bisect_right(self.up, count)
        if len(self.up) == profit:
            return self.up[-1]-profit, count-self.up[-1]
        else:
            return count-profit, 0


def has_left(int_list, target, left, limit):
    index = bisect.bisect_left(int_list, target)
    while index < len(int_list) and left > 0:
        div = int_list[index] / target
        if div.denominator > 1 or int_list[index] > target*limit:
            left -= int(div)
        index += 1
    return left <= 0


def do_one_step():
    N, D = get_ints()
    Ai = get_ints()
    Ai.sort()

    target_container = collections.defaultdict(CakeSize)

    for a in Ai:
        for i in range(1, D+1):
            g = gcd(a, i)
            f = a // g, i // g
            # Fraction hash가 오래 걸린다.
            target_container[f].update(i, D)

    answer = D-1

    for target, container in target_container.items():
        cut, left = container.valid(D)
        # print(target, vars(container), cut, left)
        if has_left(Ai, Fraction(*target), left, D):
            answer = min(answer, cut+left)

    return answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


import itertools
from fractions import Fraction


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class BinarySearch:
    def __init__(self):
        self.sorted_list = []
        self.unsorted = []

    def upper(self, p):
        yield from self._upper_sorted(p)
        yield from self._upper_unsorted(p)

    def _upper_sorted(self, p2):
        for p1 in self.sorted_list:
            if p1[1] > p2[1]:
                yield p1
            else:
                break

    def _upper_unsorted(self, p2):
        for p1 in self.unsorted:
            if p1[1] > p2[1]:
                yield p1

    def insert(self, p):
        self.unsorted.append(p)
        if len(self.unsorted) > 15:
            self.sorted_list.extend(self.unsorted)
            self.sorted_list.sort(key=lambda p1: p1[1], reverse=True)
            self.unsorted[:] = []


def do_one_step():
    N = get_int()
    pairs = [get_ints() for i in range(N)]
    pairs.sort()

    unique_swap = set()

    container = BinarySearch()
    for p2 in pairs:
        for p1 in container.upper(p2):
            diff = Fraction(p1[1]-p2[1], p2[0]-p1[0])
            unique_swap.add(diff)
        container.insert(p2)

    return len(unique_swap)+1


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


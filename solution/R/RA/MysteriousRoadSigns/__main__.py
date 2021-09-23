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


class Container:
    def __init__(self):
        self.size = 0
        self.sets = set()

    def update(self, left, right):
        length = right - left
        if length > self.size:
            self.size = length
            self.sets.clear()
            self.sets.add(left)
        elif length == self.size:
            self.sets.add(left)


class Node:
    def __init__(self, start, end, key):
        self.start = start
        self.end = end
        self.previous = None
        self.first = None
        self.key = key

    def update(self, node):
        self.previous = node.key
        if node.previous == self.key:
            self.first = node.first
        else:
            self.first = node.start

    def length(self):
        return self.end - self.first


def wrap_index(iterator) -> List[Node]:
    prev = 0
    for i, subiter in itertools.groupby(iterator):
        subiter = list(subiter)
        curr = prev + len(subiter)
        yield Node(prev, curr, i)
        prev = curr


def is_follow(one, other):
    return one and (
        len(other) == 0 or
        one[-1].start <= other[-1].start
    )


def do_one_step():
    S = get_int()

    left, right = [], []
    for _ in range(S):
        d, a, b = get_ints()
        left.append(d+a)
        right.append(d-b)

    left = list(wrap_index(left))
    right = list(wrap_index(right))
    left.reverse()
    right.reverse()
    left_prev = Node(0, 0, 0)
    right_prev = Node(0, 0, 0)

    count = Container()

    while left and right:
        left_pop = False
        right_pop = False
        if is_follow(left, right):
            left[-1].update(right_prev)
            left_pop = True
        if is_follow(right, left):
            right[-1].update(left_prev)
            right_pop = True

        if left_pop:
            l = left_prev = left.pop()
            count.update(l.first, l.end)
        if right_pop:
            r = right_prev = right.pop()
            count.update(r.first, r.end)

    return count.size, len(count.sets)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #{}: {} {}".format(i, *do_one_step()))


if __name__ == "__main__":
    main()


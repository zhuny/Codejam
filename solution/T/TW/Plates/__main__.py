import heapq
from queue import Queue


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class NumberStream:
    def __init__(self, num_list):
        self.num_list = num_list
        self.index = 0

    def is_end(self):
        return self.index == len(self.num_list)

    def top(self):
        return self.num_list[self.index]


def merge_it(l, r):
    result = [0] * (len(l)+len(r)-1)

    for i, x in enumerate(l):
        for j, y in enumerate(r):
            result[i+j] = max(result[i+j], x+y)

    return result


def accumul(nums):
    result = [0]
    for num in nums:
        result.append(result[-1]+num)
    return result


def do_one_step():
    N, K, P = get_ints()

    q = Queue()
    for i in range(N):
        q.put(accumul(get_ints()))

    while q.qsize() > 1:
        q.put(merge_it(q.get(), q.get())[:P+1])

    result = q.get()
    return result[P]


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


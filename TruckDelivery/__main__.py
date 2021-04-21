import collections
import functools
import math


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class Node:
    def __init__(self):
        self.parent = None
        self.gcd_info = []


def my_gcd(a, b):
    if a == 0:
        return b
    else:
        return math.gcd(a, b)


def merge(g, cut, weight):
    answer = list(g)
    answer.append((cut, weight))
    answer.sort()
    answer_result = []
    for c, w in answer:
        if answer_result:
            appended = c, my_gcd(answer_result[-1][1], w)
            if answer_result[-1][0] == c:
                answer_result[-1] = appended
            elif answer_result[-1][1] != appended[1]:
                answer_result.append(appended)
        else:
            answer_result.append((c, w))
    return answer_result


def build_tree(node_set, graph, current, parent):
    queue = [(parent, current, [(0, 0), (10 ** 18, 1)])]

    while queue:
        p, c, g = queue.pop()
        for adj, pair in graph[c].items():
            if adj == p:
                continue
            queue.append((c, adj, merge(g, pair[0], pair[1])))

        if p is not None:
            node_set[c].parent = node_set[p]
            node_set[c].gcd_info = g


def do_one_step():
    n, q = get_ints()

    c = collections.defaultdict(dict)
    for i in range(1, n):
        start, end, cut, count = get_ints()
        c[start][end] = cut, count
        c[end][start] = cut, count

    node_set = collections.defaultdict(Node)
    build_tree(node_set, c, 1, None)

    query_answer = []

    for i in range(q):
        start, cut = get_ints()
        answer = 0
        for c, w in node_set[start].gcd_info:
            if c <= cut:
                answer = w
            else:
                break
        query_answer.append(answer)

    return " ".join(map(str, query_answer))


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


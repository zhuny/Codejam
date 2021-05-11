import collections
import heapq


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def build_jump(command):
    jump = {}
    stack = []
    for i, char in enumerate(command):
        if char == '(':
            stack.append(i)
        elif char == ')':
            j = stack.pop()
            jump[j] = i
            jump[i] = j
    return jump


class Graph:
    def __init__(self, size):
        self.size = size
        self.mapping = collections.defaultdict(dict)

    def __del__(self):
        del self.mapping

    def add_edge(self, start, end, weight):
        if 0 <= start < self.size and 0 <= end < self.size:
            self.mapping[start][end] = weight

    def travel(self, start, end):
        q = QueueHeap()
        q.push(start, 0)
        done = set()

        while q.body:
            v, length = q.pop()
            if v == end:
                return length
            if v in done:
                continue
            done.add(v)
            for w, weight in self.mapping[v].items():
                if w not in done:
                    q.push(w, length+weight)


class QueueHeap:
    def __init__(self):
        self.body = []
        self.weight = {}

    def __del__(self):
        del self.body

    def push(self, v, length):
        if v in self.weight and self.weight[v] <= length:
            return
        heapq.heappush(self.body, (length, v))
        self.weight[v] = length

    def pop(self):
        length, v = heapq.heappop(self.body)
        return v, length


def do_one_step():
    V, Q = get_ints()
    jump = build_jump(get_line())

    g = Graph(V)
    for v, speed in enumerate(get_ints()):
        g.add_edge(v, v+1, speed)
    for v, speed in enumerate(get_ints()):
        g.add_edge(v, v-1, speed)
    for v, speed in enumerate(get_ints()):
        g.add_edge(v, jump[v], speed)

    start = get_ints()
    end = get_ints()
    length = 0
    for q in range(Q):
        length += g.travel(start[q]-1, end[q]-1)

    return length


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


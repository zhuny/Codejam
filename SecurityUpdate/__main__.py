import collections


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class Edge:
    def __init__(self):
        self.number = None
        self.latency = None


class VertexMap(collections.defaultdict):
    def __init__(self):
        super().__init__(Edge)


class Graph:
    def __init__(self, size):
        self.size = size
        self.vertices = {i: 0 for i in range(1, size+1)}
        self.edges = collections.defaultdict(VertexMap)

    def set_vertex(self, v, t):
        self.vertices[v] = t

    def connect(self, v1, v2, n):
        self.edges[v1][v2].number = n
        self.edges[v2][v1].number = n

        latency = max(abs(self.vertices[v1]-self.vertices[v2]), 1)
        self.edges[v1][v2].latency = latency
        self.edges[v2][v1].latency = latency

    def answer(self):
        number_to_latency = {}
        for v1, v1map in self.edges.items():
            for v2, edge in v1map.items():
                number_to_latency[edge.number] = edge.latency

        return " ".join(
            str(number_to_latency[i])
            for i in range(len(number_to_latency))
        )


def do_one_step():
    c, d = get_ints()
    x_list = get_ints()

    g = Graph(c)
    for i, reached_time in enumerate(x_list, 2):
        g.set_vertex(i, -reached_time)

    for i in range(d):
        u, v = get_ints()
        g.connect(u, v, i)

    for x in x_list:
        if x > 0:
            # do not run test set 2
            return "-"

    return g.answer()


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


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


def normalize(x_list):
    x_time_list = [
        (x, index)
        for index, x in enumerate(x_list)
        if x > 0
    ]
    x_time_list.sort(reverse=True)

    x_pos_list = [
        (x, index)
        for index, x in enumerate(x_list)
        if x < 0
    ]
    x_pos_list.sort(reverse=True)

    x_merge_list = []
    for x, index in x_pos_list:
        while len(x_merge_list) + x + 1 < 0:
            x_merge_list.append(x_time_list.pop())
        x_merge_list.append((x, index))
    while x_time_list:
        x_merge_list.append(x_time_list.pop())

    x_result_list = []
    current_time = 0
    current_number = 0
    for i, (x, index) in enumerate(x_merge_list, 1):
        if x > 0:
            x_result_list.append((x, index))
            current_time = x
            current_number = i
        elif current_number + x < 0:
            current_time += 1
            current_number = -x
            x_result_list.append((current_time, index))
        else:
            x_result_list.append((current_time, index))

    x_index_list = [0 for x in x_result_list]
    for x, index in x_result_list:
        x_index_list[index] = x
    return x_index_list


def do_one_step():
    c, d = get_ints()
    x_list = normalize(get_ints())

    g = Graph(c)
    for i, reached_time in enumerate(x_list, 2):
        g.set_vertex(i, reached_time)

    for i in range(d):
        u, v = get_ints()
        g.connect(u, v, i)

    return g.answer()


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


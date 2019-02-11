import collections
import random
import time


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class FlowOut(collections.defaultdict):
    def __init__(self):
        super().__init__(int)


class Flow(collections.defaultdict):
    def __init__(self):
        super().__init__(FlowOut)


class Network:
    def __init__(self):
        self.capacity = Flow()
        self.flow = Flow()

    def add(self, source, target):
        self.capacity[source][target] = 1
        self.capacity[target][source] = 0

    def residual_network(self, s, t):
        return self.capacity[s][t]-self.flow[s][t]

    def find_path(self, source, target):
        queue = [source]
        before = {}

        while queue:
            current = queue.pop()
            if current == target:
                break

            for adj in self.capacity[current]:
                if adj not in before:
                    residual = self.residual_network(current, adj)
                    if residual > 0:
                        queue.append(adj)
                        before[adj] = current

        if target in before:
            path = [target]
            while path[-1] != source:
                path.append(before[path[-1]])
            path.reverse()
            return list(zip(path[:-1], path[1:]))

    def get_max_flow(self, source, target):
        self.flow.clear()
        total_flow = 0
        while True:
            path = self.find_path(source, target)
            if path is None:
                break
            flow = [
                self.residual_network(s, t)
                for s, t in path
            ]
            flow_max = max(flow)
            total_flow += flow_max
            for s, t in path:
                self.flow[s][t] += flow_max
                self.flow[t][s] -= flow_max
        return total_flow


def get_maximum(pos_list):
    net = Network()
    start, end = 's', 'e'
    for x, y in pos_list:
        net_x = x, 0
        net_y = y, 1
        net.add(start, net_x)
        net.add(net_x, net_y)
        net.add(net_y, end)
    return net.get_max_flow(start, end)


def do_one_step():
    N = get_int()

    matches = collections.defaultdict(list)
    for i in range(N):
        for j, v in enumerate(get_ints()):
            p = i, j
            matches[v].append(p)

    count = 0
    for v, ps in matches.items():
        if len(ps) > 1:
            count += len(ps)-get_maximum(ps)
    return count


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


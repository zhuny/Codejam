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


class Flow:
    def __init__(self, count):
        self.body = [[0]*count for i in range(count)]
        self.adjacent_map = [set() for i in range(count)]

    def __setitem__(self, key, value):
        key_x, key_y = key
        self.body[key_x][key_y] = value
        self.adjacent_map[key_x].add(key_y)
        self.adjacent_map[key_y].add(key_x)

    def __getitem__(self, item):
        item_x, item_y = item
        return self.body[item_x][item_y]

    def get_adjacent(self, source):
        yield from self.adjacent_map[source]


class Network:
    def __init__(self, count):
        self.capacity = Flow(count)
        self.flow = Flow(count)
        self.count = count

    def add(self, source, target):
        self.capacity[source, target] = 1

    def residual_network(self, s, t):
        return self.capacity[s, t]-self.flow[s, t]

    def _random_dequeue(self, element_list):
        return element_list.pop()

    def find_path(self, source, target):
        queue = [source]
        before = [None for i in range(self.count)]

        while queue:
            current = self._random_dequeue(queue)
            if current == target:
                break

            for adj in self.capacity.get_adjacent(current):
                if before[adj] is None:
                    residual = self.residual_network(current, adj)
                    if residual > 0:
                        queue.append(adj)
                        before[adj] = current

        if before[target] is not None:
            path = [target]
            while path[-1] != source:
                path.append(before[path[-1]])
            path.reverse()
            return list(zip(path[:-1], path[1:]))

    def get_max_flow(self, source, target):
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
                self.flow[s, t] += flow_max
                self.flow[t, s] -= flow_max
        return total_flow


def get_maximum(count, pos_list):
    net = Network(count*2+2)
    start = count*2
    end = start+1

    for x, y in pos_list:
        net_x = x
        net_y = y+count
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
            count += len(ps)-get_maximum(N, ps)
    return count


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


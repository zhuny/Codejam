def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class DisjointSet:
    def __init__(self, count):
        self.mapping = [i for i in range(count)]

    def _root(self, p):
        while p != self.mapping[p]:
            p = self.mapping[p]
        return p

    def is_connected(self, p1, p2):
        return self._root(p1) == self._root(p2)

    def connect(self, p1, p2):
        r1 = self._root(p1)
        r2 = self._root(p2)
        self.mapping[r1] = self.mapping[p1] = self.mapping[p2] = r2

    def set_count(self):
        roots = set()
        for point, m in enumerate(self.mapping):
            roots.add(self._root(point))
        return len(roots)


def do_one_step():
    N, M = get_ints()
    ds = DisjointSet(N)
    sugar = 0
    for _ in range(M):
        ci, di = get_ints()
        ci, di = ci-1, di-1
        if not ds.is_connected(ci, di):
            sugar += 1
            ds.connect(ci, di)
    return sugar + ds.set_count()*2-2


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


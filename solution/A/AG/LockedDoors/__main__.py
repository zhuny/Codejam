def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class Heap:
    def __init__(self, start, end, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

    def __repr__(self):
        if self.start == self.end:
            return str(self.start)
        else:
            return "<{0.left}|{0.right}>".format(self)

    def merge(self, right):
        return Heap(self.start, right.end, self, right)

    def contains(self, point):
        return self.start <= point <= self.end

    def size(self):
        return self.end-self.start

    def query(self, start, count):
        current = self
        while count > 0:
            if current.left.contains(start):
                size = current.left.size()+1
                if count >= size:
                    count -= size
                    start = current.right.start
                    current = current.right
                else:
                    current = current.left
            else:
                size = current.right.size()+1
                if count >= size:
                    count -= size
                    start = current.left.end
                    current = current.left
                else:
                    current = current.right
        return start


def do_one_step():
    N, Q = get_ints()

    right = [Heap(i, i) for i in range(N)]
    left = [None]
    left.extend(right)
    right.append(None)

    link = [(v, i) for i, v in enumerate(get_ints(), 1)]
    link.sort()
    for v, i in link:
        heap = left[i].merge(right[i])
        left[i] = right[i] = None
        right[heap.start] = heap
        left[heap.end+1] = heap

    root = right[0]
    answers = []
    for i in range(Q):
        start, end = get_ints()
        answers.append(root.query(start-1, end-1)+1)

    return " ".join(str(answer) for answer in answers)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


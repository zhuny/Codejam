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


class Queue:
    def __init__(self):
        self.body = []
        self.tail_index = 0

    def size(self):
        return len(self.body)-self.tail_index

    def enqueue(self, elem):
        self.body.append(elem)

    def dequeue(self):
        result = self.body[self.tail_index]
        self.tail_index += 1
        return result

    def top(self):
        return self.body[self.tail_index]


def do_one_step():
    N, S = get_ints()
    values = get_ints()
    assert len(values) == N

    counter_val = collections.defaultdict(int)
    counter = []
    for i, value1 in enumerate(values):
        counter.append(counter_val[value1])
        counter_val[value1] += 1

    before_count = []
    max_value = 0
    counter = collections.defaultdict(Queue)
    counter_last = {}
    for i, value1 in enumerate(values):
        if counter[value1].size() < S:
            for j, count in enumerate(before_count):
                before_count[j] = count+1
        else:
            top = counter[value1].dequeue()
            last = counter_last.get(value1, 0)
            # 0 ~ last : nop
            # last ~ top : -S
            # top ~ : +1
            for j, count in enumerate(before_count):
                if j < last:
                    pass
                elif j <= top:
                    before_count[j] = count-S
                else:
                    before_count[j] = count+1
            counter_last[value1] = top+1

        counter[value1].enqueue(i)
        before_count.append(1)
        max_value = max(max_value, max(before_count))

    return max_value


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


from dataclasses import dataclass, field
from typing import List


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


@dataclass
class Interval:
    start: int = 0
    end: int = 0
    parent: 'Interval' = None
    children: List['Interval'] = field(default_factory=list)

    def find(self, point: int):
        current = self
        while current.start < point < current.end:
            current = current.find_one(point)
        return current

    def find_one(self, point: int):
        for child in self.children:
            if child.start <= point <= child.end:
                return child

    def side_cost(self, point: int):
        return self, int(self.start != point), int(self.end != point)

    def find_index(self, point: int):
        l, r = 0, len(self.children)
        while True:
            m = (l+r)//2
            child = self.children[m]
            if child.start <= point <= child.end:
                return m
            elif child.end < point:
                l = m+1
            else:
                r = m

    def until_contain(self, start: int, end: int):
        current, left, right = self.side_cost(start)
        while not (current.start <= end <= current.end):
            current = current.parent
            i = current.find_index(start)
            left += 2*i+1
            right += 2*(len(current.children)-i)-1
        return current, left, right

    def until_contain_child(self, start: int, end: int):
        current, left, right = self.side_cost(start)
        current = current.parent
        while not (current.start <= end <= current.end):
            i = current.find_index(start)
            left += 2*i+1
            right += 2*(len(current.children)-i)-1
            current = current.parent
        return current, left, right


def build_interval():
    root = Interval()
    stack = [root]

    for i, char in enumerate(get_line(), 1):
        if char == '(':
            child = Interval(start=i, parent=stack[-1])
            stack[-1].children.append(child)
            stack.append(child)
        else:
            last = stack.pop()
            last.end = i

    root.start = root.children[0].start
    root.end = root.children[-1].end

    return root


def do_query(root: Interval, start, end):
    sn = root.find(start)
    en = root.find(end)

    if sn.start <= end <= sn.end:
        cn1, slc, src = sn.side_cost(start)
        cn2, elc, erc = en.until_contain(end, start)
        return min(
            slc+elc,
            src+erc
        )

    if en.start <= start <= en.end:
        cn1, slc, src = sn.until_contain(start, end)
        cn2, elc, erc = en.side_cost(end)
        return min(
            slc+elc,
            src+erc
        )

    cn1, slc, src = sn.until_contain_child(start, end)
    cn2, elc, erc = en.until_contain_child(end, start)

    start_index = cn1.find_index(start)
    end_index = cn2.find_index(end)

    return min(
        src+elc+2*(end_index-start_index)-1,
        slc+erc+2*start_index+1+2*(len(cn2.children)-end_index)-1+1
    )


def do_one_step():
    length, query = get_ints()
    root = build_interval()

    # do just test set 1
    left = get_ints()
    right = get_ints()
    pair = get_ints()

    start_point = get_ints()
    end_point = get_ints()

    answer = []
    for start, end in zip(start_point, end_point):
        if abs(start-end) <= 1:
            answer.append(abs(start-end))
            continue
        elif start > end:
            start, end = end, start
        answer.append(do_query(root, start, end))

    # print(answer)

    return sum(answer)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()

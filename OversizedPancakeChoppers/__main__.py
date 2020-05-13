import collections
from fractions import Fraction


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class CakeSize:
    def __init__(self):
        self.cuts = {0: 0}

    @staticmethod
    def _cut_item(n):
        yield 0, 0
        for i in range(n):
            yield i+1, i+1
        yield n+1, n

    def update(self, cut_add):
        cut_after = collections.defaultdict(list)
        for people1, cut1 in self.cuts.items():
            for people2, cut2 in self._cut_item(cut_add):
                cut_after[people1+people2].append(cut1+cut2)
        for people, cut in cut_after.items():
            if people <= 50:
                self.cuts[people] = min(cut, default=-1)

    def check(self, people):
        return self.cuts.get(people)


def do_one_step():
    N, D = get_ints()
    Ai = get_ints()

    count = collections.defaultdict(CakeSize)

    for a in Ai:
        for i in range(1, D+1):
            count[Fraction(a, i)].update(i-1)

    answer = D-1

    for k, v in count.items():
        check = v.check(D)
        if check is not None:
            answer = min(answer, check)

    return answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


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


class Line:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def slope(self):
        p1 = self.left
        p2 = self.right
        if p1[0] == p2[0]:
            return 1, 0
        else:
            f = Fraction(p2[1] - p1[1], p2[0] - p1[0])
            return f.numerator, f.denominator

    @property
    def key(self):
        p1 = self.left
        p2 = self.right
        if p1[0] == p2[0]:
            return 1, 0, p1[0]
        else:
            f = Fraction(p2[1] - p1[1], p2[0] - p1[0])
            return f.numerator, f.denominator, p2[1]-p2[0]*f


def do_one_step():
    n = get_int()
    holes = [tuple(get_ints()) for i in range(n)]
    slope_group = collections.defaultdict(list)
    line_group = collections.defaultdict(set)
    for i in range(n):
        for j in range(i+1, n):
            line = Line(holes[i], holes[j])
            slope_group[line.slope].append(line)
            line_group[line.key].add(holes[i])
            line_group[line.key].add(holes[j])

    items = sorted(
        slope_group.items(),
        key=lambda item: len(item[1]), reverse=True
    )
    answer = min(4, n)
    for slope, lines in items:
        if answer > len(lines):
            break
        odd_count = 0
        key_set = {line.key for line in lines}
        for key in key_set:
            if len(line_group[key]) % 2 == 1:
                odd_count += 1
        new_answer = sum(
            len(line_group[key])
            for key in key_set
        )
        if odd_count % 2 == 1:
            new_answer -= 1
        answer = max(answer, min(new_answer+2, n))

    return answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


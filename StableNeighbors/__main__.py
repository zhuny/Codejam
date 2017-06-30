# @Date    : 2017-04-23 01:45:14
# @Author  : Jihun Yang (zhuny@kaist.ac.kr)
# @File    : __main__.py


def get_ints():
    return map(int, input().split())


class Wrap:
    def __init__(self, one, two, one_str, two_str):
        self.one = one
        self.two = two
        self.one_str = one_str
        self.two_str = two_str
        self.count = one-two
        self._valid = (one < two*2)

    def __lt__(self, rhs):
        return self.count < rhs.count

    def is_invalid(self):
        return self._valid

    def get(self):
        if self.two > 0:
            self.two -= 1
            return "{0.one_str}{0.two_str}{0.one_str}".format(self)
        else:
            return self.one_str


def do_cal():
    N, R, O, Y, G, B, V = get_ints()

    rr = Wrap(R, G, "R", "G")
    yy = Wrap(Y, V, "Y", "V")
    bb = Wrap(B, O, "B", "O")

    if is_possible(rr, yy, bb):
        print ("".join(do_stream(rr, yy, bb)))

    else:
        print ("IMPOSSIBLE")


def is_possible(rr, yy, bb):
    if rr.count == yy.count == bb.count == 0:
        L = [rr, yy, bb]
        L.sort(key=lambda e:e.one)
        return (
            L[0].one == L[1].one == 0
        )

    if rr.is_invalid() or yy.is_invalid() or bb.is_invalid():
        return False

    L = rr.count, yy.count, bb.count
    return sum(L) >= max(L)*2


def do_stream(rr, yy, bb):
    l = [rr, yy, bb]
    l.sort()

    if l[0].count == l[1].count == 0:
        for wrap in l:
            for i in range(wrap.one):
                yield wrap.one_str
                yield wrap.two_str

    else:
        three = l[0].count+l[1].count-l[2].count

        for i in range(three):
            yield l[2].get()
            yield l[1].get()
            yield l[0].get()

        for i in range(l[1].count-three):
            yield l[2].get()
            yield l[1].get()

        for i in range(l[0].count-three):
            yield l[2].get()
            yield l[0].get()


def main():
    n = int(input())

    for i in range(n):
        print ("Case #%d: "%(i+1), end="")
        do_cal()





if __name__ == "__main__":
    main()



def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class DefaultValue:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.body = {}

    def __getitem__(self, item):
        if item in self.body:
            return self.body[item]
        else:
            return self._default(item)

    def __setitem__(self, key, value):
        self.body[key] = value

    def _default(self, item):
        raise NotImplementedError


class DefaultValueN(DefaultValue):
    def _default(self, item):
        return max(item[0]-1, 1), item[1]


class DefaultValueS(DefaultValue):
    def _default(self, item):
        return min(item[0]+1, self.row), item[1]


class DefaultValueW(DefaultValue):
    def _default(self, item):
        return item[0], max(item[1]-1, 1)


class DefaultValueE(DefaultValue):
    def _default(self, item):
        return item[0], min(item[1]+1, self.col)


def do_one_step():
    N, R, C, Sr, Sc = get_ints()

    # 기본 값을 미리 계산해두면 Memory Limit Error가 나서 수정
    toN = DefaultValueN(R, C)
    toS = DefaultValueS(R, C)
    toW = DefaultValueW(R, C)
    toE = DefaultValueE(R, C)
    direct = {'W': toW, 'E': toE, 'N': toN, 'S': toS}

    def remove_link(rr, cc):
        ww = toW[rr, cc]
        ee = toE[rr, cc]
        nn = toN[rr, cc]
        ss = toS[rr, cc]
        toW[ee] = ww
        toE[ww] = ee
        toN[ss] = nn
        toS[nn] = ss

    for com in get_line():
        next_pos = direct[com][Sr, Sc]
        remove_link(Sr, Sc)
        Sr, Sc = next_pos

    return Sr, Sc


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #{}: {} {}".format(i, *do_one_step()))


if __name__ == "__main__":
    main()


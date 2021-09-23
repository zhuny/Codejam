import sys


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class Problem:
    def __init__(self, size):
        self.size = size
        self.bit_list = [-1] * size

    def get(self, pos):
        print(pos+1)
        return get_int()

    def load_bits(self, count):
        for i, v in enumerate(self.bit_list):
            if count == 0:
                break
            if v == -1:
                self.bit_list[i] = self.get(i)
                self.bit_list[~i] = self.get(self.size-i-1)
                count -= 1
        for i in range(count*2):
            self.get(0)

    def not_yet(self):
        return -1 in self.bit_list

    def check_complement(self):
        for i, v in enumerate(self.bit_list):
            if v == -1:
                break
            if v == self.bit_list[~i]:
                if v != self.get(i):
                    for i2, v2 in enumerate(self.bit_list):
                        if v2 != -1:
                            self.bit_list[i2] = 1-v2
                return 1
        return 0

    def check_reflect(self):
        for i, v in enumerate(self.bit_list):
            if v == -1:
                break
            if v != self.bit_list[~i]:
                if v != self.get(i):
                    self.bit_list.reverse()
                return 1
        return 0

    def get_bits_str(self):
        return "".join(map(str, self.bit_list))

    def solve(self):
        self.load_bits(5)

        while self.not_yet():
            count = 10
            count -= self.check_complement()
            count -= self.check_reflect()
            self.load_bits(count//2)
            if count % 2 == 1:
                self.get(0)

        print(self.get_bits_str())

        result = get_line()
        if result == "N":
            assert False, vars(self)


def main():
    n, t = get_ints()
    for i in range(1, n+1):
        Problem(t).solve()


if __name__ == "__main__":
    main()


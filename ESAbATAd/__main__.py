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
    def __init__(self, count, size):
        self.reflect = False
        self.complement = False
        self.count = count
        self.size = size
        self.bit_list = [-1] * size

    def check(self, i, replace=True):
        print(i+1)
        result = get_int()
        if self.complement:
            result = 1-result
        if self.reflect:
            i = self.size-i-1
        if replace:
            self.bit_list[i] = result
        return result

    def ask_one_state(self, i):
        self.check(i)
        self.check(self.size-i-1)

    def ask_state(self, count):
        done = 0
        for i, value in enumerate(self.bit_list):
            if count == 0:
                break
            if value == -1:
                self.ask_one_state(i)
                count -= 1
                done += 1

        for i in range(count):
            self.ask_one_state(i)
            done += 1

        return done*2

    def check_complement(self):
        for i in range(self.size):
            if self.bit_list[i] is None:
                break
            if self.bit_list[i] == self.bit_list[self.size-i-1]:
                state = self.check(i, replace=False)
                self.complement = (self.bit_list[i] != state)
                return 2
        return 0

    def check_reflect(self):
        for i in range(self.size):
            if self.bit_list[i] is None:
                break
            if self.bit_list[i] != self.bit_list[self.size-i-1]:
                state = self.check(i, replace=False)

                return 2
        return 0

    def remaind(self, count):
        if count % 5 == 0:
            return 5
        else:
            return count % 5

    def check_result(self):
        result = [state if state >= 0 else state == "?" for state in self.bit_list]
        if self.complement:
            result = [1-state for state in self.bit_list]
        if self.reflect:
            result = list(reversed(result))
        print("".join(map(str, result)))
        assert get_line() == "Y", vars(self)

    def solve(self):
        rest = self.count - self.ask_state(5)
        while rest > 0:
            rest -= self.check_complement()
            rest -= self.check_reflect()
            rest -= self.ask_state(self.remaind(rest))
        self.check_result()


def main():
    n, t = get_ints()
    for i in range(1, n+1):
        Problem(n, t).solve()


if __name__ == "__main__":
    main()


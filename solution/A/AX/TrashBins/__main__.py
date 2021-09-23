from typing import Dict, Any


class SolutionBase:
    # internal code for
    @staticmethod
    def read_int():
        return int(input())

    @staticmethod
    def read_ints():
        return [int(i) for i in input().split()]

    @staticmethod
    def read_line():
        return input().strip()

    # implementation in subclass
    def load_data(self) -> Dict[str, Any]:
        raise NotImplementedError

    def solve(self, **kwargs):
        raise NotImplementedError

    def format_answer(self, answer) -> str:
        raise NotImplementedError

    def main(self):
        t = self.read_int()
        for i in range(1, t+1):
            answer = self.format_answer(
                self.solve(
                    **self.load_data()
                )
            )
            print(f"Case #{i}: {answer}")


class MySolution(SolutionBase):
    def load_data(self) -> Dict[str, Any]:
        size = self.read_int()
        trash_bins = [char == '1' for char in self.read_line()]
        return {'size': size, 'trash_bins': trash_bins}

    def two_side(self, length):
        # 1 -> 1
        # 11 -> 2
        # 121 -> 4
        # 1221 -> 6
        # 12321 -> 9
        # 123321 -> 12
        # 1234321 -> 16
        left = length // 2
        return self.one_side(left) + self.one_side(length - left)

    def one_side(self, n):
        return n * (n + 1) // 2

    def solve(self, size, trash_bins):
        length = 0
        is_first = True
        total_walks = 0
        for has_bin in trash_bins:
            if has_bin:
                if is_first:
                    total_walks += self.one_side(length)
                else:
                    total_walks += self.two_side(length)
                is_first = False
                length = 0
            else:
                length += 1
        if length > 0:
            total_walks += self.one_side(length)

        return total_walks

    def format_answer(self, answer) -> str:
        return answer


if __name__ == "__main__":
    MySolution().main()

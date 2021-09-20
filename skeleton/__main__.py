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
        return {'r': self.read_int()}

    def solve(self, r):
        return r*r

    def format_answer(self, answer) -> str:
        return f"{answer:05}"


if __name__ == "__main__":
    MySolution().main()

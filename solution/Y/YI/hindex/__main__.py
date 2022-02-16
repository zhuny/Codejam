import heapq
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
        return {
            'n': self.read_int(),
            'citations': self.read_ints()
        }

    def solve(self, n, citations):
        h_index = []
        top = []
        for citation in citations:
            heapq.heappush(top, citation)
            if top[0] < len(top):
                heapq.heappop(top)
            h_index.append(len(top))
        return h_index

    def format_answer(self, answer) -> str:
        return " ".join(map(str, answer))


if __name__ == "__main__":
    MySolution().main()

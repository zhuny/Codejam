import itertools
import math
from dataclasses import dataclass
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


@dataclass
class Point:
    x: int
    y: int

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def rotate(self, other):
        cross = self.x * other.y - self.y * other.x
        if cross > 0:
            return 1
        elif cross < 0:
            return -1
        else:
            return 0

    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def distance(self, other):
        return (self - other).length()


class MySolution(SolutionBase):
    def load_data(self) -> Dict[str, Any]:
        whites = self.read_int()
        return {
            'white_star_list': [
                Point(*self.read_ints())
                for w in range(whites)
            ],
            'blue_star': Point(*self.read_ints()),
        }

    def solve(self, blue_star, white_star_list):
        perimeter = None
        for a, b, c in itertools.combinations(white_star_list, 3):
            if self.triangle_contains(a, b, c, blue_star):
                p = self.triangle_perimeter(a, b, c)
                if perimeter is None or p < perimeter:
                    perimeter = p

        return perimeter

    def triangle_contains(self, a, b, c, p):
        ap, bp, cp = a - p, b - p, c - p
        return ap.rotate(bp) == bp.rotate(cp) == cp.rotate(ap)

    def triangle_perimeter(self, a, b, c):
        return a.distance(b) + b.distance(c) + c.distance(a)

    def format_answer(self, answer) -> str:
        if answer is None:
            return "IMPOSSIBLE"
        else:
            return f"{answer:.08}"


if __name__ == "__main__":
    MySolution().main()

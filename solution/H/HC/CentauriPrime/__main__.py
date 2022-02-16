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
        return {'name': self.read_line()}

    def solve(self, name: str):
        name_lower = name.lower()
        vowel = "aeiou"
        if name_lower.endswith("y"):
            return name, "nobody"
        for char in vowel:
            if name_lower.endswith(char):
                return name, "Alice"
        return name, "Bob"

    def format_answer(self, answer) -> str:
        name, ruled = answer
        return f"{name} is ruled by {ruled}."


if __name__ == "__main__":
    MySolution().main()

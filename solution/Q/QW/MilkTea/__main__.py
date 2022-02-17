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
        n, m, p = self.read_ints()
        return {
            'friend_list': [self.read_line() for _ in range(n)],
            'forbidden_list': [self.read_line() for _ in range(m)],
            'option': p
        }

    def insert_queue(self, queue, queue_set, option, option_count):
        if option in queue_set:
            return
        claim_count = 0
        for char, option_count in zip(option, option_count):
            char = int(char)
            claim_count += option_count[1-char]
        heapq.heappush(queue, (claim_count, option))
        queue_set.add(option)

    def adj_option(self, option):
        for i, char in enumerate(option):
            new_char = str(1-int(char))
            yield option[:i] + new_char + option[i+1:]

    def solve(self, friend_list, forbidden_list, option):
        min_options = ['']
        option_count = []
        for i in range(option):
            t_count = f_count = 0
            for friend in friend_list:
                if friend[i] == '0':
                    f_count += 1
                else:
                    t_count += 1
            option_count.append((f_count, t_count))
            opt = []
            if t_count >= f_count:
                opt.append('1')
            if t_count <= f_count:
                opt.append('0')
            min_options = [
                min_o + o
                for min_o in min_options
                for o in opt
            ]

        queue = []
        queue_set = set()
        for option in min_options:
            self.insert_queue(queue, queue_set, option, option_count)

        while queue:
            count, option = heapq.heappop(queue)
            if option not in forbidden_list:
                return count
            for another in self.adj_option(option):
                self.insert_queue(queue, queue_set, another, option_count)

    def format_answer(self, answer) -> str:
        return str(answer)


if __name__ == "__main__":
    MySolution().main()

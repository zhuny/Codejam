import collections
import heapq
from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, Any, List


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


@dataclass(order=True)
class AttractInfo:
    happiness: int
    start_day: int
    end_day: int


class MultiSet(collections.defaultdict):
    def __init__(self):
        super().__init__(int)

    def insert(self, e):
        self[e] += 1

    def remove(self, e):
        self[e] -= 1

    def contains(self, e):
        return self[e] > 0


class Heap:
    def __init__(self):
        self.body = []
        self.total = 0
        self.body_multi_set = MultiSet()
        self.removed = MultiSet()
        self.count = 0

    def __len__(self):
        return self.count

    def key(self, element):
        raise NotImplementedError

    def push(self, element):
        ke = self.key(element), element
        heapq.heappush(self.body, ke)

        self.total += element
        self.body_multi_set.insert(element)
        self.count += 1

    def pop(self):
        while True:
            k, e = heapq.heappop(self.body)
            if self.removed.contains(e):
                self.removed.remove(e)
            else:
                break

        self.total -= e
        self.body_multi_set.remove(e)
        self.count -= 1

        return e

    def remove(self, element):
        self.total -= element
        self.body_multi_set.remove(element)
        self.removed.insert(element)
        self.count -= 1

    def contains(self, element):
        return self.body_multi_set.contains(element)

    def element_sum(self):
        return self.total


class MaxHeap(Heap):
    def key(self, element):
        return -element


class MinHeap(Heap):
    def key(self, element):
        return element


class LimitSizeQueue:
    def __init__(self, limit):
        self.limit = limit
        self.top = MinHeap()
        self.bottom = MaxHeap()

    def add(self, e):
        self.top.push(e)
        if len(self.top) > self.limit:
            self.bottom.push(self.top.pop())

    def remove(self, e):
        if self.bottom.contains(e):
            self.bottom.remove(e)
        else:
            self.top.remove(e)
            if self.bottom:
                self.top.push(self.bottom.pop())

    def get_top(self):
        return self.top.element_sum()


@dataclass(order=True)
class Event:
    day: int
    move: bool
    attract: AttractInfo


class MySolution(SolutionBase):
    def load_data(self) -> Dict[str, Any]:
        days, attract_number, ride_limit = self.read_ints()
        attract_list = [
            AttractInfo(*self.read_ints())
            for i in range(attract_number)
        ]
        return {
            'days': days,
            'attract_list': attract_list,
            'ride_limit': ride_limit
        }

    def solve(self, days, ride_limit, attract_list: List[AttractInfo]):
        event_list = []
        for attract in attract_list:
            event_list.append(Event(attract.start_day, False, attract))
            event_list.append(Event(attract.end_day, True, attract))
        event_list.sort()

        queue = LimitSizeQueue(ride_limit)
        max_happiness = 0
        for e in event_list:
            if e.move:
                queue.remove(e.attract.happiness)
            else:
                queue.add(e.attract.happiness)
                max_happiness = max(max_happiness, queue.get_top())

        return max_happiness

    def format_answer(self, answer) -> str:
        return answer


if __name__ == "__main__":
    MySolution().main()

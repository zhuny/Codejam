import collections
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


class Graph:
    def __init__(self):
        self.vertices = {0, 1}
        self.edges = collections.defaultdict(set)

    def neighbor(self, pos):
        x, y = pos
        yield x-1, y
        yield x-1, y+1
        yield x, y-1
        yield x, y+1
        yield x+1, y-1
        yield x+1, y

    def add_edge(self, v1, v2):
        self.edges[v1].add(v2)
        self.edges[v2].add(v1)

    def add_vertex(self, v):
        self.vertices.add(v)
        for another in self.neighbor(v):
            if another in self.vertices:
                self.add_edge(v, another)

    def has_edge(self, v1, v2):
        return v2 in self.edges[v1]

    def find_path(self, start, end, flow_graph):
        queue = set()
        queue.add((None, start))
        done = {}
        while queue:
            prev, v1 = queue.pop()
            done[v1] = prev
            if v1 == end:
                path = [end]
                while path[-1] != start:
                    path.append(done[path[-1]])
                path.reverse()
                return path

            for v2 in self.edges[v1]:
                if v2 in done:
                    continue
                if (v1, v2) not in flow_graph:
                    if self.has_edge(v1, v2):
                        queue.add((v1, v2))

    def has_path(self, start, end, flow):
        flow_graph = set()
        for i in range(flow):
            path = self.find_path(start, end, flow_graph)
            if path is None:
                return False
            path = path[1:-1]
            for v1, v2 in zip(path[:-1], path[1:]):
                if (v2, v1) in flow_graph:
                    flow_graph.remove((v2, v1))
                else:
                    flow_graph.add((v1, v2))
        return True


class MySolution(SolutionBase):
    def load_data(self) -> Dict[str, Any]:
        n = self.read_int()
        board = [self.read_line() for _ in range(n)]
        return {'n': n, 'board': board}

    def solve(self, n, board):
        # 불가능한 경우인지 돌 갯수 확인 & 그래프 그리기
        r, b = 0, 0
        board_map = {}
        red_graph = Graph()
        blue_graph = Graph()
        for x, row in enumerate(board):
            for y, cell in enumerate(row):
                board_map[x, y] = cell
                if cell == "R":
                    r += 1
                    red_graph.add_vertex((x, y))
                elif cell == "B":
                    b += 1
                    blue_graph.add_vertex((x, y))

        # boundary에 대해 연결해준다.
        for i in range(n):
            blue_graph.add_vertex((i, -1))
            blue_graph.add_vertex((i, n))
            blue_graph.add_edge(0, (i, -1))
            blue_graph.add_edge((i, n), 1)

            red_graph.add_vertex((-1, i))
            red_graph.add_vertex((n, i))
            red_graph.add_edge(0, (-1, i))
            red_graph.add_edge((n, i), 1)

        if abs(r - b) >= 2:
            return

        # 누가 이겼는지 확인
        if red_graph.has_path(0, 1, 1):
            # 빨강이 연결되어있긴 하다
            if r < b:
                return
            elif red_graph.has_path(0, 1, 2):
                return
            return 'R'
        elif blue_graph.has_path(0, 1, 1):
            # 파랑이 연결되어있음
            if r > b:
                return
            elif blue_graph.has_path(0, 1, 2):
                return
            return 'B'
        else:
            # 아직 게임이 안 끝남
            return 'N'

    to_str = {
        'N': 'Nobody',
        'R': 'Red',
        'B': 'Blue'
    }

    def format_answer(self, answer) -> str:
        if answer is None:
            return "Impossible"
        else:
            return f"{self.to_str[answer]} wins"


if __name__ == "__main__":
    MySolution().main()

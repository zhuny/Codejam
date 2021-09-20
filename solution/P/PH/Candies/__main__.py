def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class RangeSum:
    def __init__(self, body):
        self.original = list(body)
        self.body = []
        while body:
            self.body.append(body)
            body = [x+y for x, y in zip(body[::2], body[1::2])]

    def __setitem__(self, key, value):
        delta = value - self.original[key]
        self.original[key] = value
        for body in self.body:
            if key < len(body):
                body[key] += delta
            key //= 2

    def query(self, start, end):
        total = 0
        for body in self.body:
            if start < end:
                if start % 2 == 1:
                    total += body[start]
                    start += 1
                if end % 2 == 1:
                    end -= 1
                    total += body[end]
            start, end = start // 2, end // 2
        return total


def sign(n):
    if n % 2 == 0:
        return 1
    else:
        return -1


def do_one_step():
    N, Q = get_ints()
    A = get_ints()

    q_alter = RangeSum([a*sign(i) for i, a in enumerate(A)])
    qs_alter = RangeSum([
        a*sign(i)*(i+1) for i, a in enumerate(A)
    ])

    answer = 0

    for _ in range(Q):
        command, start, end = get_line().split()
        start, end = int(start)-1, int(end)

        if command == "Q":
            answer += (
                qs_alter.query(start, end) -
                q_alter.query(start, end) * start
            ) * sign(start)

        elif command == "U":
            q_alter[start] = end * sign(start)
            qs_alter[start] = end * sign(start) * (start+1)

    return answer


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


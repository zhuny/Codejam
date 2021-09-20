import collections
from typing import List


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


Robot = collections.namedtuple("Robot", "robot bit cashier")
Cashier = collections.namedtuple("Cashier", "maximum scan package")


def do_one_step():
    robot = Robot(*get_ints())
    cashiers = [Cashier(*get_ints()) for _ in range(robot.cashier)]

    start, end = 1, None
    while True:
        mid = get_middle(start, end)
        if is_possible(robot, cashiers, mid):
            end = mid
        else:
            start = mid
        print(start, end)
        if end is not None and end-start == 1:
            break

    if is_possible(robot, cashiers, start):
        return start
    else:
        return end


def get_middle(start, end):
    if end is None:
        return start*2
    else:
        return (start+end)//2


def is_possible(robot: Robot, cashiers: List[Cashier], limit: int) -> int:
    max_time = []
    for cashier in cashiers:
        if cashier.scan < limit:
            valid = (limit-cashier.scan)//cashier.package
            max_time.append(min(valid, cashier.maximum))
    max_time.sort(reverse=True)
    print(max_time, robot)
    return sum(max_time[:robot.robot]) >= robot.bit


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


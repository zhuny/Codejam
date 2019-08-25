import bisect
import math


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def angle(p):
    return math.atan2(p[1], p[0])


def construct_path(slots):
    coding = 0
    eating = sum(slot[1] for slot in slots)
    path = [(coding, eating)]
    for slot in slots:
        coding += slot[0]
        eating -= slot[1]
        path.append((coding, eating))
    return path


def search_path(path, x):
    index = bisect.bisect_left(path, (x, 0))
    if path[index][0] == x:
        return path[index][1]

    left = x-path[index-1][0]
    right = path[index][0]-x
    return (right*path[index-1][1]+left*path[index][1])/(left+right)


def do_one_step():
    D, S = get_ints()
    slots = [get_ints() for _ in range(S)]
    slots.sort(key=angle)

    upper = construct_path(slots)
    total_coding = upper[-1][0]
    total_eating = upper[0][1]

    answer = []
    for _ in range(D):
        coding, eating = get_ints()
        day = False
        if 0 <= coding <= total_coding:
            if 0 <= eating <= total_eating:
                if eating <= search_path(upper, coding):
                    day = True
        if day:
            answer.append('Y')
        else:
            answer.append('N')

    return ''.join(answer)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


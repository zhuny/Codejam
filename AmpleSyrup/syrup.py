# @Date    : 2017-04-30 18:06:18
# @Author  : Jihun Yang (zhuny@kaist.ac.kr)
# @File    : syrup.py


import math


def get_ints():
    return list(map(int, input().split()))


def get_max_value(L, n):
    if n <= len(L):
        L = [e[0]*e[1]*2 for e in L]
        L.sort(reverse=True)
        return sum(L[:n])
    else:
        return 0


def do_cal():
    N, K = get_ints()
    pancakes = [get_ints() for i in range(N)]
    pancakes.sort()

    previous = []
    maximum = 0

    for pancake in pancakes:
        rad, hei = pancake
        pre_max = get_max_value(previous, K-1)
        pre_max += rad*rad + 2*rad*hei
        maximum = max(maximum, pre_max)

        previous.append(pancake)

    print ("%.8f" % (maximum*math.pi))



def main():
    n = int(input())

    for i in range(n):
        print ("Case #%d: "%(i+1), end="")
        do_cal()


if __name__ == "__main__":
    main()



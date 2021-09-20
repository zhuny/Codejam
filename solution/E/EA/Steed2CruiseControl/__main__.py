# @Date    : 2017-04-23 01:18:29
# @Author  : Jihun Yang (zhuny@kaist.ac.kr)
# @File    : Steed2CruiseControl - __main__.py


def get_ints():
    return map(int, input().split())


def do_cal():
    total, n = get_ints()

    times = []

    for i in range(n):
        initial, speed = get_ints()
        times.append((total - initial)/speed)

    print ("%.7f" % (total/max(times)))


def main():
    n = int(input())

    for i in range(n):
        print ("Case #%d: "%(i+1), end="")
        do_cal()


if __name__ == "__main__":
    main()



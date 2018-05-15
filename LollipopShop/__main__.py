import itertools


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def do_one_step():
    n = get_int()

    prop = {}
    for i in range(n):
        prop[i] = 0

    def get_it(pop):
        return prop.get(pop, n)

    for i in range(n):
        prepers = get_ints()
        prepers.pop(0)

        for pop in prepers:
            if pop in prop:
                prop[pop] += 1

        if len(prepers) == 0:
            print(-1)

        else:
            sell = min(prepers, key=get_it)
            if sell in prop:
                print(sell)
                prop.pop(sell)
            else:
                print(-1)


def main():
    n = get_int()
    for i in range(1, n+1):
        do_one_step()


if __name__ == "__main__":
    main()


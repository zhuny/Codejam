import collections


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
    U = get_int()
    responses = [
        get_line().split()[1]
        for i in range(10000)
    ]
    result = []

    alphabet = set()
    for resp in responses:
        alphabet.update(resp)
    for resp in responses:
        alphabet.discard(resp[0])
    result.append(alphabet.pop())

    count = collections.Counter()
    for resp in responses:
        count[resp[0]] += 1
    for alpha, freq in count.most_common(9):
        result.append(alpha)
    return "".join(result)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


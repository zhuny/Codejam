import collections
import sys


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def print_out(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


def get_less(valids, index):
    count = collections.defaultdict(list)
    for valid in valids:
        stand = get_pos(valid, index)
        count[stand].append(valid)

    def item_key(item):
        return len(item[1])

    return min(count.items(), key=item_key)


def get_pos(th, index):
    pos = th*5+index+1
    print_out(pos)
    return get_line()


def do_one_step():
    valids = list(range(119))
    stands = []
    for i in range(3):
        infreq, valids = get_less(valids, i)
        stands.append(infreq)

    assert len(valids) == 1
    for pos in valids:
        stands.append(get_pos(pos, 4))
        stands.append(get_pos(pos, 3))

    print_out("".join(stands))
    is_answer = get_line()
    assert is_answer == 'Y'


def main():
    n, f = get_ints()
    for i in range(1, n+1):
        do_one_step()


if __name__ == "__main__":
    main()



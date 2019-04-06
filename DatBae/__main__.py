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


def print_it(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


def get_bit_seq(nums, phase):
    bit_seq = [
        int((num//phase) % 2)
        for num in range(nums)
    ]
    bit_seq = [str(num) for num in bit_seq]
    print_it("".join(bit_seq))
    return get_line()


def get_count_group(bit_seq):
    c_count = 0
    c_bit = '0'

    for index, bit in enumerate(bit_seq):
        if c_bit != bit:
            c_bit = bit
            c_count += 16
        yield c_count, index


def do_one_step():
    N, B, F = get_ints()

    split16 = get_bit_seq(N, 16)
    seq = [(num, get_bit_seq(N, num)) for num in [8, 4, 2, 1]]

    current = 0
    broken = []
    for machine, index in get_count_group(split16):
        for num, bits in seq:
            if bits[index] == '1':
                machine += num
        broken.extend(range(current, machine))
        current = machine+1
    broken.extend(range(current, N))

    print_it(" ".join([
        str(num) for num in broken
    ]))

    result = get_int()


def main():
    n = get_int()
    for i in range(1, n+1):
        do_one_step()


if __name__ == "__main__":
    main()


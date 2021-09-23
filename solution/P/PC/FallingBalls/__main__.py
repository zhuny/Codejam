def get_int():
    return int(input())

def get_line():
    return input().strip()

def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def set_tile(plate, width, x, y, tile):
    while len(plate) <= y:
        plate.append(['.']*width)

    plate[y][x] = tile


def do_one_step():
    C = get_int()
    Bs = get_ints()

    current = 0
    partition = []

    if Bs[0] == 0 or Bs[-1] == 0:
        print("IMPOSSIBLE")
        return

    for i, b in enumerate(Bs):
        if b != 0:
            end = current+b-1
            partition.append((current, end, i))
            current = current+b

    tiles = []
    for start, end, target in partition:
        if start < target:
            for i in range(target-start):
                set_tile(
                    tiles, C,
                    start+i, i, '\\'
                )
        if target < end:
            for i in range(end-target):
                set_tile(
                    tiles, C,
                    end-i, i, '/'
                )

    print(len(tiles)+1)
    for row in tiles:
        print("".join(row))
    print('.'*C)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: " % i, end="")
        do_one_step()


if __name__ == "__main__":
    main()
    # v 1.4


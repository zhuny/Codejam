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
    R, S = get_ints()
    pos = [1]*(R*S)
    pos.reverse()

    seq = []

    while len(pos) > R+1:
        seq.append((sum(pos[-2:]), sum(pos[-R-1:-2])))
        for i in range(2):
            if len(pos) > R:
                last = pos.pop()
                pos[-R] += last
    if len(pos) == R+1:
        seq.append((pos[-1], R*S-pos[0]-pos[-1]))

    show = True

    if show:
        pos2 = list(range(R))*S
    else:
        pos2 = []

    print(len(seq))

    if show:
        print(pos2)
    for start, end in seq:
        print(start, end)
        if show:
            pos2 = pos2[start:start+end] + pos2[:start] + pos2[start+end:]
            print(pos2)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: " % i, end="")
        do_one_step()


if __name__ == "__main__":
    main()

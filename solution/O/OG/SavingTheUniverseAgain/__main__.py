def do_one_step():
    threshold, prog = get_line()
    threshold = int(threshold)
    damage = 1
    total = []
    for char in prog:
        if char == 'C':
            damage <<= 1
        elif char == 'S':
            total.append(damage)

    count = 0
    while total and threshold < sum(total):
        max_damage = max(total)
        if max_damage == 1:
            break
        total.remove(max_damage)
        total.append(max_damage/2)
        count += 1

    if threshold >= sum(total):
        print(count)
    else:
        print("IMPOSSIBLE")


def get_int():
    return int(input())


def get_line():
    return input().split()


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: "%i, end="")
        do_one_step()


if __name__ == "__main__":
    main()


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
    N, P = get_ints()
    players = get_ints()

    # count sort를 구현해 뒀는데, 사실 builtins를 써도 상관없음
    # TLE가 나는건 밑에서 before.pop(0)같은 코드를 짜둬서 그렇다.
    count_list = [0 for i in range(10001)]
    for player in players:
        count_list[player] += 1
    current = 0
    for index, count in enumerate(count_list):
        for i in range(current, current+count):
            players[i] = index
        current += count

    total_sum = 0
    min_value = []
    for index, player in enumerate(players, 1):
        total_sum += player
        if index >= P:
            min_value.append(player*P-total_sum)
            total_sum -= players[index-P]

    return min(min_value)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


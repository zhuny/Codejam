def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def max_area_hist(histogram):
    if len(histogram) == 0:
        return 0

    stack = []
    area = 0

    for index, elem in enumerate(histogram+[0]):
        while stack and stack[-1] > elem:
            pindex, pelem = stack.pop()
            area = max(area, (index-pindex)*pelem)

        if stack and stack[-1] <= elem:
            stack.append((index, elem))

    return area


def do_one_step():
    R, C, K = get_ints()

    before = [-K-1 for j in range(C)]
    count = [0 for j in range(C)]

    max_area = 1

    for i in range(R):
        current = get_ints()
        for j in range(C):
            if before[j] == current[j]:
                count[j] += 1
            else:
                count[j] = 1

        row_prev = []
        for j in range(C):
            if j > 0 and current[j] == current[j-1]:
                row_prev.append(count[j])
            else:
                max_area = max(max_area, max_area_hist(row_prev))
                row_prev = [count[j]]

        if row_prev:
            max_area = max(max_area, max_area_hist(row_prev))

        before = current
        print(count)

    return max_area


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


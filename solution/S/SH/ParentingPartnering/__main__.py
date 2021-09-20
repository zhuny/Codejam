# @Date    : 2017-04-30 20:02:24
# @Author  : Jihun Yang (zhuny@kaist.ac.kr)
# @File    : parent.py


def get_ints():
    return list(map(int, input().split()))


def cycle(L):
    if len(L) > 1:
        bef = L[-1]
        for i in L:
            yield bef, i
            bef = i


def can_merge(st, en, li):
    if st < en:
        for ost, oen in li:
            if st < ost and oen < en:
                return False
        return True

    else:
        return can_merge(st-1440, en, li) and can_merge(st, en+1440, li)


def mergable(L1, L2):
    L1.sort()

    L1_total = sum([e[1]-e[0] for e in L1])
    remaind = 60*12 - L1_total

    term = [((aft[0]-bef[1])%1440, bef[1], aft[0]) for bef, aft in cycle(L1)]
    term.sort()
    count = 0

    for t, st, en in term:
        if remaind >= t:
            if can_merge(st, en, L2):
                remaind -= t
                count += 1
        else:
            break

    return count




def do_cal():
    A_c, A_j = get_ints()

    ac_list = [get_ints() for i in range(A_c)]
    aj_list = [get_ints() for i in range(A_j)]

    A_c -= mergable(ac_list, aj_list)
    A_j -= mergable(aj_list, ac_list)

    print (max(A_c,A_j)*2)



def main():
    n = int(input())

    for i in range(n):
        print ("Case #%d: "%(i+1), end="")
        do_cal()





if __name__ == "__main__":
    main()



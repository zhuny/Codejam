# @Date    : 2017-04-30 19:01:59
# @Author  : Jihun Yang (zhuny@kaist.ac.kr)
# @File    : core.py



def get_ints():
    return list(map(int, input().split()))

def get_floats():
    return list(map(float, input().split()))


def do_cal():
    N, K = get_ints()
    U = get_floats()[0]
    P = get_floats()
    P.sort()

    P_remain = P[:-K]
    P = P[-K:]

    T = U+sum(P)
    new_P = []

    while P:
        M = T/len(P)
        if M >= P[-1]:
            M = min(M, 1.0)
            for i in P:
                new_P.append(M)
            T = 0.0
            break
        else:
            cur = P.pop()
            T -= cur
            new_P.append(cur)

    P_remain.extend(new_P)
    prob = [1.0]

    for p in P_remain:
        p_inv = 1-p
        prob_o = [p*p_prev for p_prev in prob]
        prob_x = [p_inv*p_prev for p_prev in prob]

        prob_o.insert(0, 0.0)
        prob_x.append(0.0)

        prob = [x+y for x,y in zip(prob_o, prob_x)]

    print ("%.8f" % sum(prob[K:]))



def main():
    n = int(input())

    for i in range(n):
        print ("Case #%d: "%(i+1), end="")
        do_cal()




if __name__ == "__main__":
    main()



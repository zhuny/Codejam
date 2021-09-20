import math


def do_one_step():
    area = get_float()
    root2 = math.sqrt(2)

    print()
    if area < root2:
        area_ = math.sqrt(2-area*area)
        co = (area+area_)/4
        si = (area-area_)/4
        print(co, si, 0)
        print(-si, co, 0)
        print(0, 0, 0.5)
    else:
        area_ = math.sqrt(3-area*area)
        co = (area+root2*area_)/6
        si = (root2*area-area_)/6
        root2_4 = root2/4
        print(root2_4, root2_4*si, -root2_4*co)
        print(-root2_4, root2_4*si, -root2_4*co)
        print(0, co, si)

def get_int():
    return int(input())

def get_float():
    return float(input())

def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s:"%i, end=" ")
        do_one_step()


if __name__ == "__main__":
    main()


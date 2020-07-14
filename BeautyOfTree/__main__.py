def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class OneBeautyResult:
    def __init__(self, cycle, beauty):
        self.cycle = cycle
        self.beauty = beauty


class BeautyResult:
    def __init__(self, size, amadea_result, bilva_result, beauty_total):
        self.size = size
        self.beauty_one = [amadea_result, bilva_result]
        self.beauty_total = beauty_total


class Tree:
    def __init__(self):
        self.children = []

    def update_cycle(self, cycle, prev_cycle):
        for i, prev_value in enumerate(prev_cycle, -1):
            cycle[i] += prev_value

    def merge_one_beauty(self, size, cycle_length, child_one_beauty, index):
        beauty_total = sum(child.size*child.beauty_one[index].beauty for child in child_one_beauty)
        beauty_total += sum(child.beauty_one[index].cycle[0] for child in child_one_beauty)+1

        cycle = [0]*cycle_length
        for child in child_one_beauty:
            self.update_cycle(cycle, child.beauty_one[index].cycle)
        cycle[-1] += 1

        return OneBeautyResult(cycle, beauty_total/size)

    def merge_two_beauty(self, size, children_beauty):
        # 두 명이 같은 subtree에서 고른 경우
        beauty_total = sum(child.size*child.size*child.beauty_total for child in children_beauty)
        # 한 명이 이 subtree인 경우 다른 한 명이 이 subtree를 고르지 않을 때
        beauty_total += sum(
            child.size*(size-child.size)*(child.beauty_one[0].beauty+child.beauty_one[1].beauty)
            for child in children_beauty
        )
        # 누군가가 현재의 노드를 선택했을 경우
        beauty_total += size*size
        beauty_total -= sum(
            child.size-child.beauty_one[0].cycle[0] for child in children_beauty  # amadea가 색칠 안하는 경우
        ) * sum(
            child.size-child.beauty_one[1].cycle[0] for child in children_beauty  # bilva가 색칠 안하는 경우
        )

        return beauty_total / (size*size)

    def get_beauty(self, amadea, bilva):
        """
        :param amadea: step of amadea
        :param bilva: step of bilva
        :return:
            1. Beauty Only For Amadea
            2. Beauty Only For Bilva
            3. Beauty of them
        """
        children_beauty = [child.get_beauty(amadea, bilva) for child in self.children]

        size = sum(child.size for child in children_beauty)+1

        return BeautyResult(
            size=size,
            amadea_result=self.merge_one_beauty(size, amadea, children_beauty, 0),
            bilva_result=self.merge_one_beauty(size, bilva, children_beauty, 1),
            beauty_total=self.merge_two_beauty(size, children_beauty)
        )


def do_one_step():
    N, B, C = get_ints()

    root = Tree()
    tree_list = [None, root]
    for v in get_ints():
        current = Tree()
        tree_list[v].children.append(current)
        tree_list.append(current)

    return root.get_beauty(B, C).beauty_total


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %.7f" % (i, do_one_step()))


if __name__ == "__main__":
    main()


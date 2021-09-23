import collections


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class Trie:
    def __init__(self):
        self.mapping = collections.defaultdict(Trie)
        self.end = False

    def insert(self, word):
        current = self
        for char in word:
            current = current.mapping[char]
        current.end = True

    def get_max_size(self, root=True):
        '''
        :return: remaind, # of pair
        '''
        remaind_num = pair_num = 0
        for child in self.mapping.values():
            remaind, pair = child.get_max_size(False)
            remaind_num += remaind
            pair_num += pair
        if not root:
            if self.end:
                remaind_num += 1
            if remaind_num >= 2:
                remaind_num -= 2
                pair_num += 2
        return remaind_num, pair_num


def do_one_step():
    n = get_int()
    trie = Trie()
    for _ in range(n):
        word = get_line()
        trie.insert(word[::-1])
    return trie.get_max_size()[1]


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


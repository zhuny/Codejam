def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


def has_cycle(creator):
    queue = {0}
    done = set()

    while queue:
        cur = queue.pop()
        if cur in done:
            continue
        done.add(cur)

        queue.update(creator[cur])
        if 0 in queue:
            return True

    return False


def is_reachable(creator, index, cache):
    done = set()
    queue = {index}

    while queue:
        cur = queue.pop()
        if cur in cache and cache[cur]:
            cache[index] = True
            return True

        if cur in done:
            continue
        done.add(cur)
        queue.update(creator[cur])


def do_one_step_total():
    n = get_int()
    creator = [[j-1 for j in get_ints()] for i in range(n)]
    world = get_ints()

    cache = {}
    for index, count in enumerate(world):
        if count > 0:
            if index > 0:
                if is_reachable(creator, index, cache):
                    return
            elif has_cycle(creator):
                return

    return world[0]


def do_one_step():
    result = do_one_step_total()
    if result is None:
        return "UNBOUNDED"
    else:
        return result


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


def get_int():
    return int(input())


def get_line():
    return input().strip()


def get_ints():
    return [
        int(i)
        for i in input().split()
    ]


class Plate:
    def __init__(self, body):
        self.body = tuple(body)

    @property
    def width(self):
        return len(self.body)

    @property
    def height(self):
        if self.width > 0:
            return len(self.body[0])
        return 0

    def __hash__(self):
        return hash(self.body)

    def __eq__(self, other):
        return self.body == other.body

    def get_empty(self):
        for i, row in enumerate(self.body):
            for j, cell in enumerate(row):
                if cell == '.':
                    yield i, j

    def check_move(self, x, y, dx, dy):
        while 0 <= x < self.width and 0 <= y < self.height:
            cell = self.body[x][y]
            if cell == '#':
                return False
            elif cell == '.':
                x += dx
                y += dy
            else:
                break
        return True

    def _put_bac(self, plate, width, height, x, y, dx, dy):
        x += dx
        y += dy
        while 0 <= x < width and 0 <= y < height:
            if plate[x][y] != '.':
                break
            plate[x][y] = '-'
            x += dx
            y += dy

    def put_bac(self, x, y, direct):
        w, h = self.width, self.height
        body = [list(row) for row in self.body]
        body[x][y] = '-'
        if direct:
            self._put_bac(body, w, h, x, y, 1, 0)
            self._put_bac(body, w, h, x, y, -1, 0)
        else:
            self._put_bac(body, w, h, x, y, 0, 1)
            self._put_bac(body, w, h, x, y, 0, -1)
        return Plate(["".join(row) for row in body])

    def is_valid_pos(self, x, y, direct):
        if direct:
            return (
                self.check_move(x, y, 1, 0) and
                self.check_move(x, y, -1, 0)
            )
        else:
            return (
                self.check_move(x, y, 0, 1) and
                self.check_move(x, y, 0, -1)
            )

    def _is_change_win(self, cache, x, y, direct):
        if self.is_valid_pos(x, y, direct):
            plate = self.put_bac(x, y, direct)
            if plate.is_winnerable(cache):
                return False
            else:
                return True
        return False

    def _is_winnerable(self, cache, counted):
        wrap = False, True
        result = 0
        for i, j in self.get_empty():
            for direct in wrap:
                if self._is_change_win(cache, i, j, direct):
                    if counted:
                        result += 1
                    else:
                        return 1
        return result

    def is_winnerable(self, cache, counted=False):
        if self in cache:
            return cache[self]

        result = self._is_winnerable(cache, counted)
        cache[self] = result
        return result


def do_one_step():
    H, W = get_ints()
    plates = Plate([get_line() for i in range(H)])
    cache = {}
    return plates.is_winnerable(cache, True)


def main():
    n = get_int()
    for i in range(1, n+1):
        print("Case #%s: %s" % (i, do_one_step()))


if __name__ == "__main__":
    main()


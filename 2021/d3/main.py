class NotFound(Exception):
    pass


class Grid:

    def __init__(self, rows):
        self.rows = rows
        self.nb_lines = len(rows)
        self.nb_columns = len(rows)
        self.marked = list()

    def get_elt(self, x, y):
        return self.rows[x][y]

    def iter_over_rows(self):
        return [
            self.get_elt(i, j)
            for i in range(self.nb_lines)
            for j in range(self.nb_columns)
        ]

    def check_number(self, number):
        for i in range(self.nb_lines):
            for j in range(self.nb_columns):
                if self.get_elt(i, j) == number:
                    return (i, j)

        raise NotFound()

    def set_elt(self, x, y, value):
        self.rows[x][y] = value

    def digest(self, number):
        try:
            x, y = self.check_number(number)
        except NotFound:
            return

        self.set_elt(x, y, 'x')
        self.marked.append(number)

    def is_complete(self):
        for i in range(self.nb_lines):
            for j in range(self.nb_columns):
                if self.get_elt(i, j) == 'x':
                    continue
                else:
                    break
            else:
                return True

        for i in range(self.nb_columns):
            for j in range(self.nb_lines):
                if self.get_elt(j, i) == 'x':
                    continue
                else:
                    break
            else:
                return True

        return False


def get_inputs(filename):
    with open(filename) as fd:
        numbers = fd.readline().strip('\n').split(',')
        numbers = list(map(lambda x: int(x), numbers))
        grids = []
        rows = []
        for line in fd.readlines():
            if line == '\n':
                if rows != []:
                    grid = Grid(rows.copy())
                    grids.append(grid)
                    rows = []
                continue

            rows.append(
                list(
                    map(
                        lambda x: int(x),
                        filter(lambda x: x != '', line.strip('\n').split(' ')),
                    ),
                ),
            )

        grids.append(Grid(rows.copy()))

    return numbers, grids


def get_result(grid):
    not_in = list(filter(lambda x: x != 'x', grid.iter_over_rows()))
    return sum(not_in) * grid.marked[-1]


numbers, grids = get_inputs('inputs.txt')


def main(numbers, grids):
    completed = []
    while len(grids) > 0 and len(numbers) > 0:
        current_number = numbers.pop(0)
        tmp = []

        while len(grids):
            grid = grids.pop()
            grid.digest(current_number)
            if grid.is_complete():
                completed.append(grid)
            else:
                tmp.append(grid)

        grids = tmp

    return completed


completed = main(numbers, grids)
print(get_result(completed[-1]))

import sys
import typing as T
from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int


@dataclass
class Point:
    coordinate: Coordinate
    line_passages: int = 0

    def mark(self):
        self.line_passages += 1


@dataclass
class Line:
    start: Point
    end: Point

    def trace(self):
        if self.start.coordinate.y == self.end.coordinate.y:
            start_x, end_x = (
                min(self.start.coordinate.x, self.end.coordinate.x),
                max(self.start.coordinate.x, self.end.coordinate.x),
            )
            return [
                Point(Coordinate(x=i, y=self.start.coordinate.y))
                for i in range(start_x, end_x + 1)
            ]

        if self.start.coordinate.x == self.end.coordinate.x:
            start_y, end_y = (
                min(self.start.coordinate.y, self.end.coordinate.y),
                max(self.start.coordinate.y, self.end.coordinate.y),
            )
            return [
                Point(Coordinate(x=self.start.coordinate.x, y=i))
                for i in range(start_y, end_y + 1)
            ]

        forward = self.start.coordinate.x < self.end.coordinate.x
        increase = self.start.coordinate.y < self.end.coordinate.y

        start_x = self.start.coordinate.x if forward else self.end.coordinate.x
        end_x = self.end.coordinate.x if forward else self.start.coordinate.x

        return [
            Point(
                Coordinate(
                    self.start.coordinate.x + i if forward else self.start.coordinate.x - i,
                    self.start.coordinate.y + i if increase else self.start.coordinate.y - i,
                ),
            ) for i in range(end_x - start_x + 1)
        ]


@dataclass
class MapV1:
    nb_lines: int
    nb_columns: int
    points: T.List[Point] = None

    def populate(self):
        self.points = list()
        for i in range(self.nb_lines):
            row = []
            for j in range(self.nb_columns):
                row.append(0)
            self.points.append(row)

    def count_save_points(self):
        count = 0
        for row in self.points:
            for point in row:
                if point >= 2:
                    count += 1

        return count

    def check(self, line):
        for point in line.trace():
            self.points[point.coordinate.y][point.coordinate.x] += 1

    def print(self):
        for row in self.points:
            for point in row:
                if point == 0:
                    sys.stdout.write('.')
                else:
                    sys.stdout.write(str(point))
                sys.stdout.flush()

            sys.stdout.write('\n')


def split_to_int(string):
    x, y = string.split(',')
    return int(x), int(y)


def get_inputs(filename) -> T.List[Line]:
    with open(filename) as fd:
        lines = []
        max_x, max_y = (0, 0)
        for line in fd.readlines():
            line = line.strip('\n')
            start, end = line.split(' -> ')
            start_x, start_y = split_to_int(start)
            end_x, end_y = split_to_int(end)
            max_x = max(max_x, start_x, end_x)
            max_y = max(max_y, start_y, end_y)
            lines.append(
                Line(
                    start=Point(Coordinate(x=start_x, y=start_y)),
                    end=Point(Coordinate(x=end_x, y=end_y)),
                ),
            )

        return max_x + 1, max_y + 1, lines


def main():
    nb_columns, nb_lines, lines = get_inputs('inputs.txt')
    map_v1 = MapV1(nb_lines, nb_columns)
    map_v1.populate()
    for line in lines:
        try:
            map_v1.check(line)
        except IndexError:
            print(line)
            print(line.trace())
    map_v1.print()
    print(map_v1.count_save_points())


main()

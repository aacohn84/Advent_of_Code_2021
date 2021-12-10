# how do I tell if two line segments intersect?
#
# a line is defined by x1,y1 -> x2,y2
# ex: (0,0) -> (0,10)
# or: (0,10) -> (0,0) these two pairs of coordinates represent the same line segment
#
# case 1: perpendicular lines
#   two lines are perpendicular if one is horizontal and the other is vertical
#   a horizontal line H is one where y1 == y2
#   a vertical line V is one where x1 == x2
#   perpendicular lines intersect if:
#       V.x between H.x1 and H.x2, and 
#       H.y between V.y1 and V.y2
#   for 3 non-negative integers: a, b, and c, we can say that c is between a and b inclusively if:
#       (c - a) * (b - c) >= 0
#   perpendicular lines intersect at most once
#   if they intersect, the point of intersection is: (H.x, V.y)
#
# case 2: parallel lines
#   two lines are parallel if they are both horizontal or both vertical
#   parallel lines intersect if:
#       case 1: horizontal
#           H1.y == H2.y and...
#           H1.x1 is between H2.x1 and H2.x2, or
#           H1.x2 is between H2.x1 and H2.x2

from enum import Enum

class Point:
    def __init__(self, coord_str):
        [self.x, self.y] = list(int(s) for s in coord_str.split(','))

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y
    
    def __str__(self):
        return str(self.x) + ',' + str(self.y)
    
    def __repr__(self):
        return str(self)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.type = LineType.get_line_type(self)

    def __eq__(self, rhs):
        return (self.p1 == rhs.p1 and self.p2 == rhs.p2 \
            or self.p1 == rhs.p2 and self.p2 == rhs.p1) \
            and self.type == rhs.type

    def __str__(self):
        return str(self.p1) + ' -> ' + str(self.p2) + ' (' + str(self.type) + ')\n'

    def __repr__(self):
        return str(self)

class LineType(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'
    DIAGONAL = 'diagonal'

    @staticmethod
    def get_line_type(line):
        if line.p1.x == line.p2.x:
            return LineType.VERTICAL
        elif line.p1.y == line.p2.y:
            return LineType.HORIZONTAL
        else:
            return LineType.DIAGONAL

def process_input_line(line_str):
    [coord1_str, coord2_str] = line_str.strip().split('->')
    p1 = Point(coord1_str)
    p2 = Point(coord2_str)
    return Line(p1, p2)

def read_input(filename):
    f = open(filename, 'r')
    return list(process_input_line(line) for line in f.readlines())

def get_num_intersections(lines):
    all_points = {}
    intersection_points = set()
    def add_point(x, y):
        p = (x, y)
        if p not in all_points:
            all_points[p] = 1
        else:
            all_points[p] += 1
            intersection_points.add(p)

    for line in lines:
        if line.type == LineType.HORIZONTAL:
            lo = min(line.p1.x, line.p2.x)
            hi = max(line.p1.x, line.p2.x)
            for x in range(lo, hi + 1):
                add_point(x, line.p1.y)
        elif line.type == LineType.VERTICAL:
            lo = min(line.p1.y, line.p2.y)
            hi = max(line.p1.y, line.p2.y)
            for y in range(lo, hi + 1):
                add_point(line.p1.x, y)
        else:
            x_step = -1 if line.p1.x > line.p2.x else 1
            y_step = -1 if line.p1.y > line.p2.y else 1
            x = line.p1.x
            y = line.p1.y
            while x != line.p2.x and y != line.p2.y:
                add_point(x, y)
                x += x_step
                y += y_step
            add_point(x, y)
    return len(intersection_points)

def main():
    lines = read_input('05 - Input.txt')
    non_diagonal_lines = list(filter(lambda line: line.type != LineType.DIAGONAL, lines))
    intersections_1 = get_num_intersections(non_diagonal_lines)
    print('part1 result: ' + str(intersections_1))
    intersections_2 = get_num_intersections(lines)
    print('part1 result: ' + str(intersections_2))

def test_read_input():
    print('test_read_input')
    output = read_input('05 - Test Input.txt')
    expected = [Line(Point('0,9'), Point('5,9')),
        Line(Point('8,0'), Point('0,8')),
        Line(Point('9,4'), Point('3,4')),
        Line(Point('2,2'), Point('2,1')),
        Line(Point('7,0'), Point('7,4')),
        Line(Point('6,4'), Point('2,0')),
        Line(Point('0,9'), Point('2,9')),
        Line(Point('3,4'), Point('1,4')),
        Line(Point('0,0'), Point('8,8')),
        Line(Point('5,5'), Point('8,2'))]
    print('Expect: ' + str(expected))
    print('Actual: ' + str(output))
    assert(expected == output)

def test_part1():
    print('test_part1')
    lines = read_input('05 - Test Input.txt')
    non_diagonal_lines = list(filter(lambda line: line.type != LineType.DIAGONAL, lines))
    num_intersection_points = get_num_intersections(non_diagonal_lines)
    print('expect: ' + str(5))
    print('actual: ' + str(num_intersection_points))
    assert(num_intersection_points == 5)

def test_part2():
    print('test_part2')
    lines = read_input('05 - Test Input.txt')
    num_intersection_points = get_num_intersections(lines)
    print('expect: ' + str(12))
    print('actual: ' + str(num_intersection_points))
    assert(num_intersection_points == 12)

def run_tests():
    test_read_input()
    test_part1()
    test_part2()

#run_tests()
main()
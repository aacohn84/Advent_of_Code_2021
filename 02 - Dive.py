class Instruction:
    def __init__(self, direction, magnitude):
        self.direction = direction
        self.magnitude = int(magnitude)

    def get_direction(self):
        return self.direction

    def get_magnitude(self):
        return self.magnitude

def get_directions(filename):
    def process_input(s):
        l = s.strip().split()
        return Instruction(l[0], l[1])

    f = open(filename, 'r')
    return list(map(process_input, f.readlines()))

def main():
    directions = get_directions('02 - Directions.txt')
    print_part1_result(directions)
    print_part2_result(directions)

def print_part1_result(directions):
    depth = 0
    displacement = 0
    for d in directions:
        if d.direction == 'forward':
            displacement += d.magnitude
        elif d.direction == 'down':
            depth += d.magnitude
        else:
            depth -= d.magnitude
    print(str(depth * displacement))

def print_part2_result(directions):
    depth = 0
    displacement = 0
    aim = 0
    for d in directions:
        if d.direction == 'forward':
            displacement += d.magnitude
            if aim != 0:
                depth += d.magnitude * aim
        elif d.direction == 'down':
            aim += d.magnitude
        else:
            aim -= d.magnitude
    print(str(depth * displacement))

main()
# the horizontal positions of crabs are given
# we need to find the horizontal position with the least cumulative distance to all crabs
# naturally, the cheapest solution is to avoid moving as many crabs as possible
# therefore, we must find the point where the density of crabs is the highest
# map out the number of crabs per horizontal position. that is the "weight" of the position.
# 
# what I need to do:
# determine cost of each position
# choose the position with the minimum cost
# in order to make this fast, I can implement a couple of optimizations:
# -- do not check all positions. we should only check within the bounds of where the crabs are located.
# -- when calculating the cost of a position, stop calculating if it goes over the lowest known cost
# The algorithm is basically the same as finding the smallest element of a list
# we just have to be judicious about which elements we choose to look at.
# maybe we can narrow down the set even further by only looking at points that are between the maximum crabs

class Position:
    def __init__(self, idx):
        self.idx = idx
        self.crabs = 1

    def __str__(self):
        return str.format("({idx}, {crabs})", 
        idx = self.idx, crabs = self.crabs)

    def __repr__(self):
        return str(self)

def read_input(filename):
    f = open(filename, 'r')
    line = f.readline()
    return list(int(s) for s in line.split(','))

def crabs_per_position(positions):
    hist = {}
    for p in positions:
        if p not in hist:
            hist[p] = Position(p)
        else:
            hist[p].crabs += 1
    return hist

def cost_to_move(to_pos, from_pos_w_crabs):
    dist = abs(to_pos - from_pos_w_crabs.idx)
    cost = dist * from_pos_w_crabs.crabs
    return cost

def cost_to_move_2(to_pos, from_pos_w_crabs):
    dist = abs(to_pos - from_pos_w_crabs.idx)
    dist = int((dist / 2.0) * (dist + 1.0))
    cost = dist * from_pos_w_crabs.crabs
    return cost

def cost_to_align(targ_pos, positions, cost_fn, cost_threshold = 0):
    cost = 0
    if cost_threshold == 0:
        return sum(cost_fn(targ_pos, curr_pos) for curr_pos in positions)
    else:
        for curr_pos in positions:
            cost += cost_fn(targ_pos, curr_pos)
            if cost >= cost_threshold:
                return cost_threshold + 1
        return cost

def part1():
    algo('07 - Input.txt', cost_to_move)

def part2():
    algo('07 - Input.txt', cost_to_move_2)

def algo(filename, cost_fn):
    positions = read_input(filename)
    left_bound = min(positions)
    right_bound = max(positions)
    positions = crabs_per_position(positions).values()
    min_cost = cost_to_align(left_bound, positions, cost_fn)
    min_cost_position = left_bound
    for position in range(left_bound + 1, right_bound + 1):
        cost = cost_to_align(position, positions, cost_fn, min_cost)
        if cost < min_cost:
            min_cost = cost
            min_cost_position = position
    print(str.format("Position:   {p}\nCost:     {c}", p = min_cost_position, c = min_cost))
    print('output: ' + str(min_cost_position))

def test_part1():
    algo('07 - Test Input.txt', cost_to_move)

def test_part2():
    algo('07 - Test Input.txt', cost_to_move_2)

#test_part1()
#test_part2()
#part1()
part2()
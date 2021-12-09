def read_input(filename):
    f = open(filename, 'r')
    return list(map(lambda s: int(s), f.readline().strip().split(',')))

def sort_fish(input):
    fish_by_day = [0,0,0,0,0,0,0,0,0]
    for fish in input:
        fish_by_day[fish] += 1
    return fish_by_day

def process_cycles(fish_by_day, days_to_simulate):
    while (days_to_simulate > 0):
        fish_to_add = fish_by_day[0]
        for day in range(8):
            fish_by_day[day] = fish_by_day[day + 1]
        fish_by_day[8] = fish_to_add
        fish_by_day[6] += fish_to_add
        days_to_simulate -= 1
    return fish_by_day

def count_of_fish(fish_by_day):
    total = 0
    for count in fish_by_day:
        total += count
    return total

def part1():
    input = read_input('06 - Input.txt')
    fish_by_day = sort_fish(input)
    fish_by_day = process_cycles(fish_by_day, 80)
    print('Part 1 solution: ' + str(count_of_fish(fish_by_day)))

def part2():
    input = read_input('06 - Input.txt')
    fish_by_day = sort_fish(input)
    fish_by_day = process_cycles(fish_by_day, 256)
    print('Part 2 solution: ' + str(count_of_fish(fish_by_day)))

def test_read_input():
    print('test_read_input...')
    input = read_input('06 - Test Input.txt')
    print('expect: ' + str([3,4,3,1,2]))
    print('output: ' + str(input))
    assert(input == [3,4,3,1,2])

def test_sort_fish():
    print('test_sort_fish...')
    input = read_input('06 - Test Input.txt')
    fish_by_day = sort_fish(input)
    print('expect: ' + str([0,1,1,2,1,0,0,0,0]))
    print('output: ' + str(fish_by_day))
    assert(fish_by_day == [0,1,1,2,1,0,0,0,0])

def test_process_cycles():
    print('test_process_cycles...')
    input = read_input('06 - Test Input.txt')
    fish_by_day = sort_fish(input)
    process_cycles(fish_by_day, 18)
    print('expect: ' + str([3,5,3,2,2,1,5,1,4]))
    print('output: ' + str(fish_by_day))
    assert(fish_by_day == [3,5,3,2,2,1,5,1,4])

def test_count_of_fish():
    print('test_count_of_fish...')
    input = read_input('06 - Test Input.txt')
    fish_by_day = sort_fish(input)
    process_cycles(fish_by_day, 18)
    count = count_of_fish(fish_by_day)
    print('expect: ' + str(26))
    print('output: ' + str(count))

def test_count_of_fish_after_80_days():
    print('test_count_of_fish_after_80_days...')
    input = read_input('06 - Test Input.txt')
    fish_by_day = sort_fish(input)
    process_cycles(fish_by_day, 80)
    count = count_of_fish(fish_by_day)
    print('expect: ' + str(5934))
    print('output: ' + str(count))
    assert(count == 5934)

def test_count_of_fish_after_256_days():
    print('test_count_of_fish_after_80_days...')
    input = read_input('06 - Test Input.txt')
    fish_by_day = sort_fish(input)
    process_cycles(fish_by_day, 256)
    count = count_of_fish(fish_by_day)
    print('expect: ' + str(26984457539))
    print('output: ' + str(count))
    assert(count == 26984457539)

def run_tests():
    test_read_input()
    test_sort_fish()
    test_process_cycles()
    test_count_of_fish()
    test_count_of_fish_after_80_days()
    test_count_of_fish_after_256_days()

run_tests()
part1()
part2()
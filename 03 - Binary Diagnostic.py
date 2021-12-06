def read_input(filename):
    return open(filename, 'r').readlines()

def process_diagnostic(lines):
    return list(map(lambda s: list(s.strip()), lines))

def get_most_common_digit(diag, i):
    ones = 0
    zeroes = 0
    threshold = len(diag) / 2
    for row in diag:
        if ones > threshold or zeroes > threshold:
            break
        elif row[i] == '1': ones += 1
        else: zeroes += 1
    return ones > zeroes

def get_rows_for_digit_criteria(diag, i, most_common):
    # diag - a subset of the diagnostic report
    # i - the list position to inspect - must be between 0 and len(diag) - 1 inclusive
    # most_common - boolean
    # returns the rows with the most common digit in the 'i' position if most_common is set, or 1's if there is no most common digit
    # else, returns rows with the least common digit in the 'i' position, or 0's if there is no least common digit
    ones = []
    zeroes = []
    for row in diag:
        if row[i] == '1': ones.append(row)
        else: zeroes.append(row)
    if most_common:
        return ones if len(ones) >= len(zeroes) else zeroes
    else:
        return zeroes if len(zeroes) <= len(ones) else ones

def binary_to_decimal(b, inverse = 0):
    l = len(b)
    acc = 0
    for i in range(l - 1, -1, -1):
        p = l - 1 - i
        acc += ((b[i] + inverse) % 2) * 2**p
    return acc

def part1(diag):
    num_digits = len(diag[0])
    gamma_rate = []
    for i in range(num_digits):
        gamma_rate.append(get_most_common_digit(diag, i))
    gamma_rate_dec = binary_to_decimal(gamma_rate)
    epsilon_rate_dec = binary_to_decimal(gamma_rate, inverse=1)
    print(str(gamma_rate_dec * epsilon_rate_dec))

def get_rows_for_digit_criteria_recursive(diag, i, most_common):
    if len(diag) == 1 or i >= len(diag[0]):
        return list(map(lambda s: int(s), diag[0]))
    else:
        rows = get_rows_for_digit_criteria(diag, i, most_common)
        assert(i + 1 < len(diag[0]) or len(rows) == 1) # don't go past the end of the row
        return get_rows_for_digit_criteria_recursive(rows, i + 1, most_common)

def part2(diag):
    num_digits = len(diag[0])
    most_common = get_rows_for_digit_criteria_recursive(diag, 0, most_common=True)
    least_common = get_rows_for_digit_criteria_recursive(diag, 0, most_common=False)
    oxygen_rating = binary_to_decimal(most_common)
    c02_rating = binary_to_decimal(least_common)
    print(str(oxygen_rating * c02_rating))

def main():
    diag = process_diagnostic(read_input(('03 - Diagnostic Report.txt')))
    part1(diag)
    part2(diag)

def run_tests():
    test_binary_to_decimal()
    test_algorithm_1()
    test_algorithm_2()

def test_algorithm_1():
    input = read_input('03 - Unit Test Input.txt')
    diag = process_diagnostic(input)
    num_digits = len(diag[0])
    gamma_rate = []
    epsilon_rate = []
    for i in range(num_digits):
        gamma_rate.append(get_most_common_digit(diag, i))
        epsilon_rate.append((gamma_rate[i] + 1) % 2)
    assert(gamma_rate == [1,0,1,1,0])
    assert(epsilon_rate == [0,1,0,0,1])
    gamma_rate_dec = binary_to_decimal(gamma_rate)
    epsilon_rate_dec = binary_to_decimal(gamma_rate, inverse=1)
    assert(gamma_rate_dec * epsilon_rate_dec == 198)

def test_algorithm_2():
    input = read_input('03 - Unit Test Input.txt')
    diag = process_diagnostic(input)
    most_common = get_rows_for_digit_criteria_recursive(diag, 0, most_common=True)
    assert(most_common == [1,0,1,1,1])
    least_common = get_rows_for_digit_criteria_recursive(diag, 0, most_common=False)
    assert(least_common == [0,1,0,1,0])
    oxygen_rating = binary_to_decimal(most_common)
    assert(oxygen_rating == 23)
    c02_rating = binary_to_decimal(least_common)
    assert(c02_rating == 10)
    assert(oxygen_rating * c02_rating == 230)

def test_binary_to_decimal():
    b = [1,1,1]
    assert(binary_to_decimal(b) == 7)
    assert(binary_to_decimal(b, inverse=1) == 0)

run_tests()
main()
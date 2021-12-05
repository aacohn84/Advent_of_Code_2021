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

def binary_to_decimal(b, inverse = 0):
    l = len(b)
    acc = 0
    for i in range(l - 1, -1, -1):
        p = l - 1 - i
        acc += ((b[i] + inverse) % 2) * 2**p
    return acc

def main():
    diag = process_diagnostic(read_input(('03 - Diagnostic Report.txt')))
    num_digits = len(diag[0])
    gamma_rate = []
    for i in range(num_digits):
        gamma_rate.append(get_most_common_digit(diag, i))
    gamma_rate_dec = binary_to_decimal(gamma_rate)
    epsilon_rate_dec = binary_to_decimal(gamma_rate, inverse=1)
    print(str(gamma_rate_dec * epsilon_rate_dec))

def run_tests():
    test_binary_to_decimal()
    test_algorithm()

def test_algorithm():
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

def test_binary_to_decimal():
    b = [1,1,1]
    assert(binary_to_decimal(b) == 7)
    assert(binary_to_decimal(b, inverse=1) == 0)

run_tests()
main()
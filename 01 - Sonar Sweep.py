def read_measurements(filename):
    f = open(filename, 'r')
    return list(map(lambda s: int(s.strip()), f.readlines()))

def main():
    measurements = read_measurements("01 - Depth Measurements.txt")
    print("Increased measurements: " + str(num_increased(measurements)))
    print("Increased sliding windows: " + str(num_sliding_windows_increased(measurements)))

def num_increased(measurements):
    prev = None
    increased = 0
    for m in measurements:
        if prev is not None and prev < m:
            increased += 1
        prev = m
    return increased

def num_sliding_windows_increased(measurements):
    prev_sum = None
    stop = len(measurements)
    i, j, k = 0, 1, 2
    increased = 0
    while k < stop:
        sum = measurements[i] + measurements[j] + measurements[k]
        if prev_sum is not None and prev_sum < sum:
            increased += 1
        prev_sum = sum
        i, j, k = i + 1, j + 1, k + 1
    return increased

main()
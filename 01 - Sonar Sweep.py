def read_measurements(filename):
    f = open(filename, 'r')
    return list(map(lambda s: int(s.strip()), f.readlines()))

def main():
    measurements = read_measurements("01 - Depth Measurements.txt")
    prev = None
    increased = 0
    for m in measurements:
        if prev is not None and prev < m:
            increased += 1
        prev = m
    print(increased)

main()
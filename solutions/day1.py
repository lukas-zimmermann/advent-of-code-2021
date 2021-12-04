from input.day1 import input_measurements


def solve_day1():
    increases = number_of_increases_in_measurements(input_measurements)
    print('Solution for day 1 puzzle 1:')
    print('%d increases' % increases)

    print()

    increases = number_of_increases_in_measurements(input_measurements, 3)
    print('Solution for day 1 puzzle 2:')
    print('%d increases' % increases)


def number_of_increases_in_measurements(measurements, block_size=1):
    # if we don't have enough elements to compare anything, we cannot have any increases
    if len(measurements) <= block_size:
        return 0

    increases = 0
    for i in range(block_size, len(measurements)):
        if measurements[i] > measurements[i - block_size]:
            increases += 1

    return increases

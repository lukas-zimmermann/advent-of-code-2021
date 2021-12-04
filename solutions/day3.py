from input.day3 import input_binary_data


def solve_day3():
    gamma, epsilon = find_gamma_and_epsilon(input_binary_data)
    print('Solution for day 3 puzzle 1:')
    print('gamma: %d, epsilon: %d' % (gamma, epsilon))
    print('%d x %d = %d' % (gamma, epsilon, gamma * epsilon))

    print()

    oxygen = find_oxygen(input_binary_data)
    co2 = find_co2(input_binary_data)
    print('Solution for day 3 puzzle 2:')
    print('oxygen: %d, co2: %d' % (oxygen, co2))
    print('%d x %d = %d' % (oxygen, co2, oxygen * co2))


def find_gamma_and_epsilon(diagnostic_data):
    # initialize a list with an element for each position in the data with 0
    line_length = len(diagnostic_data[0])
    bit_count = [0] * line_length

    # we effectively count the 1s on each position
    for line in diagnostic_data:
        for position in range(0, line_length):
            bit_count[position] += int(line[position])  # increase for 1, unchanged for 0

    gamma = ''
    epsilon = ''
    data_length = len(diagnostic_data)
    for position in range(0, line_length):
        if bit_count[position] < data_length / 2:  # more than half of the lines had a 0 at this position
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2), int(epsilon, 2)


def find_oxygen(diagnostic_data, position=0):
    # count how many 1s exist on a position
    bit_count = 0
    for line in diagnostic_data:
        bit_count += int(line[position])

    # if more than half of the bits are 0, we keep the lines with a 0
    keep = '0' if bit_count < len(diagnostic_data) / 2 else '1'
    remaining_data = []

    for line in diagnostic_data:
        if line[position] == keep:
            remaining_data.append(line)

    # if there is only 1 left, we are done
    if len(remaining_data) == 1:
        return int(remaining_data[0], 2)

    # otherwise, we repeat the process for the next position with the remaining lines
    return find_oxygen(remaining_data, position + 1)


def find_co2(diagnostic_data, position=0):
    # count how many 1s exist on a position
    bit_count = 0
    for line in diagnostic_data:
        bit_count += int(line[position])

    # if more than half of the bits are 0, we keep the lines with a 1
    keep = '1' if bit_count < len(diagnostic_data) / 2 else '0'
    remaining_data = []

    for line in diagnostic_data:
        if line[position] == keep:
            remaining_data.append(line)

    # if there is only 1 left, we are done
    if len(remaining_data) == 1:
        return int(remaining_data[0], 2)

    # otherwise, we repeat the process for the next position with the remaining lines
    return find_co2(remaining_data, position + 1)

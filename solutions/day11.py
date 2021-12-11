from input.day11 import input_octopodes


def solve_day11():
    flashes = calculate_flashes_after_100_steps(input_octopodes.copy())
    print('Solution for day 11 puzzle 1:')
    print(f'flashes: {flashes}')

    print()

    steps = find_first_synchronized_flash(input_octopodes.copy())
    print('Solution for day 11 puzzle 2:')
    print(f'steps: {steps}')


def calculate_flashes_after_100_steps(octopodes):
    flashes = 0

    for i in range(0, 100):
        # step 1: increase all values by 1
        for row in range(0, len(octopodes)):
            octopodes[row] = [x + 1 for x in octopodes[row]]

        # step 2: handle all flashing octopuses and reset them to 0
        flashes += handle_flashes(octopodes)

    return flashes


def find_first_synchronized_flash(octopodes):
    steps = 0

    while sum(map(sum, octopodes)):
        # step 1: increase all values by 1
        for row in range(0, len(octopodes)):
            octopodes[row] = [x + 1 for x in octopodes[row]]

        # step 2: handle all flashing octopuses and reset them to 0
        handle_flashes(octopodes)

        steps += 1

    return steps


def handle_flashes(octopodes):
    flashes = 0
    for i in range(0, len(octopodes)):
        for j in range(0, len(octopodes[0])):
            if octopodes[i][j] > 9:
                flashes += handle_flash(octopodes, i, j)

    return flashes


def handle_flash(octopodes, i, j):
    octopodes[i][j] = 0
    flashes = 1
    max_i = len(octopodes) - 1
    max_j = len(octopodes[0]) - 1

    # top left
    if i and j and octopodes[i-1][j-1]:
        octopodes[i-1][j-1] += 1
        if octopodes[i-1][j-1] > 9:
            flashes += handle_flash(octopodes, i-1, j-1)

    # top
    if i and octopodes[i-1][j]:
        octopodes[i-1][j] += 1
        if octopodes[i-1][j] > 9:
            flashes += handle_flash(octopodes, i-1, j)

    # top right
    if i and j < max_j and octopodes[i-1][j+1]:
        octopodes[i-1][j+1] += 1
        if octopodes[i-1][j+1] > 9:
            flashes += handle_flash(octopodes, i-1, j+1)

    # right
    if j < max_j and octopodes[i][j+1]:
        octopodes[i][j+1] += 1
        if octopodes[i][j+1] > 9:
            flashes += handle_flash(octopodes, i, j+1)

    # bottom right
    if i < max_i and j < max_j and octopodes[i+1][j+1]:
        octopodes[i+1][j+1] += 1
        if octopodes[i+1][j+1] > 9:
            flashes += handle_flash(octopodes, i+1, j+1)

    # bottom
    if i < max_i and octopodes[i+1][j]:
        octopodes[i+1][j] += 1
        if octopodes[i+1][j] > 9:
            flashes += handle_flash(octopodes, i+1, j)

    # bottom left
    if i < max_i and j and octopodes[i+1][j-1]:
        octopodes[i+1][j-1] += 1
        if octopodes[i+1][j-1] > 9:
            flashes += handle_flash(octopodes, i+1, j-1)

    # left
    if j and octopodes[i][j-1]:
        octopodes[i][j-1] += 1
        if octopodes[i][j-1] > 9:
            flashes += handle_flash(octopodes, i, j-1)

    return flashes

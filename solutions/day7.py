from input.day7 import input_crab_positions


def solve_day7():
    ideal_position, fuel_cost = calculate_lowest_fuel_cost_linear(input_crab_positions)
    print('Solution for day 7 puzzle 1:')
    print('ideal position: %d fuel cost: %d' % (ideal_position, fuel_cost))

    print()

    ideal_position, fuel_cost = calculate_lowest_fuel_cost_increasing(input_crab_positions)
    print('Solution for day 7 puzzle 2:')
    print('ideal position: %d fuel cost: %d' % (ideal_position, fuel_cost))


def calculate_lowest_fuel_cost_linear(crab_positions):
    crab_counts = sort_crabs_by_position(crab_positions)
    ideal_position = find_ideal_position_linear(crab_counts)

    return ideal_position, calculate_fuel_cost_linear(crab_counts, ideal_position)


def sort_crabs_by_position(crab_positions):
    sorted_crab_positions = [0] * (max(crab_positions) + 1)
    for position in crab_positions:
        sorted_crab_positions[position] += 1

    return sorted_crab_positions


def find_ideal_position_linear(crab_counts):
    partial_crab_count = 0
    total_crab_count = sum(crab_counts)
    # use a value that is higher than any possible difference
    last_difference = total_crab_count * len(crab_counts)

    for i in range(0, len(crab_counts)):
        difference = abs(total_crab_count - partial_crab_count * 2 - crab_counts[i])
        # once the difference start increasing, we are just past the ideal position
        if difference > last_difference:
            return i - 1

        last_difference = difference
        partial_crab_count += crab_counts[i]


def calculate_fuel_cost_linear(crab_counts, position):
    fuel_cost = 0

    for i in range(0, len(crab_counts)):
        fuel_cost += crab_counts[i] * abs(position - i)

    return fuel_cost


def calculate_lowest_fuel_cost_increasing(crab_positions):
    crab_counts = sort_crabs_by_position(crab_positions)

    fuel_costs = [0] * len(crab_counts)

    for i in range(0, len(crab_counts)):
        for j in range(0, len(crab_counts)):
            fuel_costs[i] += crab_counts[j] * calculate_fuel_cost_increasing(i, j)

    return fuel_costs.index(min(fuel_costs)), min(fuel_costs)


def calculate_fuel_cost_increasing(i, j):
    distance = abs(i - j)

    return (1 + distance) * distance / 2

import operator

from input.day14 import input_polymer, input_pairs


def solve_day14():
    value = find_polymer_value_after_x_steps(input_polymer, input_pairs, 10)
    print('Solution for day 14 puzzle 1:')
    print(f'polymer value: {value}')

    print()

    value = find_polymer_value_after_x_steps(input_polymer, input_pairs, 40)
    print('Solution for day 14 puzzle 2:')
    print(f'polymer value: {value}')


def find_polymer_value_after_x_steps(polymer, pairs, steps):
    polymer_pairs = group_polymer(polymer)
    for i in range(0, steps):
        polymer_pairs = expand_polymer_pairs(polymer_pairs, pairs)

    polymer_counts = get_polymer_count(polymer_pairs, polymer[-1])

    return polymer_counts[-1][1] - polymer_counts[0][1]


def group_polymer(polymer):
    polymer_pairs = {}
    for i in range(1, len(polymer)):
        add_to_dict(polymer_pairs, polymer[i - 1:i + 1], 1)

    return polymer_pairs


def expand_polymer_pairs(polymer_pairs, pairs):
    new_pairs = {}
    for pair in polymer_pairs:
        if pair in pairs:
            add_to_dict(new_pairs, pair[0] + pairs[pair], polymer_pairs[pair])
            add_to_dict(new_pairs, pairs[pair] + pair[1], polymer_pairs[pair])
        else:
            add_to_dict(new_pairs, pair, polymer_pairs[pair])

    return new_pairs


def add_to_dict(dictionary, value, count):
    if value not in dictionary:
        dictionary[value] = 0
    dictionary[value] += count


def get_polymer_count(polymer_pairs, last_char):
    polymer = {last_char: 1}
    for pair in polymer_pairs:
        add_to_dict(polymer, pair[0], polymer_pairs[pair])

    return sorted(polymer.items(), key=operator.itemgetter(1))

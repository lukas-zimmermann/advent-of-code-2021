from input.day6 import input_fish


def solve_day6():
    fish_count = determine_fish_count_after_x_days(input_fish, 80)
    print('Solution for day 6 puzzle 1:')
    print('fish count: %d' % fish_count)

    print()

    fish_count = determine_fish_count_after_x_days(input_fish, 256)
    print('Solution for day 6 puzzle 2:')
    print('fish count: %d' % fish_count)


def determine_fish_count_after_x_days(fish, days):
    fish = sort_fish_by_value(fish)

    for day in range(0, days):
        # we remove the fish which have 0 days left from the list
        # as a result all others will move forward by 1 position/day
        new_fish = fish.pop(0)
        # all the fish that were at 0 now have 6 days left
        fish[6] += new_fish
        # there are new fish at the end of the list (with 8 days left)
        fish.append(new_fish)

    return sum(fish)


def sort_fish_by_value(fish):
    sorted_fish = [0] * 9
    for value in fish:
        sorted_fish[value] += 1

    return sorted_fish

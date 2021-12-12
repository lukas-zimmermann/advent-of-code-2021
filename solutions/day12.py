from input.day12 import input_caves


def solve_day12():
    paths = count_possible_paths_simple(input_caves.copy())
    print('Solution for day 12 puzzle 1:')
    print(f'paths: {paths}')

    print()

    paths = count_possible_paths_complex(input_caves.copy())
    print('Solution for day 12 puzzle 2:')
    print(f'paths: {paths}')


def count_possible_paths_simple(caves):
    for i in range(0, len(caves)):
        # all caves can be traversed in both directions
        caves.append(caves[i][::-1])

    # expand paths from the starting point
    paths = expand_path_simple(['start'], caves)

    return len(paths)


def count_possible_paths_complex(caves):
    for i in range(0, len(caves)):
        # all caves can be traversed in both directions
        caves.append(caves[i][::-1])

    # expand paths from the starting point
    paths = expand_path_complex(['start'], caves)

    return len(paths)


def expand_path_simple(path, caves):
    # if we reach the end, the path is done
    if path[-1] == 'end':
        return [path]

    paths = []
    for cave in caves:
        if cave[0] == path[-1]:
            # if the path is lowercase, we cannot visit it multiple times
            if cave[1].isupper() or cave[1] not in path:
                new_path = path.copy()
                new_path.append(cave[1])
                paths += expand_path_simple(new_path, caves)

    return paths


def expand_path_complex(path, caves):
    # if we reach the end, the path is done
    if path[-1] == 'end':
        return [path]

    paths = []
    for cave in caves:
        if cave[0] == path[-1]:
            # we never want to go back to the start
            if cave[1] == 'start':
                continue

            new_path = path.copy()
            new_path.append(cave[1])

            # a lowercase path can be used twice, but only once per path
            if cave[1].islower() and cave[1] in path:
                paths += expand_path_simple(new_path, caves)
            else:
                paths += expand_path_complex(new_path, caves)

    return paths

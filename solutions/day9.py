from input.day9 import input_heightmap


def solve_day9():
    risk_level = calculate_risk_level(input_heightmap)
    print('Solution for day 9 puzzle 1:')
    print(f'risk level: {risk_level}')

    print()

    basins = calculate_largest_basins(input_heightmap)
    print('Solution for day 9 puzzle 2:')
    print(f'largest_basins: {basins} product: {basins[0] * basins[1] * basins[2]}')


def calculate_risk_level(heightmap):
    risk_level = 0
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[0])):
            if is_low_point(i, j, heightmap):
                risk_level += int(heightmap[i][j]) + 1

    return risk_level


def is_low_point(i, j, hmap):
    tmp = int(hmap[i][j])

    # check left element
    if j and tmp >= int(hmap[i][j-1]):
        return False

    # check right element
    if j + 1 < len(hmap[i]) and tmp >= int(hmap[i][j+1]):
        return False

    # check up element
    if i and tmp >= int(hmap[i-1][j]):
        return False

    # check down element
    if i + 1 < len(hmap) and tmp >= int(hmap[i+1][j]):
        return False

    return True


def calculate_largest_basins(heightmap):
    basins = []
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[0])):
            if is_low_point(i, j, heightmap):
                basins.append(calculate_basin_size(i, j, heightmap))

    basins.sort(reverse=True)
    return basins[0:3]


def calculate_basin_size(i, j, heightmap):
    basin_map = get_empty_map(heightmap)
    basin_map[i][j] = 1
    expand_basin(heightmap, basin_map, int(heightmap[i][j]) + 1)

    return sum(map(sum, basin_map))


def get_empty_map(hmap):
    empty_map = []
    for i in hmap:
        empty_map.append([0] * len(hmap[0]))

    return empty_map


def expand_basin(hmap, bmap, value):
    if value < 9:
        for i in range(0, len(bmap)):
            for j in range(0, len(bmap[0])):
                if bmap[i][j] == 1:
                    expand_basin_around_point(i, j, hmap, bmap, value)

        return expand_basin(hmap, bmap, value + 1)


def expand_basin_around_point(i, j, hmap, bmap, value):
    if i and bmap[i-1][j] == 0 and int(hmap[i-1][j]) == value:
        add_to_basin(i - 1, j, hmap, bmap)
    if i + 1 < len(bmap) and bmap[i+1][j] == 0 and int(hmap[i+1][j]) == value:
        add_to_basin(i + 1, j, hmap, bmap)
    if j and bmap[i][j-1] == 0 and int(hmap[i][j-1]) == value:
        add_to_basin(i, j - 1, hmap, bmap)
    if j + 1 < len(bmap[0]) and bmap[i][j+1] == 0 and int(hmap[i][j+1]) == value:
        add_to_basin(i, j + 1, hmap, bmap)


def add_to_basin(i, j, hmap, bmap):
    tmp = int(hmap[i][j])
    # check all squares around for lower squares outside the existing basin
    if not ((j and tmp > int(hmap[i][j-1]) and bmap[i][j-1] == 0)                           # check left
            or (j + 1 < len(hmap[i]) and tmp > int(hmap[i][j+1]) and bmap[i][j+1] == 0)     # check right
            or (i and tmp > int(hmap[i-1][j]) and bmap[i-1][j] == 0)                        # check up
            or (i + 1 < len(hmap) and tmp > int(hmap[i+1][j]) and bmap[i+1][j] == 0)):      # check down
        bmap[i][j] = 1

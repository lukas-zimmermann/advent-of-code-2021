from input.day5 import input_lines


def solve_day5():
    intersection_points = count_points_with_intersecting_lines(input_lines)
    print('Solution for day 5 puzzle 1:')
    print('intersection points: %d' % intersection_points)

    print()


def count_points_with_intersecting_lines(lines):
    diagram = create_empty_diagram(1000, 1000)

    for line in lines:
        # x coordinates are the same
        if line[0] == line[2]:
            for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                diagram[line[0]][y] += 1
        # y coordinates are the same
        elif line[1] == line[3]:
            for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                diagram[x][line[1]] += 1
        # diagonal line
        else:
            x_dir = 1 if line[0] < line[2] else -1
            y_dir = 1 if line[1] < line[3] else -1
            for i in range(0, abs(line[0] - line[2]) + 1):
                diagram[line[0] + x_dir * i][line[1] + y_dir * i] += 1

    return count_intersection_points(diagram)


def create_empty_diagram(x, y):
    diagram = []
    for i in range(0, y):
        diagram.append([0] * x)

    return diagram


def count_intersection_points(diagram):
    count = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if diagram[x][y] >= 2:
                count += 1

    return count

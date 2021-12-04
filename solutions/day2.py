from input.day2 import input_commands


def solve_day2():
    h_pos, depth = calculate_horizontal_position_and_depth(input_commands)
    print('Solution for day 2 puzzle 1:')
    print('%d horizontal distance, %d depth' % (h_pos, depth))
    print('%d x %d = %d' % (h_pos, depth, h_pos * depth))

    print()

    h_pos, depth = calculate_horizontal_position_and_depth_with_aim(input_commands)
    print('Solution for day 2 puzzle 2:')
    print('%d horizontal distance, %d depth' % (h_pos, depth))
    print('%d x %d = %d' % (h_pos, depth, h_pos * depth))


def calculate_horizontal_position_and_depth(commands):
    h_pos = 0
    depth = 0

    for command in commands:
        command = command.split()

        if command[0] == 'forward':
            h_pos += int(command[1])
        elif command[0] == 'up':
            depth -= int(command[1])
        elif command[0] == 'down':
            depth += int(command[1])

    return h_pos, depth


def calculate_horizontal_position_and_depth_with_aim(commands):
    h_pos = 0
    depth = 0
    aim = 0

    for command in commands:
        command = command.split()

        if command[0] == 'forward':
            h_pos += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])

    return h_pos, depth

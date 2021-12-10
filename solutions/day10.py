from input.day10 import input_navigation_subsystem


def solve_day10():
    error_score = calculate_syntax_error_score(input_navigation_subsystem)
    print('Solution for day 10 puzzle 1:')
    print(f'syntax error score: {error_score}')

    print()

    completion_score = calculate_syntax_line_completion_score(input_navigation_subsystem)
    print('Solution for day 10 puzzle 2:')
    print(f'line completion score: {completion_score}')


def calculate_syntax_error_score(lines):
    error_values = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    error_score = 0

    for line in lines:
        error = find_line_error(line)
        # if it's a string, it's an actual error
        if isinstance(error, str):
            error_score += error_values[error]

    return error_score


def calculate_syntax_line_completion_score(lines):
    scores = []

    for line in lines:
        stack = find_line_error(line)
        # if it's a list, it's the missing closing brackets of a valid line
        if isinstance(stack, list):
            scores.append(calculate_completion_score(stack))

    scores.sort()
    return scores[int(len(scores) / 2)]


def find_line_error(line):
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    stack = []

    for char in line:
        if char in brackets:
            stack.append(brackets[char])
        elif char != stack.pop():
            return char

    return stack


def calculate_completion_score(stack):
    bracket_values = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    score = 0
    for i in range(0, len(stack)):
        score = score * 5 + bracket_values[stack.pop()]

    return score

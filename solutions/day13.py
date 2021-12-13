from input.day13 import input_dots, input_folds


def solve_day13():
    dots = count_dots_after_first_fold(input_dots.copy(), input_folds)
    print('Solution for day 13 puzzle 1:')
    print(f'dots: {dots}')

    print()

    code = get_activation_code(input_dots.copy(), input_folds)
    print('Solution for day 13 puzzle 2:')
    print('activation code:')
    print(code)


def count_dots_after_first_fold(dots, folds):
    return len(fold_paper(dots, folds[0]))


def get_activation_code(dots, folds):
    max_x = 0
    max_y = 0
    for fold in folds:
        dots = fold_paper(dots, fold)
        if fold[0] == 'x':
            max_x = fold[1]
        else:
            max_y = fold[1]

    code = ''
    for line in map_dots(dots, max_x, max_y):
        code += ' '.join(line) + '\n'

    return code


def fold_paper(dots, fold):
    # decide if we fold in x or y direction
    pos = 0 if fold[0] == 'x' else 1

    new_dots = set()
    for dot in dots:
        dot = list(dot)
        if dot[pos] > fold[1]:
            dot[pos] = fold[1] * 2 - dot[pos]

        new_dots.add(tuple(dot))

    return new_dots


def map_dots(dots, max_x, max_y):
    mapped_dots = []
    for i in range(0, max_y):
        mapped_dots.append([' '] * max_x)

    for dot in dots:
        mapped_dots[dot[1]][dot[0]] = '\u2588'

    return mapped_dots

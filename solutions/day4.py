from input.day4 import input_boards, input_numbers


def solve_day4():
    score = find_winning_board_score(input_numbers, input_boards)
    print('Solution for day 4 puzzle 1:')
    print('score: %d' % score)

    print()

    score = find_last_board_score(input_numbers, input_boards)
    print('Solution for day 4 puzzle 2:')
    print('score: %d' % score)


def find_winning_board_score(numbers, boards):
    # we create a list with a board of 0s for each given board
    marking_boards = get_marking_boards(boards)

    for number in numbers:
        mark_number(number, boards, marking_boards)

        winning_board_index = find_winning_board(marking_boards)
        if winning_board_index != -1:
            return get_board_score(boards[winning_board_index], marking_boards[winning_board_index]) * number


def find_last_board_score(numbers, boards):
    # we create a list with a board of 0s for each given board
    marking_boards = get_marking_boards(boards)

    for number in numbers:
        mark_number(number, boards, marking_boards)

        winning_board_index = find_winning_board(marking_boards)
        if winning_board_index != -1:
            if len(boards) <= 1:
                return get_board_score(boards[0], marking_boards[0]) * number

            remove_winning_boards(boards, marking_boards)


def get_marking_boards(boards):
    marking_boards = []
    for board in boards:
        marking_boards.append([0] * 25)

    return marking_boards


def mark_number(number, boards, marking_boards):
    for i in range(0, len(boards)):
        board = boards[i]
        if number in board:
            index = board.index(number)
            marking_boards[i][index] = 1


def find_winning_board(boards):
    for board in boards:
        if is_winning_board(board):
            return boards.index(board)

    return -1


def is_winning_board(board):
    for i in range(0, 5):
        line = i * 5
        if board[line] + board[line+1] + board[line+2] + board[line+3] + board[line+4] == 5:
            return True

        if board[i] + board[i+5] + board[i+10] + board[i+15] + board[i+20] == 5:
            return True

    return False


def get_board_score(board, marking_board):
    score = 0
    for i in range(0, 25):
        if marking_board[i] == 0:
            score += board[i]

    return score


def remove_winning_boards(boards, marking_boards):
    # we need to use a copy of the list because we will remove elements in the loop
    for marking_board in list(marking_boards):
        if is_winning_board(marking_board):
            index = marking_boards.index(marking_board)
            del boards[index]
            del marking_boards[index]

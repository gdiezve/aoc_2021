import numpy as np


def build_board_from_input(input_file):
    a = []
    for i in range(5):
        row = list(filter(None, input_file[i].split(' ')))
        row = [int(item) for item in row]
        a.append(row)
    board = np.array(a)
    return board


def get_winner_board_score(draw_list, boards):
    marked_boards = boards
    for number in draw_list:
        for board in marked_boards:
            np.place(board, board == number, -1)
            if True in np.all(board == -1, axis=0):
                return get_score(board, number)
            if True in np.all(board == -1, axis=1):
                return get_score(board, number)


def get_score(board, number):
    sum = 0
    for row in board:
        for num in row:
            if num != -1:
                sum += num
    return sum * number


if __name__ == "__main__":
    with open("input.txt") as input_file:
        input_file_lines = input_file.read().splitlines()
        draw_list = [int(number) for number in input_file_lines[0].split(',')]
        file = list(filter(None, input_file_lines[2:]))
        boards = []
        while file:
            boards.append(build_board_from_input(file))
            file = file[5:]
        winner_board = get_winner_board_score(draw_list, boards)
        print('Score for winner board is: ', winner_board)

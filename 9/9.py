import numpy as np


def get_adjacent(matrix, i, j):
    try:
        return matrix[i][j]
    except IndexError:
        return -1


def get_risk_level_sum(input_file):
    matrix = [[int(x) for x in line] for line in input_file]
    sum_low_heights = 0
    i = 0
    while i <= len(matrix) - 1:
        j = 0
        while j <= len(matrix[i]) - 1:
            current_number = matrix[i][j]
            up = get_adjacent(matrix, i - 1, j) if i - 1 >= 0 else -1
            down = get_adjacent(matrix, i + 1, j)
            left = get_adjacent(matrix, i, j - 1) if j - 1 >= 0 else -1
            right = get_adjacent(matrix, i, j + 1)
            j += 1
            adjacent_numbers = np.array([up, down, left, right])
            if np.any(adjacent_numbers == -1):
                adjacent_numbers = adjacent_numbers[adjacent_numbers != -1]
            if np.all(current_number < adjacent_numbers):
                sum_low_heights += current_number + 1
        i += 1
    return sum_low_heights


if __name__ == "__main__":
    with open("input.txt") as input_file:
        input_file_lines = input_file.read().splitlines()
        print('The sum of risk levels for low height points is: ' + str(get_risk_level_sum(input_file_lines)))

def get_number_fishes(input, days):
    input = [int(x) for x in input]
    dict_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in input:
        dict_fish[fish] += 1

    while days > 0:
        number = 0
        new_born = 0
        if dict_fish[0] > 0:
            new_born = dict_fish[0]
        while number < 8:
            dict_fish[number] = dict_fish[number + 1]
            number += 1
        dict_fish[6] = dict_fish[6] + new_born
        dict_fish[8] = 0
        dict_fish[8] = dict_fish[8] + new_born
        days -= 1

    sum_fishes = 0
    for fishes in dict_fish:
        sum_fishes += dict_fish[fishes]

    return sum_fishes


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().split(',')
        print('Number of fishes for first part: ', get_number_fishes(input_file_lines, 80))
        print('Number of fishes for first part: ', get_number_fishes(input_file_lines, 256))

def get_gamma_epsilon_rates(input_file):
    sum = []
    for line in input_file:
        if not sum:
            sum = [bit for bit in line]
        else:
            i = 0
            while i < len(line):
                sum[i] = str(int(sum[i]) + int(line[i]))
                i += 1
    most_common = ''
    less_common = ''
    for pos in sum:
        if int(pos) > len(input_file)/2:
            most_common += '1'
            less_common += '0'
        else:
            most_common += '0'
            less_common += '1'
    return int(most_common, 2) * int(less_common, 2)


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        print(get_gamma_epsilon_rates(input_file_lines))

def get_gamma_epsilon_rates(input_file):
    sum = []
    for line in input_file:
        if not sum:
            sum = [bit for bit in line]
        else:
            for i in range(len(line)):
                sum[i] = str(int(sum[i]) + int(line[i]))
    most_common = ''
    less_common = ''
    for pos in sum:
        if int(pos) > len(input_file) / 2:
            most_common += '1'
            less_common += '0'
        else:
            most_common += '0'
            less_common += '1'
    return int(most_common, 2) * int(less_common, 2)


def get_oxygen_co2_rates(input_file):
    oxygen_list = [line for line in input_file]
    sum = get_most_common_bit(input_file)
    pos = 0
    while len(oxygen_list) > 1 and pos < len(oxygen_list[0]):
        if len(oxygen_list) == 1:
            break
        if int(pos) >= len(oxygen_list) / 2:  # most common 1
            oxygen_list = [line for line in oxygen_list if line[sum.index(pos)] == '1']
        else:  # most common 0
            oxygen_list = [line for line in oxygen_list if line[sum.index(pos)] == '0']
        sum = get_most_common_bit(oxygen_list)
        print(sum)
        print("8====D")
        pos += 1

    print(f'oxygen {oxygen_list}')


def get_most_common_bit(input_file):
    sum = []
    for line in input_file:
        if not sum:
            sum = [bit for bit in line]
        else:
            i = 0
            while i < len(line):
                sum[i] = str(int(sum[i]) + int(line[i]))
                i += 1
    return sum


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        get_gamma_epsilon_rates(input_file_lines)

    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        get_oxygen_co2_rates(input_file_lines)

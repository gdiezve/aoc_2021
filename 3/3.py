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


def get_oxygen_generator_rating(input_file):
    bit_criteria = get_bit_criteria(input_file)
    input = input_file
    i = 0
    while i < len(input[0]) and len(input) > 1:
        if float(bit_criteria[i]) >= len(input)/2:
            input = [line for line in input if line[i] == '1']
        else:
            input = [line for line in input if line[i] == '0']
        bit_criteria = get_bit_criteria(input)
        i += 1
    return input


def get_co2_scrubber_rating(input_file):
    bit_criteria = get_bit_criteria(input_file)
    input = input_file
    i = 0
    while i < len(input[0]) and len(input) > 1:
        if float(bit_criteria[i]) >= len(input)/2:
            input = [line for line in input if line[i] == '0']
        else:
            input = [line for line in input if line[i] == '1']
        bit_criteria = get_bit_criteria(input)
        i += 1
    return input


def get_bit_criteria(input):
    bit_criteria = []
    for line in input:
        if not bit_criteria:
            bit_criteria = [bit for bit in line]
        else:
            for i in range(len(line)):
                bit_criteria[i] = str(int(bit_criteria[i]) + int(line[i]))
    return bit_criteria


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        result = get_gamma_epsilon_rates(input_file_lines)
        print(f'First part answer: {result}')

    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        oxygen = get_oxygen_generator_rating(input_file_lines)
        co2 = get_co2_scrubber_rating(input_file_lines)
        result = int(oxygen[0], 2) * int(co2[0], 2)
        print(f'Second part answer: {result}')

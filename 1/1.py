def get_number_of_increasements(input_file):
    count = 0
    previous = None
    for measurement in input_file:
        if previous is not None and previous < int(measurement):
            count += 1
        previous = int(measurement)
    return count


def get_number_three_measurement_of_increasements(input_file):
    count = 0
    previous = None
    i = 0
    while i+2 < len(input_file):
        three_measurement = int(input_file[i]) + int(input_file[i+1]) + int(input_file[i+2])
        if previous is not None and previous < three_measurement:
            count += 1
        previous = three_measurement
        i += 1
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        increasements = get_number_of_increasements(input_file)
        print(f'First part answer: {increasements}')
    with open("input.txt", "r") as input_file:
        input_file_list = input_file.read().splitlines()
        three_measurement_increasements = get_number_three_measurement_of_increasements(input_file_list)
        print(f'Second part answer: {three_measurement_increasements}')


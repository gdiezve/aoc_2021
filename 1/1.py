def get_number_of_increasements(input_file):
    count = 0
    previous = None
    for measurement in input_file:
        if previous is not None and previous < int(measurement):
            count += 1
        previous = int(measurement)
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        increasements = get_number_of_increasements(input_file)
        print(increasements)

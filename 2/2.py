def get_position(input_file):
    position = 0
    depth = 0
    for step in input_file:
        movement, amount = step.split(' ')
        if movement == "forward":
            position += int(amount)
        elif movement == "down":
            depth += int(amount)
        elif movement == "up":
            depth -= int(amount)

    return position * depth


def get_position_by_aim(input_file):
    position = 0
    depth = 0
    aim = 0
    for step in input_file:
        movement, amount = step.split(' ')
        if movement == "forward":
            position += int(amount)
            if aim > 0:
                depth += int(amount) * aim
        elif movement == "down":
            aim += int(amount)
        elif movement == "up":
            aim -= int(amount)

    return position * depth


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        result = get_position(input_file_lines)
        print(f'First part answer: {result}')

    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        result = get_position_by_aim(input_file_lines)
        print(f'Second part answer: {result}')

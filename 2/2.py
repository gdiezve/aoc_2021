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


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        result = get_position(input_file_lines)
        print(result)

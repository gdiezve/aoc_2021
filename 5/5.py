def process_file(input_file):
    formatted_input = []
    for line in input_file:
        line = line.split(" -> ")
        formatted_input.append(line)
    return formatted_input


def get_hydrothermal_vents_overlapped_points(input_file):
    points = []
    overlaped_points = []
    i = 0
    for line in input_file:
        x1, y1 = line[0].split(',')
        x2, y2 = line[1].split(',')
        print(i)
        if int(x1) == int(x2):
            if int(y1) > int(y2):
                for num in range(int(y1), int(y2)-1, -1):
                    if (int(x1), num) not in points:
                        points.append((int(x1), num))
                    else:
                        if (int(x1), num) not in overlaped_points:
                            overlaped_points.append((int(x1), num))
            else:
                for num in range(int(y1), int(y2)+1):
                    if (int(x1), num) not in points:
                        points.append((int(x1), num))
                    else:
                        if (int(x1), num) not in overlaped_points:
                            overlaped_points.append((int(x1), num))

        elif int(y1) == int(y2):
            if int(x1) > int(x2):
                for num in range(int(x1), int(x2)-1, -1):
                    if (num, int(y1)) not in points:
                        points.append((num, int(y1)))
                    else:
                        if (num, int(y1)) not in overlaped_points:
                            overlaped_points.append((num, int(y1)))
            else:
                for num in range(int(x1), int(x2)+1):
                    if (num, int(y1)) not in points:
                        points.append((num, int(y1)))
                    else:
                        if (num, int(y1)) not in overlaped_points:
                            overlaped_points.append((num, int(y1)))

        else:
            if int(x1) > int(x2) and int(y1) > int(y2):
                count = 0
                for num in range(int(x1), int(x2) - 1, -1):
                    if (num, int(y1) - count) not in points:
                        points.append((num, int(y1) - count))
                    else:
                        if (num, int(y1) - count) not in overlaped_points:
                            overlaped_points.append((num, int(y1) - count))
                    count += 1
            if int(x1) > int(x2) and int(y1) < int(y2):
                count = 0
                for num in range(int(x1), int(x2)-1, -1):
                    if (num, int(y1)+count) not in points:
                        points.append((num, int(y1)+count))
                    else:
                        if (num, int(y1)+count) not in overlaped_points:
                            overlaped_points.append((num, int(y1)+count))
                    count += 1
            if int(x1) < int(x2) and int(y1) > int(y2):
                count = 0
                for num in range(int(x1), int(x2)+1):
                    if (num, int(y1) - count) not in points:
                        points.append((num, int(y1) - count))
                    else:
                        if (num, int(y1) - count) not in overlaped_points:
                            overlaped_points.append((num, int(y1) - count))
                    count += 1
            if int(x1) < int(x2) and int(y1) < int(y2):
                count = 0
                for num in range(int(x1), int(x2)+1):
                    if (num, int(y1) + count) not in points:
                        points.append((num, int(y1) + count))
                    else:
                        if (num, int(y1) + count) not in overlaped_points:
                            overlaped_points.append((num, int(y1) + count))
                    count += 1
        i += 1

    return len(overlaped_points)


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        input_file_lines = input_file.read().splitlines()
        formatted_input = process_file(input_file_lines)
        print(get_hydrothermal_vents_overlapped_points(formatted_input))

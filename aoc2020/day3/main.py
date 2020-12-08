# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_file(file_name):
    with open(file_name, "r") as f:
        input = [x.strip() for x in f.readlines()]
    return input


def aoc2020_3_a(input: list):
    tree_count = 0
    x_coord = 3
    y_coord = 1
    for i in range(len(input) - 1):
        line = input[y_coord]
        if line[x_coord % len(line)] == "#":
            tree_count += 1
        x_coord += 3
        y_coord += 1
    return tree_count


def aoc2020_3_b(input: list, slopes: list):
    product = 1
    for slope in slopes:
        tree_count = 0
        x, y = slope.split(" ")
        x = int(x)
        y = int(y)
        (x_coord, y_coord) = (x, y)
        for i in range(len(input) - 1):
            line = input[y_coord]
            if line[x_coord % len(line)] == "#":
                tree_count += 1
            x_coord += x
            y_coord += y
            if y_coord >= len(input):
                break
        product *= tree_count
    return product


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(aoc2020_3_a(read_file("day3.txt")))
    print(aoc2020_3_b(read_file("day3.txt"), read_file("day3_slopes.txt")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

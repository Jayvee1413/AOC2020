# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re


def read_file_as_whole_string(file_name):
    with open(file_name, "r") as f:
        input = f.read()
    return input


def read_file(file_name):
    with open(file_name, "r") as f:
        input = [x.strip() for x in f.readlines()]
    return input


def convert_input_to_batches(input: str):
    sp = re.split('\n\s*\n', input)
    return sp


def check_shiny(bag_colors, color, is_valid):
    if "other" in bag_colors[color]:
        return is_valid
    else:
        y = bag_colors[color]
        keys = bag_colors[color].keys()

        if "shiny gold" in bag_colors[color].keys():
            return 1
        else:
            x = 0
            for bag_color in bag_colors[color]:
                x += check_shiny(bag_colors, bag_color, x)
            return bool(x)


def check_gold_count(bag_colors):
    count = 0
    for bag_color in bag_colors["shiny gold"]:
        x = check_bag_count(bag_colors, bag_color, int(bag_colors["shiny gold"][bag_color]))
        count += x
    return count


def check_bag_count(bag_colors, color, count):
    if "other" in bag_colors[color]:
        return int(count)
    else:
        sum_color = int(count)
        for c in bag_colors[color]:
            x = check_bag_count(bag_colors, c, bag_colors[color][c])
            sum_color += int(count) * x
        return sum_color


def aoc2020_7_a(input: list):
    bag_colors = dict()
    for data in input:
        bag_color = data.split(" contain ")[0].split(" bag")[0].split("bags")[0]
        bag_colors[bag_color] = {}
    for data in input:
        bag_color = data.split(" contain ")[0].split(" bag")[0].split("bags")[0]
        for inside_bags in data.split(" contain ")[1].split(", "):
            number = inside_bags.split(" ")[0]
            inside_bag_color = inside_bags.split(" ", 1)[1].split(" bags")[0].split(" bag")[0]

            bag_colors[bag_color][inside_bag_color] = number

    valid_bag_colors = []
    for bag_color in bag_colors.keys():
        valid_bag_colors.append(check_shiny(bag_colors, bag_color, 0))

    return sum(valid_bag_colors)


def aoc2020_7_b(input: list):
    bag_colors = dict()
    for data in input:
        bag_color = data.split(" contain ")[0].split(" bag")[0].split("bags")[0]
        bag_colors[bag_color] = {}
    for data in input:
        bag_color = data.split(" contain ")[0].split(" bag")[0].split("bags")[0]
        for inside_bags in data.split(" contain ")[1].split(", "):
            number = inside_bags.split(" ")[0]
            inside_bag_color = inside_bags.split(" ", 1)[1].split(" bags")[0].split(" bag")[0]

            bag_colors[bag_color][inside_bag_color] = number

    return check_gold_count(bag_colors)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(aoc2020_7_a(read_file("day7.txt")))
    print(aoc2020_7_b(read_file("day7.txt")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

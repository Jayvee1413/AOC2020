# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
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


def aoc2020_5_a(input: list):
    row_total = 128
    column_total = 8

    max_seat = 0
    for data in input:
        f_b = data[0:7]
        l_r = data[7:]
        current_row_max = 127
        current_row_min = 0
        current_col_max = 7
        current_col_min = 0
        cur_row = 0
        cur_col = 0
        for fb in f_b:
            if fb == "F":
                current_row_max = math.floor((current_row_min + current_row_max) / 2)
            else:
                current_row_min = math.ceil((current_row_min + current_row_max) / 2)
        if f_b[-1] == "F":
            cur_row = current_row_min
        else:
            cur_row = current_row_max
        for lr in l_r:
            if lr == "L":
                current_col_max = math.floor((current_col_min + current_col_max) / 2)
            else:
                current_col_min = math.ceil((current_col_min + current_col_max) / 2)
        if f_b[-1] == "L":
            cur_col = current_col_min
        else:
            cur_col = current_col_max

        print((cur_row * 8) + cur_col)
        max_seat = max(max_seat, (cur_row * 8) + cur_col)
    return max_seat


def aoc2020_5_b(input: list):
    seat_ids = set()
    for data in input:
        f_b = data[0:7]
        l_r = data[7:]
        current_row_max = 127
        current_row_min = 0
        current_col_max = 7
        current_col_min = 0
        for fb in f_b:
            if fb == "F":
                current_row_max = math.floor((current_row_min + current_row_max) / 2)
            else:
                current_row_min = math.ceil((current_row_min + current_row_max) / 2)
        if f_b[-1] == "F":
            cur_row = current_row_min
        else:
            cur_row = current_row_max
        for lr in l_r:
            if lr == "L":
                current_col_max = math.floor((current_col_min + current_col_max) / 2)
            else:
                current_col_min = math.ceil((current_col_min + current_col_max) / 2)
        if f_b[-1] == "L":
            cur_col = current_col_min
        else:
            cur_col = current_col_max

        seat_ids.add((cur_row * 8) + cur_col)
    seat_ids = sorted(seat_ids)
    for i in range(seat_ids[0], seat_ids[-1]):
        if i not in seat_ids and i + 1 in seat_ids and i - 1 in seat_ids:
            return i
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(aoc2020_5_a(read_file("day8.txt")))
    print(aoc2020_5_b(read_file("day5.txt")))
    # print(aoc2020_4_b(convert_input_to_batches(read_file_as_whole_string("day8.txt"))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

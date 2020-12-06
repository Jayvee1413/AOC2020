# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import re

from aoc2020.day4.validators import validate_byr, validate_pid, validate_ecl, validate_hcl, validate_hgt, validate_eyr, \
    validate_iyr


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


def aoc2020_6_a(input: list):
    count = 0
    for data in input:
        if data != "":
            answer_set = set()

            for answer in data:
                if answer != "\n":
                    answer_set.add(answer)
            print(answer_set)
            count += len(answer_set)
    return count


def aoc2020_6_b(input: list):
    count = 0
    for data in input:
        if data != "":
            persons_answers = data.split("\n")
            group_set = set()
            started = 0
            for answers in persons_answers:
                if not started:
                    for answer in answers:
                        group_set.add(answer)
                    started = 1
                else:
                    group_set = group_set.intersection(set(list(answers)))

            count += len(group_set)
    return count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(aoc2020_6_b(convert_input_to_batches(read_file_as_whole_string("day6.txt"))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

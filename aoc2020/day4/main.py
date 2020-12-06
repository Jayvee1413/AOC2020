# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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

def aoc2020_4_a(input: list):
    count = 0
    for data in input:
        try:
            re.compile(r"(?<=byr:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            re.compile(r"(?<=iyr:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            re.compile(r"(?<=eyr:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            re.compile(r"(?<=hgt:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            re.compile(r"(?<=hcl:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            re.compile(r"(?<=ecl:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            re.compile(r"(?<=pid:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            count += 1
        except Exception as e:
            pass
    return count

def aoc2020_4_b(input: list):
    count = 0
    valid_data = []
    for data in input:
        try:
            byr = int(re.compile(r"(?<=byr:)([#]*)(\w+)(?=\s|$)").search(data)[0])
            validate_byr(byr)
            iyr = int(re.compile(r"(?<=iyr:)([#]*)(\w+)(?=\s|$)").search(data)[0])
            validate_iyr(iyr)
            eyr = int(re.compile(r"(?<=eyr:)([#]*)(\w+)(?=\s|$)").search(data)[0])
            validate_eyr(eyr)
            hgt = re.compile(r"(?<=hgt:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            validate_hgt(hgt)
            hcl = re.compile(r"(?<=hcl:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            validate_hcl(hcl)
            ecl = re.compile(r"(?<=ecl:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            validate_ecl(ecl)
            pid = re.compile(r"(?<=pid:)([#]*)(\w+)(?=\s|$)").search(data)[0]
            validate_pid(pid)
            count += 1
            valid_data.append(data)
        except Exception as e:
            pass
    return count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(aoc2020_4_a(convert_input_to_batches(read_file_as_whole_string("day4.txt"))))
    print(aoc2020_4_b(convert_input_to_batches(read_file_as_whole_string("day4.txt"))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

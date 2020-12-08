# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re


def read_file(file_name):
    with open(file_name, "r") as f:
        input = [x.strip() for x in f.readlines()]
    return input


def get_numbers(line):
    first_number_pattern = re.compile(r"^\d*[^-]")
    first_number = first_number_pattern.search(line)[0]
    second_number_pattern = re.compile(r"(?<=-)\d+(?= )")
    second_number = second_number_pattern.search(line)[0]
    return int(first_number), int(second_number)


def get_letter(line):
    letter_pattern = re.compile(r"(?<= )\w+(?=:)")
    letter = letter_pattern.search(line)[0]
    return letter


def get_password(line):
    password_pattern = re.compile(r"(?<=[: ])\w+$")
    password = password_pattern.search(line)[0]
    return password


def aoc2020_2_a(input: list):
    valid_count = 0
    for data in input:
        password = get_password(data)
        policy_letter = get_letter(data)
        policy_count_min, policy_count_max = get_numbers(data)
        policy_letter_count = password.count(policy_letter)
        if policy_count_min <= policy_letter_count <= policy_count_max:
            valid_count += 1
    return valid_count


def aoc2020_2_b(input: list):
    valid_count = 0
    for data in input:
        password = get_password(data)
        policy_letter = get_letter(data)
        policy_index_valid_1, policy_index_valid_2 = get_numbers(data)
        if policy_letter == password[policy_index_valid_1 - 1] or policy_letter == password[policy_index_valid_2 - 1]:
            if password[policy_index_valid_1 - 1] != password[policy_index_valid_2 - 1]:
                valid_count += 1
    return valid_count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(aoc2020_2_a(read_file("day2.txt")))
    print(aoc2020_2_b(read_file("day2.txt")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

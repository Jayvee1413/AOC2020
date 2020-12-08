# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_file(file_name):
    with open(file_name, "r") as f:
        input = [x.strip() for x in f.readlines()]
    return input


def aoc2020_1_a(input: list):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(0, len(input) - 1):
        for j in range(i, len(input)):
            if int(input[i]) + int(input[j]) == 2020:
                return int(input[i]) * int(input[j])


def aoc2020_1_b(input: list):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(0, len(input) - 2):
        for j in range(i, len(input) - 1):
            for k in range(j, len(input)):
                if int(input[i]) + int(input[j]) + int(input[k]) == 2020:
                    return int(input[i]) * int(input[j]) * int(input[k])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(aoc2020_1_a(read_file("day1.txt")))
    print(aoc2020_1_b(read_file("day1.txt")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

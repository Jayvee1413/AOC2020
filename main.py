# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_file(file_name):
    with open(file_name, "r") as f:
        input = [x.strip() for x in f.readlines()]
    return input

def aoc2020_1_a(input: list):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(0, len(input)-1):
        for j in range(i, len(input)):
            if int(input[i])+int(input[j]) == 2020:
                return int(input[i]) * int(input[j])

def aoc2020_1_b(input: list):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(0, len(input)-2):
        for j in range(i, len(input)-1):
            for k in range(j, len(input)):
                if int(input[i])+int(input[j])+int(input[k]) == 2020:
                    return int(input[i]) * int(input[j]) * int(input[k])

def aoc2020_2_a(input: list):
    valid_count = 0
    for data in input:
        line = data.split(": ")
        policy = line[0]
        password = line[1]
        policy_formatted = policy.split(" ")
        policy_letter = policy_formatted[1]
        policy_counts = policy_formatted[0].split("-")
        policy_count_min = int(policy_counts[0])
        policy_count_max = int(policy_counts[1])
        policy_letter_count = password.count(policy_letter)
        if policy_letter_count >= policy_count_min and policy_letter_count <= policy_count_max:
            valid_count += 1
    return valid_count

def aoc2020_2_b(input: list):
    valid_count = 0
    for data in input:
        line = data.split(": ")
        policy = line[0]
        password = line[1]
        policy_formatted = policy.split(" ")
        policy_letter = policy_formatted[1]
        policy_counts = policy_formatted[0].split("-")
        policy_index_valid_1 = int(policy_counts[0])
        policy_index_valid_2 = int(policy_counts[1])
        if policy_letter == password[policy_index_valid_1-1] or policy_letter == password[policy_index_valid_2-1]:
            if password[policy_index_valid_1-1] != password[policy_index_valid_2-1]:
                valid_count += 1
    return valid_count


def aoc2020_3_a(input: list):

    tree_count = 0
    x_coord = 3
    y_coord = 1
    for i in range(len(input)-1):
        line = input[y_coord]
        if line[x_coord%len(line)] == "#":
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
            if line[x_coord%len(line)] == "#":
                tree_count += 1
            x_coord += x
            y_coord += y
            if y_coord >= len(input):
                break
        product *= tree_count
    return product


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # print(aoc2020_1_a(read_file("day1.txt")))
    #print(aoc2020_1_b(read_file("day1.txt")))
    # print(aoc2020_2_a(read_file("day2.txt")))
    # print(aoc2020_2_b(read_file("day2.txt")))
    # print(aoc2020_3_a(read_file("day3.txt")))
    print(aoc2020_3_b(read_file("day3.txt"), read_file("day3_slopes.txt")))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import math
import re
from copy import deepcopy


def read_file(file_name):
    with open(file_name, "r") as f:
        input = [x.strip() for x in f.readlines()]
    return input

def read_file_as_str(file_name):
    with open(file_name, "r") as f:
        input = f.read()
    return input

def aoc2019_1_a(input: list):

    required_fuel = 0
    for mass in input:
        required_fuel += math.floor(int(mass)/3) -2
    return required_fuel

def aoc2019_1_b(input: list):

    total_required_fuel = 0
    for mass in input:
        mass_here = mass
        while True:
            required_fuel = math.floor(int(mass_here)/3) -2
            if required_fuel <= 0:
                break
            total_required_fuel += required_fuel
            mass_here = required_fuel
    return total_required_fuel

def aoc_2019_2_a_opcode_1(input: list, curr_index):
    index_num1 = input[curr_index+1]
    index_num2 = input[curr_index+2]
    position_index = input[curr_index+3]
    input[position_index] = input[index_num1] + input[index_num2]

def aoc_2019_2_a_opcode_2(input: list, curr_index):
    index_num1 = input[curr_index + 1]
    index_num2 = input[curr_index + 2]
    position_index = input[curr_index+3]
    input[position_index] = input[index_num1] * input[index_num2]

def aoc2019_2_a(input: str, noun=12, verb=2):
    input = [int(x) for x in input.split(",")]

    input[1] = noun
    input[2] = verb
    # print(input)
    curr_index = 0
    while input[curr_index] != 99:
        if input[curr_index] == 1:
            aoc_2019_2_a_opcode_1(input, curr_index)
        elif input[curr_index] == 2:
            aoc_2019_2_a_opcode_2(input, curr_index)
        # print("****")
        # print(input)
        # print("***")
        curr_index += 4
    return input

def aoc2019_2_b(input: str):

    for i in range(100):
        for j in range(100):
            ans = aoc2019_2_a(deepcopy(input), noun=i, verb=j)[0]
            if ans == 19690720:
                print(i, j)
                break

def aoc2019_3_a(input: list):

    coords = []
    for data in input:
        commands = data.split(',')
        current_coords = (0,0)

        lines = set()
        for command in commands:
            direction = re.match(r"([UDLR])(\d+)", command).group(1)
            steps = int(re.match(r"([UDLR])(\d+)", command).group(2))
            if direction == "D" or direction == "L":
                steps = -steps
            index = 0 if direction in ["L", "R"] else 1
            fixed_index = 1 if direction in ["L", "R"] else 0
            for i in range(min(current_coords[index], current_coords[index]+steps), max(current_coords[index], current_coords[index]+steps)):
                new_coord = [0,0]
                new_coord[index] = i
                new_coord[fixed_index] = current_coords[fixed_index]
                lines.add(tuple(new_coord))
                print
        coords.append(set(sorted(lines)))
    for coord in coords:
        print (coord)
    intersects = coords[0].intersection(coords[1])
    print(intersects)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # print(aoc2019_1_a(read_file("2019_day1.txt")))
    # print(aoc2019_1_b(read_file("2019_day1.txt")))
    # print(aoc2019_2_a(read_file_as_str("2019_day2.txt")))
    # print(aoc2019_2_b(read_file_as_str("2019_day2.txt")))
    print(aoc2019_3_a(read_file("2019_day3_a.txt")))

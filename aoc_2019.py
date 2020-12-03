import math


def read_file(file_name):
    with open(file_name, "r") as f:
        input = [x.strip() for x in f.readlines()]
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

def aoc2020_2_a(input: list):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # print(aoc2019_1_a(read_file("2019_day1.txt")))
    print(aoc2019_1_b(read_file("2019_day1.txt")))

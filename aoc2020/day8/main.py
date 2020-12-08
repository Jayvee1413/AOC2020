# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
from copy import deepcopy


def read_file_as_whole_string(file_name):
    with open(file_name, "r") as f:
        contents = f.read()
    return contents


def read_file(file_name):
    with open(file_name, "r") as f:
        contents = [x.strip() for x in f.readlines()]
    return contents


def convert_input_to_batches(contents: str):
    sp = re.split('\n/s*\n', contents)
    return sp


def op_fun(lines, counter, accelerator, lines_done=None):
    if lines_done is None:
        lines_done = set()
    if counter >= len(lines):
        return accelerator
    if counter in lines_done:
        raise ValueError(accelerator)
    lines_done.add(counter)
    data = lines[counter].split(" ")
    op = data[0]
    value = int(data[1])
    if op == "nop":
        accelerator = op_fun(lines, counter + 1, accelerator, lines_done)
    elif op == "jmp":
        accelerator = op_fun(lines, counter + value, accelerator, lines_done)
    elif op == "acc":
        accelerator = op_fun(lines, counter + 1, accelerator + value, lines_done)
    return accelerator


def aoc2020_8_a(lines: list):
    try:
        accelerator = op_fun(lines, 0, 0)
        return accelerator
    except ValueError as e:
        return e
    except Exception as e:
        return e


def aoc2020_8_b(lines: list):
    for i in range(len(lines)):
        if "nop" in lines[i] or "jmp" in lines[i]:
            lines2 = deepcopy(lines)
            if "nop" in lines2[i]:
                lines2[i] = lines2[i].replace("nop", "jmp")
            else:
                lines2[i] = lines2[i].replace("jmp", "nop")
            try:

                accelerator = op_fun(lines2, 0, 0)

                return accelerator
            except ValueError:
                pass
            except Exception:
                pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(aoc2020_8_a(read_file("day8.txt")))
    print(aoc2020_8_b(read_file("day8.txt")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from datetime import time
from exceptions.load_exceptions import incorrect_file_type, incorrect_runner_field, empty_runner_field, empty_file

def get_data(file_name = 'competencia.txt'):
    if ".txt" in file_name:
        file = open(f"parcial_1/competencia.txt", "rt")
        validate_file(file)
        file.seek(0)
        data = arrange_data(file)
        file.close()
        return data
    else:
        raise incorrect_file_type("The file type is not .txt")

def validate_runner(line, pointer):
    if '' in line:
        raise empty_runner_field(f'There is an empty field on runner, please check line {pointer}.')
    if len(line) != 10:
        raise incorrect_runner_field(f"Incomplete or excess of runner information, please check line {pointer}.")
    if len(line) == 10:
        if not (line[5].upper() == 'M' or line[5].upper() == 'F'):
            raise incorrect_runner_field(f"Incorrect runner sex format, please check line {pointer}.")
        if not line[0].isnumeric():
            raise incorrect_runner_field(f"Incorrect runner ID format, please check line {pointer}.")
        if not line[6].isnumeric():
            raise incorrect_runner_field(f"Incorrect runner age format, please check line {pointer}.")
        if line[6].isnumeric():
            if int(line[6]) < 1:
                raise incorrect_runner_field(f"Incorrect runner age format, please check line {pointer}.")
        if not line[7].isnumeric() or not line[8].isnumeric() or not line[9].isnumeric():
            raise incorrect_runner_field(f"Incorrect runner time, please check line {pointer}.")
        if line[7].isnumeric() and line[8].isnumeric() and line[9].isnumeric():
            if int(line[7]) < 0 or int(line[8]) < 0 or int(line[9]) < 0:
                raise incorrect_runner_field(f"Incorrect runner time, please check line {pointer}.")

def validate_file(file):
    pointer = 0
    for line in file:
        pointer += 1
        validate_runner(line.strip().split(','),pointer)
    if pointer == 0:
        raise empty_file("the file is empty.")

def arrange_data(f):
    data = []
    for line in f:
        data.append(line.strip().split(','))
    return data     
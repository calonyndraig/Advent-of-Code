import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(3,2025)

battery_banks = get_source.string_convert_to_list(input)

def find_highest_charge(bank):
    
    first_digit_highest = int(bank[0])
    first_digit_index = 0
    for i in range(1, len(bank)-1): # checking for highest first possible digit
        print("Checking first index at ", i)
        print("Current highest first digit: ", first_digit_highest)
        print("Current highest first digit index: ", first_digit_index)
        digit = int(bank[i])
        if digit > first_digit_highest:
            first_digit_highest = digit
            first_digit_index = i

        if first_digit_highest == 9:
            print("Found a 9, breaking loop")
            break

    second_digit_highest = int(bank[first_digit_index+1])
    second_digit_index = first_digit_index+1
    for i in range(second_digit_index, len(bank)):
        print("Checking second index at ", i)
        print("Current highest second digit: ", second_digit_highest)
        print("Current highest second digit index: ", second_digit_index)
        second_digit = int(bank[i])
        if second_digit > second_digit_highest:
            second_digit_highest = second_digit
            second_digit_index = i
        if second_digit_highest == 9:
            print("Found a 9, breaking loop")
            break

    highest_charge = int(str(first_digit_highest) + str(second_digit_highest))

    return highest_charge

total_charge = 0
for bank in battery_banks:
    bank_charge = find_highest_charge(bank)
    total_charge += bank_charge

print(total_charge)


import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(3,2025)

battery_banks = get_source.string_convert_to_list(input)

CURRENT_STRING = ""

def find_next_digit(bank,start_index,end_index):
    highest_digit = int(bank[start_index])
    highest_index = start_index
    for i in range(start_index, end_index):
        # print("Checking index at ", i)
        # print("Current highest digit: ", highest_digit)
        # print("Current highest digit index: ", highest_index)
        digit = int(bank[i])
        if digit > highest_digit:
            highest_digit = digit
            highest_index = i

        if highest_digit == 9:
            # print("Found a 9, breaking loop")
            break
    global CURRENT_STRING
    CURRENT_STRING += str(highest_digit)

    if end_index < len(bank):
        return find_next_digit(bank,highest_index+1,end_index+1)

        
    return CURRENT_STRING

last_index = len(battery_banks[0]) - 11

total_charge = 0
for bank in battery_banks:
    CURRENT_STRING = ""
    bank_charge = find_next_digit(bank,0,last_index)
    total_charge += int(bank_charge)

print(total_charge)

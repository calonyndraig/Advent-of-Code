import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(1,2025)

moves_list = get_source.string_convert_to_list(input)

clicks_list = [x for x in range(100)]

print(clicks_list)

CURRENT_ZEROS = 0

def move_right(current_position, number, CURRENT_ZEROS):
    
    idx = current_position

    for _ in range(number):
        idx = (idx + 1) % 100
        if idx == 0:
            CURRENT_ZEROS += 1

    return idx, CURRENT_ZEROS

def move_left(current_position,number,CURRENT_ZEROS):
    
    idx = current_position

    for _ in range(number):
        idx = (idx - 1) % 100
        # print(idx)
        if idx == 0:
            CURRENT_ZEROS += 1
        # print(CURRENT_ZEROS)

    return idx, CURRENT_ZEROS


idx = 50

for move in moves_list:
    direction = move[0]
    number = int(move[1:])
    print("Starting move...")
    print("Current index = ", idx)
    print("Direction = ", direction)
    print("Number = ", number)
    if direction == "L":
        idx, CURRENT_ZEROS = move_left(idx, number, CURRENT_ZEROS)
    if direction == "R":
        idx, CURRENT_ZEROS = move_right(idx, number, CURRENT_ZEROS)
    print("Final stop = ", idx)
    print("Current Zeroes: ", CURRENT_ZEROS)



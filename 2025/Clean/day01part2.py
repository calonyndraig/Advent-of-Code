import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(1,2025)

moves_list = get_source.string_convert_to_list(input)

CURRENT_ZEROS = 0 # sets global count of zeroes passed in the list

def move_right(current_position, number, CURRENT_ZEROS):
    """
    Uses the current position and the number of moves to click through the "lock" and record the number of times zero is passed.
    """
    
    idx = current_position

    for _ in range(number): # rotates through all numbers 0 to 99 forwards, starting with the current position
        idx = (idx + 1) % 100 # ensures position "resets" to zero anytime it hits 100
        if idx == 0:
            CURRENT_ZEROS += 1 # if zero is passed, updates total

    return idx, CURRENT_ZEROS # returns the new position + the updated global variable

def move_left(current_position,number,CURRENT_ZEROS):
    """
    Uses the current position and the number of moves to click through the "lock" backwards and record the number
    of times zero is passed.
    """
    
    idx = current_position

    for _ in range(number): # rotates through all numbers 0 to 99 backwards, starting with the current position
        idx = (idx - 1) % 100 # ensures position "resets" to zero and to positive numbers anytime it hits 100
        if idx == 0:
            CURRENT_ZEROS += 1 # if zero is passed, updates total

    return idx, CURRENT_ZEROS # returns the new position + the updated global variable.


idx = 50 # lock starts at 50

for move in moves_list: 
    direction = move[0] # splits string into direction + number
    number = int(move[1:])
    
    if direction == "L": # if direction is left, uses move_left() to fetch new current position and update zeroes total
        idx, CURRENT_ZEROS = move_left(idx, number, CURRENT_ZEROS)
    if direction == "R": # if direction is right, uses move_right() to fetch new current position and update zeroes total
        idx, CURRENT_ZEROS = move_right(idx, number, CURRENT_ZEROS)

print("Final Zeroes Count: ", CURRENT_ZEROS)


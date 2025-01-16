"""For challenge found at https://adventofcode.com/2024/day/7"""

import os
import sys
from collections import deque

# Fallback to script directory if current working directory is incorrect
script_dir = os.path.dirname(sys.argv[0])
file_path = os.path.join(script_dir, "input_files/day_07.txt")

with open(file_path, "r") as file:
    entries = [x.strip() for x in file.readlines()]
    # creates list of entries

def prep_data(entry):
    """Formats entry for processing"""
    total, operands = entry.split(': ')
    total = int(total)
    operands = [int(x) for x in operands.split()]
    return total, operands

def test_entry(goal, operands, current_result=0):
    """
    Uses recursion to attempt all combinations of addition, multiplication,
    and concatenation; returns True if goal is possible using only operands
    """
    if not operands:
        return current_result == goal
    
    next_test = operands[0]
    remaining_test = operands[1:]

    if test_entry(goal,remaining_test,current_result+next_test):
        return True
    if test_entry(goal,remaining_test,current_result*next_test): 
        return True
    if test_entry(goal,remaining_test,int(str(current_result)+str(next_test))):
        return True

    return False


calibration = 0
for entry in entries:
    goal, operands = prep_data(entry)
    if test_entry(goal,operands): # if possible, adds goal to calibration total
        calibration += goal

print(calibration)
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

def test_entry(goal, operands):
    """
    Uses deque to attempt all combinations of addition and multiplication;
    returns True if goal is possible using only operands
    """

    queue = deque([tuple((0,-1))]) # default set to zero and current_op to negative one
    visited = set([tuple((0,-1))]) # list of totaled numbers and current_op, avoids loops

    required_loops = len(operands)-1
    
    while queue:
        
        current_total, previous_op = queue.popleft()
        current_op = previous_op + 1

        if current_total == goal:
            return True
        
        if current_op > required_loops:
            continue
        
        test_sum = current_total + operands[current_op]
        if test_sum <= goal and tuple((test_sum, current_op)) not in visited:
            visited.add(tuple((test_sum, current_op)))
            queue.append(tuple((test_sum, current_op)))

        test_prod = current_total * operands[current_op]
        if test_prod <= goal and tuple((test_prod, current_op)) not in visited:
            visited.add(tuple((test_prod, current_op)))
            queue.append(tuple((test_prod, current_op)))

    return False




calibration = 0
for entry in entries:
    goal, operands = prep_data(entry)
    if test_entry(goal,operands): # if possible, adds goal to calibration total
        calibration += goal

print(calibration)
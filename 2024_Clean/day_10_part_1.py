"""For challenge found at https://adventofcode.com/2024/day/10"""

import os
import sys
from collections import deque

# Fallback to script directory if current working directory is incorrect
# Basically keeps me from encountering errors during debugging

script_dir = os.path.dirname(sys.argv[0])
file_path = os.path.join(script_dir, "input_files/day_10.txt")

with open(file_path, "r") as file:
    puzzle = [x.strip() for x in file.readlines()]
    # returns list of strings

def prep_data(data):
    """converts list of string to 2d array of ints"""

    trail_map = []
    for line in data:
        ints = [int(x) for x in line]
        trail_map.append(ints)
    return trail_map

def identify_trailheads(trail_map):
    """creates deque of coordinates of trailheads"""

    to_check = deque()

    for row_num, row in enumerate(trail_map):
        for col_num, num in enumerate(row):
            if num == 0:
                to_check.append([(row_num, col_num)])

    return to_check
    
def find_paths(to_check,trail_map):
    """identifies potential trail endings for trailheads"""
    
    coord_dict = {}
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    while to_check:

        temp = to_check.pop()

        
        if len(temp) == 10: # if path has reached 9
            if temp[0] in coord_dict:
                if temp[-1] not in coord_dict[temp[0]]:
                # check prevents multiple paths counted for single ending 
                    coord_dict[temp[0]].append(temp[-1])
            else:
                coord_dict[temp[0]] = [temp[-1]]
                #creates dictionary of trailheads with concluding coordinates
            continue

        # this section checks each direction for potential next step in the path
        # if there is a next step, adds the coordinate and returns it to the 
        # queue to check again
        x,y = temp[-1]
        next_step = trail_map[x][y] + 1
        for d in directions:
            newx, newy = x+d[0], y+d[1]
            if newx >= 0 and newx <= len(trail_map)-1 and newy >= 0 and newy <=len(trail_map[0])-1:
                if trail_map[newx][newy] == next_step:
                    new_temp = temp + [(newx,newy)]
                    to_check.append(new_temp)
    
    return coord_dict
    # returns the final dictionary

def total_scores(coord_dict):
    """totals the scores of all trailheads"""
    total_score = 0

    for trail in coord_dict.keys():
        total_score += len(coord_dict[trail])
        # the length of the value is the number of
        # path endings found from the trailhead

    return total_score

matrix = prep_data(puzzle)
trailheads = identify_trailheads(matrix)
paths = find_paths(trailheads,matrix)
final_score = total_scores(paths)
print(final_score)

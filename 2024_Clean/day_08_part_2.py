"""For challenge found at https://adventofcode.com/2024/day/8"""

import os
import sys
from itertools import combinations

# Fallback to script directory if current working directory is incorrect
script_dir = os.path.dirname(sys.argv[0])
file_path = os.path.join(script_dir, "input_files/day_08.txt")

with open(file_path, "r") as file:
    map = [x.strip() for x in file.readlines()]
    # creates map in list form

def prep_data(map):
    """
    Parses map into list of lists containing coordinates
    of matching nodes 
    """
    location_dict = {} # dictionary of coords associated with specific node types
    for index, row in enumerate(map):
        for col_num, item in enumerate(row):
            if item != '.':
                if item in location_dict:
                    location_dict[item].append((index,col_num))
                else:
                    location_dict[item] = [(index,col_num)]
    
    # creates groups of matching node coordinates
    node_groups = [x for x in location_dict.values()]
    
    return node_groups

antinode_set = set() # to keep track of antinodes found
max_x = len(map) - 1
max_y = len(map[0]) - 1

def find_antinodes(node_set):
    """identifies antinodes in a given set of nodes"""
    
    global antinode_set

    node_combos = list(combinations(node_set,2))
    # for all possible combinations of matching nodes

    def calc_antinodes(coord1,coord2):
        # calculates the possible antinodes of two given nodes
        x1, y1 = coord1
        x2, y2 = coord2
        
        multiplier = 2 # uses multipliers to include modified constraints
        new_x, new_y = (multiplier*x1 - (multiplier-1)*x2, multiplier*y1-(multiplier-1)*y2)
        while new_x >= 0 and new_x <= max_x and new_y >= 0 and new_y <= max_y:
            antinode_set.add((new_x,new_y))
            multiplier += 1
            new_x, new_y = (multiplier*x1 - (multiplier-1)*x2, multiplier*y1-(multiplier-1)*y2)

        multiplier = 2
        new_x, new_y = (multiplier*x2 - (multiplier-1)*x1, multiplier*y2-(multiplier-1)*y1)
        while new_x >= 0 and new_x <= max_x and new_y >= 0 and new_y <= max_y:
            antinode_set.add((new_x,new_y))
            multiplier += 1
            new_x, new_y = (multiplier*x2 - (multiplier-1)*x1, multiplier*y2-(multiplier-1)*y1)

    for item in node_combos:
        if len(item) > 1: # if node has at least one partner, all nodes are also antinodes
            for node in item:
                antinode_set.add(node)
        calc_antinodes(item[0],item[1])
    
    return


node_locations = prep_data(map)
for group in node_locations:
    find_antinodes(group)

print(len(antinode_set)) # displays length of unique antinode list
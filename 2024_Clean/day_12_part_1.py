"""For challenge found at https://adventofcode.com/2024/day/12"""

import os
import sys
from collections import deque

# Fallback to script directory if current working directory is incorrect
# Basically keeps me from encountering errors during debugging

script_dir = os.path.dirname(sys.argv[0])
file_path = os.path.join(script_dir, "input_files/day_12.txt")

with open(file_path, "r") as file:
    puzzle = [list(x.strip()) for x in file.readlines()]
    # creates 2D array of lists of characters in garden map

def prep_tools(data):
    """creates a tracker for visited plots"""
    rows, cols = len(data), len(data[0])
    visited = [[False] * cols for _ in range(rows)] 
    return visited

visited_tracker = prep_tools(puzzle)
directions = [(1,0),(-1,0),(0,1),(0,-1)] # to use for reviewing connected plots

def id_region(coord):
    """Identifies the specific coords within a region as well as its edge locations"""
    
    global visited_tracker

    x, y = coord
    plant_type = puzzle[x][y]
    to_check = deque([(coord)])
    region = set()
    edges = set()
    
    while to_check:

        current_x, current_y = to_check.popleft()
        
        # checks if we've already added it to the region
        # if we have, skips to next item to check
        # if we have not, adds to region and continues within loop
        if (current_x, current_y) in region:
            continue
        region.add((current_x, current_y))

        for dx, dy in directions:
            new_x, new_y = current_x + dx, current_y + dy
            if new_x >= 0 and new_x < len(puzzle) and new_y >= 0 and new_y < len(puzzle[0]):
                if puzzle[new_x][new_y] == plant_type:
                    # if we haven't already added item to another region
                    if not visited_tracker[new_x][new_y]:
                        to_check.append((new_x,new_y))
                else:
                    edges.add(((current_x,current_y),(new_x,new_y)))
                    # adds to edge if incorrect plant type
            else:
                edges.add(((current_x,current_y),(new_x,new_y)))
                # adds to edge if exceeds bounds of map

    return region, edges

def traverse_map(map):
    """
    Goes though each item within the map, and if it has not yet been assigned to a region,
    it builds a region around it.
    """

    regions =[] # list of all regions and edges

    for row_num, row in enumerate(map):
        for col_num, col in enumerate(row):
            if not visited_tracker[row_num][col_num]:
                region, edges = id_region((row_num, col_num))
                regions.append((region, edges))
                for plot in region:
                    visited_tracker[plot[0]][plot[1]] = True

    return regions


regions = traverse_map(puzzle)
total_price = 0

for region in regions:
    current_price = len(region[0]) * len(region[1]) # length of region = area, length of edges = perimeter
    total_price += current_price

print(total_price)
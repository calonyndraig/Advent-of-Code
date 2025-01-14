"""For challenge found at https://adventofcode.com/2024/day/6"""

# This code is very slow, but it works. I will see if I can find a better way later.

import os
import sys
import copy

# Fallback to script directory if current working directory is incorrect
script_dir = os.path.dirname(sys.argv[0])
file_path = os.path.join(script_dir, "input_files/day_06.txt")

with open(file_path, "r") as file:
    init_matrix = [list(x.strip()) for x in file.readlines()] 
    # creates list of lists to simulate warehouse


guards = {'^' : [(-1,0),0], # up        For directional maker, assigns direction coords and an order number 
        '>' : [(0,1), 1], # right
        'v' : [(1,0), 2], # down
        '<' : [(0,-1),3], # left
    }

order_guards = {0:'^', 1:'>', 2:'v', 3:'<'}  # assigns new guard based on order number

def prep_data(matrix):
    """finds start position, direction, and order"""

    start_guards = [((i, j), guards[value]) for i, row in enumerate(matrix) for j, value in enumerate(row) if value in guards]
    startinfo = start_guards[0]
    return startinfo

def init_walk_matrix(init_matrix,startpos,direction,order):
    """traverses matrix, returning list of where guard walks"""
    norm_path = set() #initializes set of coordinates to try later
    matrix = copy.deepcopy(init_matrix)
    start_x, start_y = startpos
    dir_x, dir_y = direction
    new_x, new_y = start_x + dir_x, start_y + dir_y
    
    norm_path.add((startpos))
    
    while 0 <= new_x and new_x < len(matrix) and 0 <= new_y and new_y < len(matrix[0]):
        # while loop exits when the guard is about to walk out of the matrix
        if matrix[new_x][new_y] == '.':
            # if path is clear, adds new position to path, 
            # moves guard, and marks previous position with "."
            norm_path.add(((new_x,new_y))) 
            matrix[new_x][new_y] = matrix[start_x][start_y]
            matrix[start_x][start_y] = "."
            start_x, start_y = new_x, new_y
            new_x, new_y = new_x, new_y = start_x + dir_x, start_y + dir_y

        elif matrix[new_x][new_y] == '#':
            # if path is not clear, changes direction
            new_order = (order + 1) % 4
            matrix[start_x][start_y] = order_guards[new_order]
            direction = guards[matrix[start_x][start_y]][0]
            dir_x, dir_y = direction
            new_x, new_y = start_x + dir_x, start_y + dir_y
            order = new_order

    matrix[start_x][start_y] = "." # marks final position with "."
    
    return list(norm_path)



def loop_check(matrix, startpos, direction, order):
    """traverses matrix with new obstacle, checks for loop"""
    visited = {} # for recording obstacles hit

    start_x, start_y = startpos
    dir_x, dir_y = direction
    new_x, new_y = start_x + dir_x, start_y + dir_y

    while 0 <= new_x and new_x < len(matrix) and 0 <= new_y and new_y < len(matrix[0]):
        # while loop exits when the guard is about to walk out of the matrix
        if matrix[new_x][new_y] == '.':
            # if path is clear, moves guard, marks previous position with "."
            matrix[new_x][new_y] = matrix[start_x][start_y]
            matrix[start_x][start_y] = "."
            start_x, start_y = new_x, new_y
            new_x, new_y = new_x, new_y = start_x + dir_x, start_y + dir_y

        elif matrix[new_x][new_y] == '#':
            # if path is not clear, checks for recurrence,
            # then changes direction
            if (new_x, new_y) in visited:
                if direction in visited[(new_x,new_y)]:
                    return True 
                    # returns True if same obstacle hit from same direction
                else:
                    visited[(new_x,new_y)].append(direction)
                    # adds direction to obstacle if previously hit
            else:
                visited[(new_x,new_y)] = [direction] # adds obstacle and direction
            new_order = (order + 1) % 4
            matrix[start_x][start_y] = order_guards[new_order]
            direction = guards[matrix[start_x][start_y]][0]
            dir_x, dir_y = direction
            new_x, new_y = start_x + dir_x, start_y + dir_y
            order = new_order

    return False # returns false if guard makes it out of warehouse

total_loops = 0
start_pos, direction_and_order = prep_data(init_matrix)
direction, order = direction_and_order # unpacks direction_and_order
standard_path = init_walk_matrix(init_matrix,start_pos,direction,order)

for coord in standard_path:
    matrix = copy.deepcopy(init_matrix)
    obs_x, obs_y = coord
    matrix[obs_x][obs_y] = "#"
    if loop_check(matrix,start_pos,direction,order):
        total_loops += 1

print(total_loops)
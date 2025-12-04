import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(4,2025)

factory_rows = get_source.string_convert_to_list(input)

# print(factory_rows)

factory_grid = []

for i in range(len(factory_rows)):
    factory_grid.append([char for char in factory_rows[i]])

block_dict = {}        

def check_up(row_num, col_num):  # is there paper above block?
    global factory_grid 
    if row_num == 0:
        return False
    if factory_grid[row_num-1][col_num] == "@":
        return True
    return False

def check_up_right(row_num, col_num):
    global factory_grid
    if row_num == 0 or col_num == len(factory_grid[0])-1: 
        return False
    if factory_grid[row_num-1][col_num+1] == "@":
        return True
    return False

def check_up_left(row_num,col_num):
    global factory_grid
    if row_num == 0 or col_num == 0:
        return False
    if factory_grid[row_num-1][col_num-1] == "@":
        return True
    return False

def check_left(row_num,col_num):
    global factory_grid
    if col_num == 0:
        return False
    if factory_grid[row_num][col_num-1] == "@":
        return True
    return False
    
def check_right(row_num,col_num):
    global factory_grid
    if col_num == len(factory_grid[0])-1:
        return False
    if factory_grid[row_num][col_num+1] == "@":
        return True
    return False

def check_down(row_num,col_num):
    global factory_grid
    if row_num == len(factory_grid)-1:
        return False
    if factory_grid[row_num+1][col_num] == "@":
        return True
    return False

def check_down_right(row_num,col_num):
    global factory_grid
    if row_num == len(factory_grid)-1 or col_num == len(factory_grid[0])-1:
        return False
    if factory_grid[row_num+1][col_num+1] == "@":
        return True
    return False

def check_down_left(row_num,col_num):
    global factory_grid
    if row_num == len(factory_grid)-1 or col_num == 0:
        return False
    if factory_grid[row_num+1][col_num-1] == "@":
        return True
    return False
    
def check_block(row_num,col_num): # check if spot is accessible
    global factory_grid
    if factory_grid[row_num][col_num] != "@":
        return False # if spot doesn't hold "@"
    else:
        if (row_num,col_num) not in block_dict:
            block_dict[(row_num,col_num)] = 0
        if check_up(row_num,col_num):
            block_dict[(row_num,col_num)] += 1
        if check_up_right(row_num,col_num):
            block_dict[(row_num,col_num)] += 1
        if check_up_left(row_num,col_num):
            block_dict[(row_num,col_num)] += 1
        if check_right(row_num,col_num):
            block_dict[(row_num,col_num)] += 1
        if check_left(row_num,col_num):
            block_dict[(row_num,col_num)] += 1
        if check_down(row_num,col_num):
            block_dict[(row_num,col_num)] += 1
        if check_down_left(row_num,col_num): 
            block_dict[(row_num,col_num)] += 1
        if check_down_right(row_num,col_num):
            block_dict[(row_num,col_num)] += 1
        if block_dict[(row_num,col_num)] < 4:
            return True
    return False

blocks_to_remove = True
blocks_removed = 0

while blocks_to_remove:
    total_accessible = 0
    for i in range(len(factory_grid)): # rows
        for j in range(len(factory_grid[i])): #cols
            if check_block(i,j):
                total_accessible += 1
                factory_grid[i][j] = "."
                blocks_removed += 1
    if total_accessible == 0:
        blocks_to_remove = False
    print(total_accessible)
    block_dict = {}

print(blocks_removed)
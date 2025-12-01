import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(1,2025)

moves_list = get_source.string_convert_to_list(input)

current_lock_location = 50 # lock starts at 50

current_zeros = 0 # for counting number of times zero is hit

for move in moves_list: # converts individual strings to a direction + a number of moves
    direction = move[0] 
    number = int(move[1:])
    
    if direction == "L":
        current_lock_location -= number # moves lock position backwards
       
    if direction == "R":
        current_lock_location += number # moves lock position forward
       
    if current_lock_location % 100 == 0:  # checks whether the lock position is a multiple of 100 (i.e., if it landed back on 0)
        current_zeros += 1 # updates current number of zeroes

print("Final Zero Count: ", current_zeros) # prints final answer
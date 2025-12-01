import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(1,2025)

moves_list = get_source.string_convert_to_list(input)

current_lock_location = 50

current_zeros = 0

for move in moves_list:
    direction = move[0]
    number = int(move[1:])
    print("Current move,", move)
    print("Direction = ", direction, "number=", number, "number_type=", type(number))

    if direction == "L":
        print("current location", current_lock_location)
        current_lock_location -= number
        print("new location", current_lock_location)
        
            
    if direction == "R":
        print("current location", current_lock_location)
        current_lock_location += number
        print("new location", current_lock_location)
        
    if current_lock_location % 100 == 0:
        current_zeros += 1
        print("Current zeros", current_zeros)
        

print("Final Zero Count: ", current_zeros)
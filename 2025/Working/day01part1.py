import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(1,2025,"53616c7465645f5fbb067603173994af2e21bebdd2b341a01395e2fb0cc53a062a148cdf70098ffec55fbfb023b471b283dc6403a774ae372c4614a32c682336")

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
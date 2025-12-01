import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

directions = get_source.download_input(1,2015)

direction_dict = {}

for char in directions:
    if char in direction_dict:
        direction_dict[char] += 1
    else:
        direction_dict[char] = 1

final_floor = direction_dict['('] - direction_dict[')']

print("Final Floor: ", final_floor)





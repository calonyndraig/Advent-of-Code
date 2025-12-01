import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

directions = get_source.download_input(1,2015)

current_floor = 0
current_position = 0

for char in directions:
    if char == "(":
        current_floor += 1
    if char == ")":
        current_floor -= 1

    current_position += 1
    
    if current_floor < 0:
        print("Entered basement at position: ", current_position)
        break

        








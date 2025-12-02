import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

directions = get_source.download_input(3,2015)

house_dict = {(0,0): 1}

x, y = 0,0

for dir in directions:
    
    
    if dir == '>':
        x += 1
    elif dir == '<':
        x -= 1
    elif dir == '^':   
        y += 1 
    elif dir == 'v':
        y -= 1
    
    if (x,y) in house_dict:
        house_dict[(x,y)] += 1
    else:
        house_dict[(x,y)] = 1

print(house_dict)
print(len(house_dict))
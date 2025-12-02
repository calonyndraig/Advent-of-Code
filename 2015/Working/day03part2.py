import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

directions = get_source.download_input(3,2015)

house_dict = {(0,0): 1}

santa_x, santa_y = 0,0
robot_x, robot_y = 0,0

Santa = True
Robot = False
for dir in directions:
    
    if Santa:
        if dir == '>':
            santa_x += 1
        elif dir == '<':
            santa_x -= 1
        elif dir == '^':
            santa_y += 1
        elif dir == 'v':
            santa_y -= 1

        if (santa_x,santa_y) in house_dict:
            house_dict[(santa_x,santa_y)] += 1
        else:
            house_dict[(santa_x,santa_y)] = 1
        Santa = False
        Robot = True
        continue
    
    if Robot:
        if dir == '>':
            robot_x += 1
        elif dir == '<':
            robot_x -= 1
        elif dir == '^':
            robot_y += 1
        elif dir == 'v':
            robot_y -= 1

        if (robot_x,robot_y) in house_dict:
            house_dict[(robot_x,robot_y)] += 1
        else:
            house_dict[(robot_x,robot_y)] = 1
        Santa = True
        Robot = False
        continue   


print(house_dict)
print(len(house_dict))
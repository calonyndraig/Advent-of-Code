import re
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source



strings = get_source.download_input(6,2015)

string_list = get_source.string_convert_to_list(strings)

GRID = [[0 for _ in range(1000)] for _ in range(1000)] # 0 equals off, 1 equals on

def parse_string(string):
    x1,y1,x2,y2 = re.findall(r"\d+",string)
    command = (re.match(r"^\D+",string)).group()

    return (command,int(x1),int(y1),int(x2),int(y2))

def turn_on(x,y):
    GRID[x][y] += 1

def turn_off(x,y):
    if GRID[x][y] > 0:
        GRID[x][y] -= 1

def toggle(x,y):
    GRID[x][y] += 2

def apply_command(command,x1,y1,x2,y2):

   for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if command == "turn on ":
                turn_on(i,j)
            elif command == "turn off ":
                turn_off(i,j)
            elif command == "toggle ":
                toggle(i,j)

for string in string_list:
    command, x1,y1,x2,y2 = parse_string(string)
    apply_command(command,x1,y1,x2,y2)


total_brightness = 0
for row in GRID:
    total_brightness += sum(row)    

print(total_brightness)
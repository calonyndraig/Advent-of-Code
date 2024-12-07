import numpy as np
from pip._vendor import requests
import re

url = 'https://adventofcode.com/2024/day/6/input'

session = "53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd"
headers = {
    'Cookie': f'session={session}',
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    # The input data as text
    data = response.text
else:
    data = None

rows = data.splitlines()

warehouse = [list(row) for row in rows]
warehouse_width = len(warehouse[0])
warehouse_height = len(warehouse)




"""
Used for part one
"""

visit_dict = {

}

add_result = False
loop_obstacles = 0

directions = {"up": "^", "right": ">", "down": "v", "left" : "<"}
direction_characters = [value for value in directions.values()]

def initial_guard(current_warehouse,direction="up"):
    matrix_np = np.array(current_warehouse)  # Convert to NumPy array    
    result = np.where(matrix_np == directions[direction])  # Find indices of target
    if result[0].size > 0:  # If target is found
        guard_location = int(result[0][0]), int(result[1][0])
        return guard_location  # Row and column indices
    
guard_start = initial_guard(warehouse)

# def guard_travel(current_warehouse,direction,current_guard_location=None):
    
#     if direction == "up":
#         guard_up(current_warehouse,current_guard_location)
#     if direction == "right":
#         guard_right(current_warehouse,current_guard_location)
#     if direction == "down":
#         guard_down(current_warehouse,current_guard_location)
#     if direction == "left":
#         guard_left(current_warehouse,current_guard_location)
    
        
def guard_up(current_warehouse,guard_location):
    global add_result
    global visit_dict
    current_x = int(guard_location[0])
    current_y = int(guard_location[1])
    
    while current_x > 0:
        
        if current_warehouse[current_x-1][current_y] == ".":
            current_x -= 1
        elif current_warehouse[current_x-1][current_y] == "#":
            
            if (current_x,current_y) not in visit_dict:
                visit_dict[(current_x,current_y)] = {"down": 0, "up": 1, "left": 0, "right" : 0}
            else:
                visit_dict[(current_x,current_y)]["up"] += 1
            print(visit_dict[(current_x,current_y)])
            if visit_dict[(current_x,current_y)]["up"] >= 2:
                add_result = True
                current_x = -1
                break

            new_direction = "right"
            guard_location = (current_x,current_y)
           
            
            print(guard_location, "turning right")
            
            guard_right(current_warehouse,guard_location)
            break
    print("supposedly done")

def guard_right(current_warehouse,guard_location):
    global add_result
    global visit_dict
    current_x = guard_location[0]
    current_y = guard_location[1]

    while current_y < warehouse_width - 1:
        if current_warehouse[current_x][current_y+1] == ".":
            current_y += 1
        elif current_warehouse[current_x][current_y+1] == "#":
            if (current_x,current_y) not in visit_dict:
                visit_dict[(current_x,current_y)] = {"down":  0, "up": 0, "left": 0, "right" : 1}
            else:
                visit_dict[(current_x,current_y)]["right"] += 1
            print(visit_dict[(current_x,current_y)])
            if visit_dict[(current_x,current_y)]["right"] >= 2:
                add_result = True
                current_y = warehouse_width + 1
                break

            new_direction = "down"
            guard_location = (current_x,current_y)
            
            
            print(guard_location, "turning down")
            guard_down(current_warehouse,guard_location)
            break
    print("supposedly done")


def guard_down(current_warehouse,guard_location):
    global add_result
    global visit_dict
    current_x = guard_location[0]
    current_y = guard_location[1]
    
    while current_x < warehouse_height-1:        
        if current_warehouse[current_x+1][current_y] == ".":
            current_x += 1
        elif current_warehouse[current_x+1][current_y] == "#":
            if (current_x,current_y) not in visit_dict:
                visit_dict[(current_x,current_y)] = {"down":  1, "up": 0, "left": 0, "right" : 0}
            else:
                visit_dict[(current_x,current_y)]["down"] += 1
            print(visit_dict[(current_x,current_y)])

            if visit_dict[(current_x,current_y)]["down"] >= 2:
                add_result = True
                current_x = warehouse_height + 1
                break
            
                  
            new_direction = "left"
            guard_location = (current_x,current_y)
            
            print(guard_location, "turning left")
            guard_left(current_warehouse,guard_location)
            break
    print("supposedly done")

        


def guard_left(current_warehouse,guard_location):
    global add_result
    global visit_dict
    current_x = guard_location[0]
    current_y = guard_location[1]
    while current_y > 0:
        
        if current_warehouse[current_x][current_y-1] == ".":
            current_y -= 1
        elif current_warehouse[current_x][current_y-1] == "#":
            
            if (current_x,current_y) not in visit_dict:
                visit_dict[(current_x,current_y)] = {"down":  0, "up": 0, "left": 1, "right" : 0}
            else:
                visit_dict[(current_x,current_y)]["left"] += 1
            print(visit_dict[(current_x,current_y)])

            if visit_dict[(current_x,current_y)]["left"] >= 2:
                add_result = True
                current_y = -1
                break
            
            new_direction = "up"
            guard_location = (current_x,current_y)
            
            print(guard_location, "turning up")
            guard_up(current_warehouse,guard_location)
            break
    print("supposedly done")


            
def test_for_loop(warehouse_mod):
    global visit_dict
    visit_dict = {}
    warehouse_mod[guard_start[0]][guard_start[1]] = "."
    guard_up(warehouse_mod,guard_start)
    

    





def add_obstacle(warehouse_mod):
    global add_result
    global loop_obstacles
    global visit_dict
    for row in warehouse_mod:
        for index, item in enumerate(row):
            if item == "#":
                continue
            elif item != "#":
                row[index] = "#"
                test_for_loop(warehouse_mod)
                row[index] = '.'
                if add_result == True:
                    loop_obstacles += 1
                    add_result = False
                visit_dict = {}
    return loop_obstacles



print(add_obstacle(warehouse))






# def build_warehouse(warehouse):
#     new_rows = [''.join(row) for row in warehouse]
#     new_warehouse = "\n".join(new_rows)
#     print(new_warehouse)
#     count_exes(new_warehouse)

# def count_exes(warehouse):
#     exes = 0
#     for char in warehouse:
#         if char == "X":
# #             exes += 1
# #     print(f"X's = {exes}")






# guard_travel(warehouse,"up")





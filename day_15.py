# import numpy as np
from pip._vendor import requests
# import re

"""
dataparsing
"""

def fetch_data(url,session):
    headers = {
    'Cookie': f'session={session}',
        }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # The input data as text
        data = response.text
    else:
        data = None

    return data

def parse_data(data):
    data = data.split('\n\n')
    warehouse_matrix = create_warehouse(data[0])
    with open("directions_list.txt", "w") as file:
        file.write(data[1])
    directions = create_directions(data[1])
    # print(warehouse_matrix)
    # print(directions)
    return warehouse_matrix, directions

def create_warehouse(data):
    warehouse_rows = data.splitlines()
    warehouse = []
    for row in warehouse_rows:
        warehouse.append(list(row))
    return warehouse

def create_directions(data):
    directions_list = [x for x in data if x != "\n"]
    return directions_list

def double_warehouse(warehouse):
    x = 0
    y = 0
    while x < len(warehouse) and y < len(warehouse[0]):
        if warehouse[x][y] == "#":
            warehouse[x].insert(y+1,"#")
        elif warehouse[x][y] == ".":
            warehouse[x].insert(y+1,'.')
        elif warehouse[x][y] == "O":
            warehouse[x][y] = '['
            warehouse[x].insert(y+1,']')
        elif warehouse[x][y] == '@':
            warehouse[x].insert(y+1,'.')
        y+=2
        if y >= len(warehouse[0]):
            y = 0
            x += 1

    warehouse_image = "\n".join(" ".join(map(str, row)) for row in warehouse)        
    print(warehouse_image)
    return warehouse




"""
global variables
"""

direction_dict = {
    'v' : "down",
    '<' : "left",
    '^' : "up",
    '>' : "right"
}

symbol_dict = {
    '@' : 'robot',
    "#" : 'wall',
    "O" : 'box',
    "." : 'empty'
}

def initialize_robot_pos(warehouse):
    for i, row in enumerate(warehouse):
        for j, item in enumerate(row):
            if item == "@":
                robot_pos = (i,j)
                break
    return robot_pos

def attempt_move(direction,warehouse,robot_pos):
    global direction_dict
    x,y = robot_pos
    if direction_dict[direction] == "down":
        new_location_item,pos = warehouse[x+1][y], (x+1,y)
        direction = "down"
    elif direction_dict[direction] == "up":
        new_location_item,pos = warehouse[x-1][y], (x-1,y)
        direction = "up"
    elif direction_dict[direction] == "right":
        new_location_item,pos = warehouse[x][y+1], (x,y+1)
        direction = "right"
    elif direction_dict[direction] == "left":
        new_location_item,pos = warehouse[x][y-1], (x, y-1)
        direction = "left"
    return new_location_item,pos,direction,warehouse

def move(robot_pos,new_location_item,pos,direction,warehouse):
    x,y = robot_pos
    nx,ny = pos
    if new_location_item == '#':
        return warehouse, robot_pos
    elif new_location_item == '.':
        robot_pos = (nx,ny)
        warehouse[x][y] = '.'
        warehouse[nx][ny] = '@'
    elif new_location_item == 'O':
        next_x,next_y = (nx,ny)
        while new_location_item == 'O':
            if direction == "up":
                next_x,next_y = (next_x-1,next_y)
            elif direction == "down":
                next_x,next_y = (next_x+1,next_y)
            elif direction == "right":
                next_x,next_y = (next_x,next_y+1)
            elif direction == "left":
                next_x,next_y = (next_x,next_y-1)
            new_location_item = warehouse[next_x][next_y]
            if new_location_item == "#":
                return warehouse, robot_pos
            elif new_location_item == '.':
                warehouse[next_x][next_y] = 'O'
                warehouse[nx][ny] = '@'
                robot_pos = (nx,ny)
                warehouse[x][y] = '.'
    # warehouse_image = "\n".join(" ".join(map(str, row)) for row in warehouse)
    # with open("robot_matrixes.txt", "a") as file:
    #     file.write(warehouse_image + "\n")
    return warehouse, robot_pos






def iterate_directions(directions_list,warehouse,robot_pos):
    for direction in directions_list:
        new_location_item,pos,direction,warehouse = attempt_move(direction,warehouse,robot_pos)
        warehouse, robot_pos = move(robot_pos,new_location_item,pos,direction,warehouse)
    return warehouse, robot_pos

def calculate_box_coordinates(warehouse):
    total_score = 0
    for row_num, row in enumerate(warehouse):
        for col_num, item in enumerate(row):
            if item == "O":
                box_score = 100 * row_num + col_num
                total_score += box_score
    return total_score


if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/15/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    warehouse, directions_list = parse_data(data)
    warehouse = double_warehouse(warehouse)
    robot_pos = initialize_robot_pos(warehouse)
    # warehouse, robot_pos = iterate_directions(directions_list,warehouse,robot_pos)
    # total_score = calculate_box_coordinates(warehouse)
    # print(total_score)
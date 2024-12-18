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

data = fetch_data('https://adventofcode.com/2024/day/15/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")

lines = data.splitlines()

# def parse_data(data):
#     data = data.split('\n\n')
#     warehouse_matrix = create_warehouse(data[0])
#     with open("directions_list.txt", "w") as file:
#         file.write(data[1])
#     directions = create_directions(data[1])
#     # print(warehouse_matrix)
#     # print(directions)
#     return warehouse_matrix, directions

# def create_warehouse(data):
#     warehouse_rows = data.splitlines()
#     warehouse = []
#     for row in warehouse_rows:
#         warehouse.append(list(row))
#     return warehouse





x_bound = len(lines[0]) * 2
warehouse_map = dict()
m = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1)
}
moves = []
robot = tuple()
switch = False
for y, this_line in enumerate(lines):
    if this_line == '':
        y_bound = y
        switch = True
    if not switch:
        for x, this_char in enumerate(this_line):
            if this_char == '@':
                robot = (x * 2, y)
                warehouse_map[(x * 2, y)] = '@'
                warehouse_map[(x * 2 + 1, y)] = '.'
            elif this_char == 'O':
                warehouse_map[(x * 2, y)] = '['
                warehouse_map[(x * 2 + 1, y)] = ']'
            else:
                warehouse_map[(x * 2, y)] = this_char
                warehouse_map[(x * 2 + 1, y)] = this_char
    else:
        for this_char in this_line:
            moves.append(this_char)


def print_map(w_map: dict):
    print()


for move in moves:
    dx, dy = m[move]  # Get the direction we're moving in
    move_possible = True  # If we hit a wall, this will turn False
    movers = {robot: warehouse_map[robot]}  # Things that will move if move_possible is still True at the end
    rx, ry = robot
    to_check = [(rx, ry)]
    # Since we could potentially be moving lots of stuff at once, we'll keep a queue of things we're going to move
    # that we need to check we have room for. When moving horizontally, we'll only add the far side of a box to this
    # queue, since that's the side that could potentially hit a wall. Whe moving vertically, we'll add both sides of
    # each box to the queue since either side could hit a wall (or a new box).
    while to_check:
        cx, cy = to_check.pop()  # My actual location
        mx, my = cx + dx, cy + dy  # The location I want to move to
        if move == '<':
            if warehouse_map[(mx, my)] == ']':
                # We are moving left and we found the right side of the box. Add it and the left side to the movers
                # dictionary and then add the left side of the box to the queue to make sure it has room to move
                movers[(mx, my)] = warehouse_map[(mx, my)]
                movers[(mx - 1, my)] = warehouse_map[(mx - 1, my)]
                to_check.append((mx - 1, my))
            elif warehouse_map[(mx, my)] == '#':
                # We found a wall. No move is possible. Stop checking.
                move_possible = False
                break
        elif move == '>':
            if warehouse_map[(mx, my)] == '[':
                # We are moving right and we found the left side of the box. Add it and the right side to the movers
                # dictionary and then add the right side of the box to the queue to make sure it has room to move
                movers[(mx, my)] = warehouse_map[(mx, my)]
                movers[(mx + 1, my)] = warehouse_map[(mx + 1, my)]
                to_check.append((mx + 1, my))
            elif warehouse_map[(mx, my)] == '#':
                # We found a wall. No move is possible. Stop checking.
                move_possible = False
                break
        elif move in '^v':
            if warehouse_map[(mx, my)] == '[':
                # We are moving vertically and we found the left side of a box. Add it and the right side to the
                # movers dictionary and then add both sides to the queue to make sure it has room to move
                movers[(mx, my)] = warehouse_map[(mx, my)]
                movers[(mx + 1, my)] = warehouse_map[(mx + 1, my)]
                to_check.extend([(mx, my), (mx + 1, my)])
            elif warehouse_map[(mx, my)] == '#':
                # We found a wall. No move is possible. Stop checking.
                move_possible = False
                break
            elif warehouse_map[(mx, my)] == ']':
                # We are moving vertically and we found the right side of a box. Add it and the left side to the movers
                # dictionary and then add both sides tot he queue to make sure it has room to move
                movers[(mx, my)] = warehouse_map[(mx, my)]
                movers[(mx - 1, my)] = warehouse_map[(mx - 1, my)]
                to_check.extend([(mx, my), (mx - 1, my)])

    if move_possible:
        # Set all the original locations to '.' in the warehouse_map
        for this_loc in movers:
            warehouse_map[this_loc] = '.'
        # Move everyone to their new location
        for this_mover in movers:
            mx, my = this_mover
            warehouse_map[(mx + dx, my + dy)] = movers[this_mover]
        robot = (rx + dx, ry + dy)
        warehouse_map[robot] = '@'

gps_sum = 0
for coord in warehouse_map:
    cx, cy = coord
    if warehouse_map[coord] == '[':
        gps_sum += cx + 100 * cy
# print_map(warehouse_map)
print(gps_sum)




# def create_directions(data):
#     directions_list = [x for x in data if x != "\n"]
#     return directions_list

# def double_warehouse(warehouse):
#     x = 0
#     y = 0
#     while x < len(warehouse) and y < len(warehouse[0]):
#         if warehouse[x][y] == "#":
#             warehouse[x].insert(y+1,"#")
#         elif warehouse[x][y] == ".":
#             warehouse[x].insert(y+1,'.')
#         elif warehouse[x][y] == "O":
#             warehouse[x][y] = '['
#             warehouse[x].insert(y+1,']')
#         elif warehouse[x][y] == '@':
#             warehouse[x].insert(y+1,'.')
#         y+=2
#         if y >= len(warehouse[0]):
#             y = 0
#             x += 1

#     warehouse_image = "\n".join(" ".join(map(str, row)) for row in warehouse)        
#     print(warehouse_image)
#     return warehouse




# """
# global variables
# """

# # direction_dict = {
# #     'v' : "down",
# #     '<' : "left",
# #     '^' : "up",
# #     '>' : "right"
# # }

# # symbol_dict = {
# #     '@' : 'robot',
# #     "#" : 'wall',
# #     "O" : 'box',
# #     "." : 'empty'
# # }

# # def initialize_robot_pos(warehouse):
# #     for i, row in enumerate(warehouse):
# #         for j, item in enumerate(row):
# #             if item == "@":
# #                 robot_pos = (i,j)
# #                 break
# #     return robot_pos

# # def attempt_move(direction,warehouse,robot_pos):
# #     global direction_dict
# #     x,y = robot_pos
# #     if direction_dict[direction] == "down":
# #         new_location_item,pos = warehouse[x+1][y], (x+1,y)
# #         direction = "down"
# #     elif direction_dict[direction] == "up":
# #         new_location_item,pos = warehouse[x-1][y], (x-1,y)
# #         direction = "up"
# #     elif direction_dict[direction] == "right":
# #         new_location_item,pos = warehouse[x][y+1], (x,y+1)
# #         direction = "right"
# #     elif direction_dict[direction] == "left":
# #         new_location_item,pos = warehouse[x][y-1], (x, y-1)
# #         direction = "left"
# #     return new_location_item,pos,direction,warehouse

# # def move(robot_pos,new_location_item,pos,direction,warehouse):
# #     x,y = robot_pos
# #     nx,ny = pos
# #     if new_location_item == '#':
# #         return warehouse, robot_pos
# #     elif new_location_item == '.':
# #         robot_pos = (nx,ny)
# #         warehouse[x][y] = '.'
# #         warehouse[nx][ny] = '@'
# #     elif new_location_item == '[' or new_location_item == ']':
# #         return check_boxes(robot_pos,direction,warehouse)

# # def check_boxes(robot_pos,direction,warehouse):
# #     x,y = robot_pos
# #     if direction == "left":
# #         if warehouse[x][y-3] == ".":
# #             warehouse[x][y-3] == '['
# #             warehouse[x][y-2] == ']'
# #             if warehouse[x][y] != "@":
# #                 next_x, next_y = x, y
# #                 while warehouse[next_x][next_y] != "@":
# #                     warehouse[next_x][next_y-1] = '['
# #                     warehouse[next_x][next_y] = ']'
# #                     next_y -= 2
# #                 warehouse[next_x][next_y-1] == '@'
# #                 warehouse[next_x][next_y] == '.'
# #                 robot_pos = (next_x,next_y-1)
# #             elif warehouse[x][y] == "@":
# #                 warehouse[x][y-1] = "@"
# #                 warehouse[x][y] = '.'
# #                 robot_pos = x, y-1
# #             return warehouse, robot_pos
# #         elif warehouse[x][y-3] == "]":
# #             temp_robot_pos = (x, y-2)
# #             warehouse, robot_pos = check_boxes(temp_robot_pos,direction,warehouse)
# #     if direction == "right":
# #         if warehouse[x][y+3] == ".":
# #             warehouse[x][y+3] == ']'
# #             warehouse[x][y+2] == '['
# #             if warehouse[x][y] != "@":
# #                 next_x, next_y = x, y
# #                 while warehouse[next_x][next_y] != "@":
# #                     warehouse[next_x][next_y+1] = ']'
# #                     warehouse[next_x][next_y] = '['
# #                     next_y += 2
# #                 warehouse[next_x][next_y+1] == '@'
# #                 warehouse[next_x][next_y] == '.'
# #                 robot_pos = (next_x,next_y+1)
# #             elif warehouse[x][y] == "@":
# #                 warehouse[x][y+1] = "@"
# #                 warehouse[x][y] = '.'
# #                 robot_pos = x, y+1
# #             return warehouse, robot_pos
# #         elif warehouse[x][y+3] == "[":
# #             temp_robot_pos = (x, y+2)
# #             warehouse,robot_pos = check_boxes(temp_robot_pos,direction,warehouse)
# #     if direction == "up":
# #         warehouse,robot_pos = check_boxes_up(robot_pos,warehouse)
# #     return warehouse, robot_pos

# # def check_boxes_up(robot_pos,warehouse):
# #     x,y = robot_pos
# #     nx, ny = x-1,y
# #     if warehouse[nx][ny] == '.':
# #         warehouse[nx][ny] = '@'
# #         warehouse[x][y] = '.'
# #         nx,ny = robot_pos
# #         return warehouse,robot_pos
# #     elif warehouse[nx][ny] == '#':
# #         return warehouse,robot_pos
# #     elif warehouse[nx][ny] == '[':
# #         box_coords = ((nx,ny),(nx,ny+1))

# #     elif warehouse[nx][ny] == ']':
# #         box_coords = ((nx,ny-1),(nx,ny))
# #         temp_robot_pos = box_coords[0]
# #         warehouse, robot_pos = 


# # def check_boxes_down(robot_pos,warehouse):

# #         #     next_x,next_y = (nx,ny)
# #     #     while new_location_item == 'O':
# #     #         if direction == "up":
# #     #             next_x,next_y = (next_x-1,next_y)
# #     #         elif direction == "down":
# #     #             next_x,next_y = (next_x+1,next_y)
# #     #         elif direction == "right":
# #     #             next_x,next_y = (next_x,next_y+1)
# #     #         elif direction == "left":
# #     #             next_x,next_y = (next_x,next_y-1)
# #     #         new_location_item = warehouse[next_x][next_y]
# #     #         if new_location_item == "#":
# #     #             return warehouse, robot_pos
# #     #         elif new_location_item == '.':
# #     #             warehouse[next_x][next_y] = 'O'
# #     #             warehouse[nx][ny] = '@'
# #     #             robot_pos = (nx,ny)
# #     #             warehouse[x][y] = '.'
# #     # # warehouse_image = "\n".join(" ".join(map(str, row)) for row in warehouse)
# #     # with open("robot_matrixes.txt", "a") as file:
# #     #     file.write(warehouse_image + "\n")
# #     return warehouse, robot_pos






# # def iterate_directions(directions_list,warehouse,robot_pos):
# #     for direction in directions_list:
# #         new_location_item,pos,direction,warehouse = attempt_move(direction,warehouse,robot_pos)
# #         warehouse, robot_pos = move(robot_pos,new_location_item,pos,direction,warehouse)
# #     return warehouse, robot_pos

# # def calculate_box_coordinates(warehouse):
# #     total_score = 0
# #     for row_num, row in enumerate(warehouse):
# #         for col_num, item in enumerate(row):
# #             if item == "O":
# #                 box_score = 100 * row_num + col_num
# #                 total_score += box_score
# #     return total_score


# # if __name__ == "__main__":
# #     data = fetch_data('https://adventofcode.com/2024/day/15/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
# #     warehouse, directions_list = parse_data(data)
# #     warehouse = double_warehouse(warehouse)
# #     robot_pos = initialize_robot_pos(warehouse)
# #     # warehouse, robot_pos = iterate_directions(directions_list,warehouse,robot_pos)
# #     # total_score = calculate_box_coordinates(warehouse)
# #     # print(total_score)
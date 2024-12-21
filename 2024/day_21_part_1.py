from collections import deque
from math import inf

with open("day_21_input.txt", "r") as file:
    input_list = file.readlines()

for index, item in enumerate(input_list):
    input_list[index] = input_list[index][0:4]
    # print(input_list[index])

robot_num_pad = [["7","8","9"],
                 ["4","5","6"],
                 ["1","2","3"],
                 ["#",'0',"A"]]

robot_dir_pad = [["#"],["^"],["A"],
                 ["<"],["v"],[">"]]

robot_num_dict = {}

robot_dir_pad_dict = {} 

directions_dict = {(0,1) : ">",
                   (1,0) : "v",
                   (0,-1) : "<",
                   (-1,0) : "^"}

final_x, final_y = 3,2

for row_num, row in enumerate(robot_num_pad):
    for col_num, item in enumerate(row):
        if item == "#":
            continue
        robot_num_dict[item] = (row_num,col_num)


for row_num, row in enumerate(robot_dir_pad):
    for col_num, item in enumerate(row):
        if item == "#":
            continue
        robot_dir_pad_dict[item] = (row_num,col_num)

def find_shortest_path(pad,start,end):
    shortest_distance = inf
    best_paths = []
    rows, cols = len(pad), len(pad[0])
    path = ''
    queue = deque([(start[0],start[1],0,path)])
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True


    while queue:
        x, y, distance, path = queue.popleft()

        if (x,y) == end:
            if distance < shortest_distance:
                shortest_distance = distance
                best_paths = []
                best_paths.append(path)
                final_x, final_y = x, y
            elif distance == shortest_distance:
                best_paths.append(path)
            continue

        for dx, dy in [key for key in directions_dict]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                visited[nx][ny] = True
                # print((nx,ny,distance+1,path + directions_dict[(dx,dy)]))
                queue.append((nx,ny,distance+1,path + directions_dict[(dx,dy)]))

    best_paths = set(best_paths)
    best_paths = list(best_paths)
    return shortest_distance, best_paths


def robot_sequence(string,pad):

    total_distance = 0
    best_paths = []
    dictionary = None
    if pad == robot_num_pad:
        dictionary = robot_num_dict
    elif pad == robot_dir_pad:
        dictionary = robot_dir_pad_dict
    

    for index,char in enumerate(string[0:-1]):
        start, end = dictionary[char], dictionary[string[index+1]]
        current_shortest_distance, current_best_paths = find_shortest_path(pad,start,end)
        total_distance += current_shortest_distance
        best_paths.append(current_best_paths)
    combined_path = []
    first_path = ''
    for item in best_paths:
        if len(item) == 1:
            first_path += item[0]
            first_path += "A"
        elif len(item) > 1:
            combined_path.append(first_path)
            first_path = ''
            combined_path.append(item)
    if first_path:
        combined_path.append(first_path)
    return total_distance, combined_path
total_complexity = 0

for item in input_list:    
    first_robot=(robot_sequence(robot_num_pad[final_x][final_y]+item,robot_num_pad))
    current_distance, combined_path = first_robot
    print(combined_path)
    second_robot = (robot_sequence(combined_path[0],robot_dir_pad))
    current_distance2, combined_path2 = second_robot

    third_robot = (robot_sequence(combined_path2[0],robot_dir_pad))
    print(third_robot[1])
    distance = len(third_robot[1][0])
    keycode = int(item[0:3])
    total_complexity += (distance * keycode)

print(total_complexity)

# import numpy as np
from pip._vendor import requests
# import re


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

def parse_data(data):  ### creates matrix
    parsed_data = []
    rows = data.splitlines()
    for row in rows:
        parsed_data.append(list(row))
    return parsed_data

data = fetch_data('https://adventofcode.com/2024/day/16/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
maze = parse_data(data)

start_pos = (len(maze)-2, 1)
exit_pos = (1,len(maze[0])-2)

directions = {'right' : (0,1),
              'up': (-1,0),
              'left': (0,-1),
              'down' : (1,0)}

direction_to_check = {'right': ('up','down'),
                      'left': ('up','down'),
                      'up': ('right','left'),
                      'down': ('right','left')
                      }
min_points = float('inf')

def build_paths(maze):
    global exit_pos, start_pos
    
    stack = [(start_pos, [], 0, "right")]  # Stack holds (current_pos, path, points, direction)
    min_points = float('inf')  # Start with a very high value to find the minimum
    
    while stack:
        current_pos, path, current_points, current_direction = stack.pop()
        x, y = current_pos
        
        # Add the current position to the path
        new_path = path + [current_pos]
        # print(f"Checking PoS: {x}, {y}")
        
        # If the current position is the exit, update the minimum points
        if current_pos == exit_pos:
            min_points = min(min_points, current_points)
            print(f"New Minimum Points: {min_points}")
            continue
        
        for direction in ['right', 'left', 'up', 'down']:
            nx, ny = x + directions[direction][0], y + directions[direction][1]
            # print(f"Checking to {direction}, {nx}, {ny}")
            
            if (nx, ny) in new_path:
                # print(f"Already in path, continuing")
                continue
            elif maze[nx][ny] != '#':  # Valid move
                # print(f"Able to move, moving")
                
                # Calculate points for moving to the new position
                new_points = current_points + 1  # Point for moving
                # print(f"Current direction: {current_direction}, new direction: {direction}")
                
                if direction != current_direction:
                    if direction in direction_to_check[current_direction]:  # One rotation
                        # print(f"Adding points for one rotation")
                        new_points += 1000
                    else:  # Two rotations
                        # print(f"Adding points for two rotations")
                        new_points += 2000
                
                # Add the new state to the stack
                stack.append(((nx, ny), new_path, new_points, direction))
    
    # Return the minimum points found, or -1 if no path is found
    return min_points if min_points != float('inf') else -1

print(build_paths(maze))
# if __name__ == "__main__":
#     data = fetch_data('https://adventofcode.com/2024/day/16/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
#     parsed_data = parse_data(data)
#     print("\n".join("".join(map(str, row)) for row in parsed_data))
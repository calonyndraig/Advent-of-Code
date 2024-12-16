import heapq
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

"""Trying BFS with help from ChatGPT"""

def build_paths(maze):
    global exit_pos, start_pos

    pq = [(0,start_pos,[],"right")] # items include current points, current position, path, and current direction
    visited = {} # will track with (pos, direction): best_score
    directions_list = ['right','left','up','down']
    min_points = float('inf')
    best_paths = []

    while pq:  # while there is still something to check
        current_points,current_pos,path,current_direction = heapq.heappop(pq)
        x,y = current_pos

        # if (current_pos, current_direction) in visited:
        #     if visited[(current_pos, current_direction)] <= current_points:  # if we've already been here but with fewer current points
        #         continue
        visited[(current_pos,current_direction)] = current_points

        new_path = path + [current_pos] # adding the new position to the path we are currently treading

        if current_pos == exit_pos:
            if current_points < min_points:
                min_points = current_points
                best_paths = [new_path]
            elif current_points == min_points:
                best_paths.append(new_path)
            continue

        for direction in directions_list:
            nx,ny = x + directions[direction][0], y + directions[direction][1]

            if (nx,ny) in new_path or maze[nx][ny] == '#':
                continue

            new_points = current_points + 1 # adding because we are moving

            if direction != current_direction:
                if direction in direction_to_check[current_direction]:  # One rotation
                    new_points += 1000
                else:  
                    new_points += 2000 # two rotations
                

            heapq.heappush(pq,(new_points, (nx,ny), new_path, direction))

    unique_tiles = set()
    for path in best_paths:
        for tile in path:
            unique_tiles.add(tile)

    return min_points, best_paths, unique_tiles

min_points, best_paths, unique_tiles = build_paths(maze)

print(len(unique_tiles))


""" trying dijkstra"""

def dijkstra_min_paths(maze):
    global exit_pos, start_pos

    pq = [(0, start_pos,"right")] #current points, current location, current direction
    costs = {} #minimum cost to reach each position
    paths = {} #best path to each position
    best_paths = []
    min_points = float('inf')

    costs[start_pos] = 0
    paths[start_pos] = [start_pos]

    while pq:
        current_points,current_pos,current_direction = heapq.heappop(pq)
        x,y = current_pos

        if current_pos == exit_pos and current_points > min_points: # stop if we find higher cost exit
            continue

        if current_pos == exit_pos and current_points == min_points: # adding path to exit with same cost
            best_paths.append(paths[current_pos])
            continue

        if current_pos == exit_pos and current_points < min_points: #found better path, update min points and reset paths
            min_points = current_points
            best_paths = [paths[current_pos]]
            continue

        for direction in ['right', 'left', 'up', 'down']:
            nx, ny = x + directions[direction][0], y + directions[direction][1]
            neighbor = (nx, ny)

            if maze[nx][ny] == '#':
                continue    # skip walls
            
            new_points = current_points + 1:
            
            if direction != current_direction:
                if direction in direction_to_check[current_direction]:
                    new_points += 1000  # One rotation
                else:
                    new_points += 2000  # Two rotations            

            if neighbor not in costs or new_points < costs[neighbor]:
                costs[neighbor] = new_points
                heapq.heappush(pq,(newpoints,neighbor,direction))
                paths[neighbor] = paths[current_pos] + [neighbor]

    unique_tiles = set()
    for path in best_paths:
        unique_tiles.update(path)

    return min_points, best_paths, unique_tiles
            
min_points, best_paths, unique_tiles = dijkstra_min_paths(maze)

print(min_points, len(best_paths), len(unique_tiles))


""" previous attempt"""


# direction_to_check = {'right': ('up','down'),
#                       'left': ('up','down'),
#                       'up': ('right','left'),
#                       'down': ('right','left')
#                       }
# min_points = float('inf')

# def build_paths(maze):
#     global exit_pos, start_pos
    
#     stack = [(start_pos, [], 0, "right")]  # Stack holds (current_pos, path, points, direction)
#     min_points = float('inf')  # Start with a very high value to find the minimum
    
#     while stack:
#         current_pos, path, current_points, current_direction = stack.pop()
#         x, y = current_pos
        
#         # Add the current position to the path
#         new_path = path + [current_pos]
#         # print(f"Checking PoS: {x}, {y}")
        
#         # If the current position is the exit, update the minimum points
#         if current_pos == exit_pos:
#             min_points = min(min_points, current_points)
#             print(f"New Minimum Points: {min_points}")
#             continue
        
#         for direction in ['right', 'left', 'up', 'down']:
#             nx, ny = x + directions[direction][0], y + directions[direction][1]
#             # print(f"Checking to {direction}, {nx}, {ny}")
            
#             if (nx, ny) in new_path:
#                 # print(f"Already in path, continuing")
#                 continue
#             elif maze[nx][ny] != '#':  # Valid move
#                 # print(f"Able to move, moving")
                
#                 # Calculate points for moving to the new position
#                 new_points = current_points + 1  # Point for moving
#                 # print(f"Current direction: {current_direction}, new direction: {direction}")
                
#                 if direction != current_direction:
#                     if direction in direction_to_check[current_direction]:  # One rotation
#                         # print(f"Adding points for one rotation")
#                         new_points += 1000
#                     else:  # Two rotations
#                         # print(f"Adding points for two rotations")
#                         new_points += 2000
                
#                 # Add the new state to the stack
#                 stack.append(((nx, ny), new_path, new_points, direction))
    
#     # Return the minimum points found, or -1 if no path is found
#     return min_points if min_points != float('inf') else -1

# print(build_paths(maze))
# # if __name__ == "__main__":
# #     data = fetch_data('https://adventofcode.com/2024/day/16/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
# #     parsed_data = parse_data(data)
# #     print("\n".join("".join(map(str, row)) for row in parsed_data))





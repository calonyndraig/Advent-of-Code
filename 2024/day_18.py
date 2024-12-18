import logging
import time
from pip._vendor import requests
from heapq import heappop,heappush


# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")






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

data = fetch_data('https://adventofcode.com/2024/day/18/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
coords = []
for line in data.splitlines():
    coord = line.split(',')
    coords.append(coord)

memory_space = [['.' for x in range(71)] for y in range(71)]

for index, c in enumerate(coords):
    new_coord = int(c[0]), int(c[1])
    x, y = new_coord
    if index < 1024 - 1:
        memory_space[x][y] = "#"

memory_space[0][0] = "S"
memory_space[70][70] = "E"



memory_space_image = "\n".join(["".join(row) for row in memory_space])
# logging.debug("\n" + memory_space_image)
with open("memory_space.txt", "w") as file:
    file.write(memory_space_image)

# logging.debug(memory_space)

start,end = (0,0), (70,70)

dirs = {0:"R",1:"L",2:"U",3:"D"}

directions = {0 : (0,1),
              1 : (0,-1),
              2 : (-1,0),
              3 : (1,0)
              }

# def check_possibility(memory_space,start,end):
#     visited = {}  # will be (position, direction) : steps to get there
#     # min_steps = float('inf')
#     # paths = []
#     checking = [(0,start,-1,[start])]
#     # path = [start]
#     while checking:
#         current_steps, current_pos, dir_index, path = heappop(checking)
#         # print(current_pos)
#         # logging.debug(f"NEW CHECK STARTING")
#         # logging.debug(f"Steps Taken: {current_steps}")
#         # logging.debug(f"Current Location: {current_pos}")
#         # logging.debug(f"Current Direction: {direction}")
#         if current_pos == end:
#             return True
#         # if current_steps >= min_steps:
#             # logging.debug("Current steps exceeds current minimum, breaking...")
#             continue
#         # if (current_pos, direction) in visited and visited[(current_pos, direction)] <= current_steps:
#             # logging.debug("Been here before with fewer steps, moving on...")
#             # continue
#         # visited[(current_pos, direction)] = current_steps
#         # if current_pos == end:
#         #     paths.append(path)
#         #     print(path)
#         #     # logging.debug(f"Made it to the end with {current_steps} steps!")
#         #     if current_steps < min_steps:
#         #         # logging.debug(f"New current minimum steps!  {current_steps}")
#         #         min_steps = current_steps

#             # continue
#         for dir_index in range(4):
#             new_x = current_pos[0] + directions[dir_index][0]
#             new_y = current_pos[1] + directions[dir_index][1]
#             # logging.debug(f"Checking new coordinates: {new_x}, {new_y}...")
#             # logging.debug(f"Current path: {path}")
#             if 0 <= new_x < len(memory_space) and 0 <= new_y < len(memory_space) and memory_space[new_x][new_y] != "#":
#                 # logging.debug(f"We can move forward!")
#                 new_pos = (new_x, new_y)
#                 if (new_pos,dir_index) not in visited or visited[(new_pos,dir_index)] > current_steps +1:
#                     # logging.debug(f"Pushing forwarded to heap: ({current_steps+1},({new_pos}), {dir_index})")
#                     visited[(new_pos,dir_index)] = current_steps + 1
#                     heappush(checking,(current_steps+1, new_pos, dir_index,path + [new_pos]))
#                     # print(path)
#                     # logging.debug(checking)
#         return False

def is_solvable(memory_space, start, end):
    """Check if the maze is solvable from start to end."""
    visited = {}
    checking = [(0, start, -1, [start])]  # Heap for the priority queue
    
    while checking:
        current_steps, current_pos, dir_index, path = heappop(checking)
        if current_pos == end:
            return True  # Found a solution

        for dir_index in range(4):
            new_x = current_pos[0] + directions[dir_index][0]
            new_y = current_pos[1] + directions[dir_index][1]

            if 0 <= new_x < len(memory_space) and 0 <= new_y < len(memory_space[0]) and memory_space[new_x][new_y] != "#":
                new_pos = (new_x, new_y)
                if (new_pos, dir_index) not in visited or visited[(new_pos, dir_index)] > current_steps + 1:
                    visited[(new_pos, dir_index)] = current_steps + 1
                    heappush(checking, (current_steps + 1, new_pos, dir_index, path + [new_pos]))

    return False  # No path found


unsolveable_coord = None

for index in range(1024-1,len(coords)):
    new_coord = (int(coords[index][0]), int(coords[index][1]))
    x,y = new_coord
    memory_space[x][y] = "#"

    if not is_solvable(memory_space, start, end):
        unsolvable_coord = new_coord
        break 
    
print(unsolvable_coord)



# correct_coords = [-1,-1]

# for index, c in enumerate(coords[1024:]):
#     new_coord = int(c[0]), int(c[1])
#     x, y = new_coord
#     memory_space[x][y] = "#"
#     min_steps = float('inf')
#     push_it(memory_space)
#     print(min_steps)    
#     if type(min_steps) != int:
#         correct_coords = [x,y]
#         break

# print(correct_coords)




        



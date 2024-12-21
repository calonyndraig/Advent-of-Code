import copy
from threading import Event
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor, as_completed
from heapq import heappop, heappush
from math import inf
from pip._vendor import requests

stop_event = Event()

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

data = fetch_data('https://adventofcode.com/2024/day/20/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
maze = data.splitlines()

dirs = {0:"R",1:"L",2:"U",3:"D"}
reverse_dirs = {v: k for k, v in dirs.items()}  # Reverse the mapping of dirs


directions = {0 : tuple((0,1)),
              1 : tuple((0,-1)),
              2 : tuple((-1,0)),
              3 : tuple((1,0))
              }

def find_points(maze,start=None,end=None): # initializes start and end
    for i, row in enumerate(maze):
        if start and end:
            break
        for j, item in enumerate(row):
            if item == "S":
                start = tuple((i,j))
            elif item == "E":
                end = tuple((i,j))
            if start and end:
                break
        if start and end:
            break
    return start, end

start,end = find_points(maze)

def find_obstacles(maze):  # retuns list of coordinates that have obstacles
    walls_coords = set()
    for i in range(1,len(maze)-1):
        for j in range(1,len(maze[0])-1):
            if maze[i][j] == "#":
                walls_coords.add(((i,j)))
                for dx, dy in directions.values():
                    new_i, new_j = i + dx, j + dy
                    if 0 <= new_i < len(maze[0]) - 1 and 0 <= new_j < len(maze) - 1 and maze[new_i][new_j] == "#":
                        walls_coords.add(((i,j),(new_i,new_j)))
    return walls_coords

cheat_list = find_obstacles(maze)

def run_maze(maze, start, end, cheats=False,current_goal=inf):
    visited = dict()
    path = tuple()
    checking = [(0,start,0,path)]
    seconds_taken = inf

    while checking:
        current_seconds, pos, d, path = heappop(checking)
        # print(f"Popping from heap: {current_seconds}, {pos}, {d}, {path}")
        if cheats and current_seconds > current_goal:
            continue
        if current_seconds > seconds_taken:
            break
        if (pos, d) in visited and visited[(pos, d)] <= current_seconds:
            continue
        visited[(pos, d)] = current_seconds
        if pos == end:
            seconds_taken = current_seconds
            return current_seconds, path
        for i, (dx,dy) in directions.items():
            new_x,new_y = pos[0] + dx, pos[1] + dy
            if maze[new_x][new_y] != "#":
                newpos = tuple((new_x, new_y))
                # print("Pushing to heap: f{current_seconds+1}, {newpos}, {i}, {path + dirs[i]}")
                heappush(checking, (current_seconds+1, newpos, i, path + (pos,)))

    return seconds_taken, path


without_cheats, path = run_maze(maze,start,end)

with_cheats_goal = without_cheats - 100

beats_goal = 0 
test_maze = [list(row) for row in maze]
cheat_list = list(cheat_list)

# Context manager for applying and reverting cheats
@contextmanager
def apply_cheat(maze, item):
    if isinstance(item[0], int):  # Single cheat
        x, y = item
        original = maze[x][y]
        maze[x][y] = '.'
        yield
        maze[x][y] = original
    else:  # Paired cheat
        (x1, y1), (x2, y2) = item
        original1, original2 = maze[x1][y1], maze[x2][y2]
        maze[x1][y1], maze[x2][y2] = '.', '.'
        yield
        maze[x1][y1], maze[x2][y2] = original1, original2

# Function to process a batch of cheats
def process_cheat_batch(batch, maze, start, end, with_cheats_goal, batch_index, total_batches):
    local_beats_goal = 0
    print(f"Processing batch {batch_index + 1}/{total_batches}...")
    for index,item in enumerate(batch):
        print(f"Processing item {index}")
        with apply_cheat(maze, item):
            result = run_maze(maze, start, end, True, with_cheats_goal)
            if result is not None:
                local_beats_goal += 1
    return local_beats_goal

# Split cheat_list into batches
batch_size = 4  # Adjust batch size based on performance
batches = [cheat_list[i:i + batch_size] for i in range(0, len(cheat_list), batch_size)]
total_batches = len(batches)

beats_goal = 0

# Parallel processing using ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(process_cheat_batch, batch, test_maze, start, end, with_cheats_goal, idx, total_batches)
        for idx, batch in enumerate(batches)
    ]

    # Collect results as each batch completes
    for future in as_completed(futures):
        beats_goal += future.result()

print(f"Total cheats that beat the goal: {beats_goal}")
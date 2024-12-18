import heapq
from pip._vendor import requests

# def fetch_data(url,session):
#     headers = {
#     'Cookie': f'session={session}',
#         }
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         # The input data as text
#         data = response.text
#     else:
#         data = None

#     return data

# def parse_data(data):  ### creates matrix
#     parsed_data = []
#     rows = data.splitlines()
#     for row in rows:
#         parsed_data.append(list(row))
#     return parsed_data

# data = fetch_data('https://adventofcode.com/2024/day/16/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
# maze = parse_data(data)


# Read the maze input
with open('maze.txt', 'r') as f:
    maze = [line.strip() for line in f.readlines()]

# Define global start and exit positions
start_pos = (len(maze) - 2, 1)
exit_pos = (1, len(maze[0]) - 2)

directions = {'right': (0, 1), 'up': (-1, 0), 'left': (0, -1), 'down': (1, 0)}
direction_to_check = {'right': ('up', 'down'),
                      'left': ('up', 'down'),
                      'up': ('right', 'left'),
                      'down': ('right', 'left')}

def dijkstra_min_paths(maze):
    global exit_pos, start_pos

    pq = [(0, start_pos, "right")]
    costs = {}
    paths = {}
    min_points = float('inf')
    best_paths = []

    costs[start_pos] = 0
    paths[start_pos] = [[start_pos]]

    while pq:
        current_points, current_pos, current_direction = heapq.heappop(pq)
        x, y = current_pos

        # If we've exceeded the known minimum points, skip processing
        if current_pos == exit_pos and current_points > min_points:
            continue

        # If we've reached the exit, handle best paths
        if current_pos == exit_pos:
            if current_points < min_points:
                min_points = current_points
                best_paths = paths[current_pos]
            elif current_points == min_points:
                best_paths.extend(paths[current_pos])
            continue

        for direction in ['right', 'left', 'up', 'down']:
            nx, ny = x + directions[direction][0], y + directions[direction][1]
            neighbor = (nx, ny)

            if maze[nx][ny] == '#':
                continue

            new_points = current_points + 1
            if direction != current_direction:
                if direction in direction_to_check[current_direction]:
                    new_points += 1000
                else:
                    new_points += 2000

            # Update costs and paths
            if neighbor not in costs or new_points < costs[neighbor]:
                costs[neighbor] = new_points
                heapq.heappush(pq, (new_points, neighbor, direction))
                paths[neighbor] = [path + [neighbor] for path in paths[current_pos]]
            elif new_points == costs[neighbor]:
                paths[neighbor].extend(path + [neighbor] for path in paths[current_pos])

    # Collect unique tiles from all best paths
    unique_tiles = set()
    for path in best_paths:
        unique_tiles.update(path)

    return min_points, best_paths, unique_tiles

min_points, best_paths, unique_tiles = dijkstra_min_paths(maze)
print(f"Minimum Points: {min_points}")
print(f"Number of Best Paths: {len(best_paths)}")
print(f"Number of Unique Tiles: {len(unique_tiles)}")

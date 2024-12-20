from pip._vendor import requests

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


def find_points(maze,start=None,end=None): # initializes start and end
    for i, row in enumerate(maze):
        for j, item in enumerate(row):
            if not start:
                if item == "S":
                    start = tuple((i,j))
            if not end:
                if item == "E":
                    end = tuple((i,j))
            if start and end:
                break
        if start and end:
            break
    return start, end

start,end = find_points(maze)

def find_obstacles(maze):  # retuns list of coordinates that have obstacles
    walls_coords = []
    for i in range(1,len(maze)-1):
        for j in range(1,len(maze[0])-1):
            if maze[i][j] == "#":
                walls_coords.append((i,j))
    return walls_coords

"""def legal_cheats(maze,wall_coords)"""  # maybe modify find_obstacles to do this in a single step? 
# if wall has another wall directly next to it, you can use both; otherwise use only one.
# make cheat list

dirs = {0:"R",1:"L",2:"U",3:"D"}

directions = {0 : (0,1),
              1 : (0,-1),
              2 : (-1,0),
              3 : (1,0)
              }

""" Use modification of day 16 to run maze, get quickest path"""

""" Use modification of maze to get quickest path with up to two obstacles removed"""

"""need to calculate difference in length of path from no-cheat path to the cheat path"""

"""if difference is greater than 100, add cheat to list"""
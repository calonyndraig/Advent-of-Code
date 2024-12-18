import logging
# import json
# import numpy as np
from pip._vendor import requests
# import re

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler("output.txt", mode='a'),
        logging.StreamHandler()
    ]
)



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
        row = list(row)
        for index,item in enumerate(row):
            row[index] = int(item)
        parsed_data.append(row)
    return parsed_data

trail_count = 0

trail_dict = {}

def build_trailheads(current_num,coord,data,visited,startcoord):
    logging.info(f"Checking {current_num}, {coord}...")
    global trail_count
    global trail_dict
    
    if coord in visited:
        logging.info("Coordinate previously visited, ending loop...")
        return
    visited.add(coord)

    x, y = coord

    if current_num == 9:
        trail_count += 1
        if coord not in trail_dict[startcoord]:
            trail_dict[startcoord].append(coord)

        logging.info(f"Increased trail_count...{trail_count}")
    elif current_num < 9:
        if x < len(data)-1 and (x+1,y) not in visited:
            next_coords = (x+1,y)
            if check_next(current_num+1,next_coords,data):                
                build_trailheads(current_num+1,next_coords,data,visited.copy(),startcoord)
        if x > 0 and (x-1,y) not in visited:
            next_coords = (x-1,y)
            if check_next(current_num+1,next_coords,data):
                build_trailheads(current_num+1,next_coords,data,visited.copy(),startcoord)
        if y < len(data[0])-1 and (x,y+1) not in visited:
            next_coords = (x, y+1)
            if check_next(current_num+1,next_coords,data):
                build_trailheads(current_num+1,next_coords,data,visited.copy(),startcoord)
        if y > 0 and (x,y-1) not in visited:
            next_coords = (x, y-1)
            if check_next(current_num+1,next_coords,data):
                build_trailheads(current_num+1,next_coords,data,visited.copy(),startcoord)


def check_next(current_num, coord, data):
    x,y = coord
    return data[x][y] == current_num


def iterate_map(data):
    global trail_count
    # global score_sum
    global trail_dict
    visited = set()
    for row_num, row in enumerate(data):
        for col_num, item in enumerate(row):
            if item == 0 and (row_num, col_num) not in visited:
                coord = (row_num,col_num)
                startcoord = coord
                if coord not in trail_dict:
                    trail_dict[coord] = []
                build_trailheads(0,coord,data,visited.copy(),startcoord)


    scores = [len(x) for x in trail_dict.values()]
    score_sum = 0
    for i in scores:
        score_sum += i

    return score_sum


if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/10/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    parsed_data = parse_data(data)
    trail_scores = iterate_map(parsed_data)
    print(trail_scores)
    
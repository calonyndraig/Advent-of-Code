# import numpy as np
from pip._vendor import requests
# import re
import json

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

def build_trailheads(current_num,coord,data):
    print(f"Checking {current_num}, {coord}...")
    global trail_count
    if current_num == 9:
        trail_count +=1
        print(f"Increased trail_count...{trail_count}")
    elif current_num < 9:
        x,y = coord
        if x < len(data)-1:
            next_coords = x+1,y
            continue_check = check_next(current_num+1,next_coords,data)
            if continue_check:
                build_trailheads(current_num+1,next_coords,data)
        if x > 0:
            next_coords = x-1,y
            continue_check = check_next(current_num+1,next_coords,data)
            if continue_check:
                build_trailheads(current_num+1,next_coords,data)
        if y < len(data[0])-1:
            next_coords = x, y+1
            continue_check = check_next(current_num+1,next_coords,data)
            if continue_check:
                build_trailheads(current_num+1,next_coords,data)
        if y > 0:
            next_coords = x, y-1
            continue_check = check_next(current_num+1,next_coords,data)
            if continue_check:
                build_trailheads(current_num+1,next_coords,data)
    
def check_next(current_num, coord, data):
    x,y = coord
    if data[x][y] == current_num:
        return True
    else:
        return False  

def iterate_map(data):
    global trail_count
    for row_num, row in enumerate(data):
        for col_num, item in enumerate(row):
            if item == 0:
                coord = row_num,col_num
                build_trailheads(0,coord,data)
            
    return trail_count


if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/10/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    parsed_data = parse_data(data)
    trail_count = iterate_map(parsed_data)
    print(trail_count)
    
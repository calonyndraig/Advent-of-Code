import json
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

def create_matrix(data):
    matrix = []
    rows = data.splitlines()
    for row in rows:
        matrix.append(list(row))
    matrix_limits = (len(matrix)-1, len(matrix[0])-1)
    
    return matrix, matrix_limits

def build_node_dict(matrix,matrix_limits):
    node_dict ={}
    for row_num, row in enumerate(matrix):
        for col_num, char in enumerate(row):
            if char != ".":
                if char not in node_dict.keys():
                    node_dict[char] = [(row_num, col_num)]
                else:
                    node_dict[char].append((row_num, col_num))
    return node_dict,matrix_limits

def build_antinode_list(node_dict,matrix_limits):
    antinodes_list = []
    for char in node_dict:
        if len(node_dict[char]) > 1:
            for coord in node_dict[char]:
                antinodes_list.append(coord)
        for i, coord1 in enumerate(node_dict[char]):
            x,y = coord1
            for coord2 in node_dict[char][i+1:]:
                x1,y1 = coord2
                multiplier = 2
                newcoord1 = (multiplier*x - (multiplier-1)*x1, multiplier*y-(multiplier-1)*y1)
                while 0 <= newcoord1[0] and newcoord1[0] <= matrix_limits[0] and 0 <= newcoord1[1] and newcoord1[1] <= matrix_limits[1]:
                    antinodes_list.append(newcoord1)
                    multiplier += 1
                    newcoord1 = (multiplier*x - (multiplier-1)*x1, multiplier*y-(multiplier-1)*y1)
                multiplier = 2
                newcoord2 = (multiplier*x1 - (multiplier-1)*x, multiplier*y1 - (multiplier-1)*y)
                while 0 <= newcoord2[0] and newcoord2[0] <= matrix_limits[0] and 0 <= newcoord2[1] and newcoord2[1] <= matrix_limits[1]:
                    antinodes_list.append(newcoord2)
                    multiplier += 1
                    newcoord2 = (multiplier*x1 - (multiplier-1)*x, multiplier*y1 - (multiplier-1)*y)

    return antinodes_list


if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/8/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    matrix,matrix_limits = create_matrix(data)
    node_dict,matrix_limits = build_node_dict(matrix,matrix_limits)
    antinodes_list = build_antinode_list(node_dict,matrix_limits)
    print(matrix_limits)
    print(len(set(antinodes_list)))
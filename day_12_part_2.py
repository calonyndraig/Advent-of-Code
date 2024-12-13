import logging
import time
import numpy as np
from pip._vendor import requests
# import re

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler("output.txt", mode='w'),  # Log to file
        logging.StreamHandler()  # Log to console
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
        parsed_data.append(list(row))
    return parsed_data


# perimeters_dict = {}
# crop_locations_dict = {}

# # def identify_crop_locations(item,row_num,col_num):
    


# def perimeters(matrix,garden_height,garden_width):
#     global crop_locations_dict
#     for crop_type in crop_locations_dict:
#         for start_coord in crop_locations_dict[crop_type]:
#             if start_coord not in perimeters_dict:
#                 area = 1
#                 perimeters_dict[start_coord] = [area,0] # will hold area and perimeter
#             for coord in crop_locations_dict[crop_type][start_coord]:
#                 row_num, col_num = coord
#                 perimeters_dict[start_coord][0] += 1
#                 if row_num == 0:
#                     perimeters_dict[start_coord][1] += 1
#                 if row_num > 0 and matrix[row_num-1][col_num] != crop_type:
#                     perimeters_dict[start_coord][1] += 1
#                 if row_num == garden_height-1:
#                     perimeters_dict[start_coord][1] += 1
#                 if row_num < garden_height-1 and matrix[row_num + 1][col_num] != crop_type:
#                     perimeters_dict[start_coord][1] += 1
#                 if col_num == 0:
#                     perimeters_dict[start_coord][1] += 1 
#                 if col_num > 0 and matrix[row_num][col_num-1] != crop_type:
#                     perimeters_dict[start_coord][1] += 1
#                 if col_num == garden_width - 1:
#                     perimeters_dict[start_coord][1] += 1
#                 if col_num < garden_width-1 and matrix[row_num][col_num +1] != crop_type:
#                     perimeters_dict[start_coord][1] += 1
#     return

# def check_group(item,coord):
#     global crop_locations_dict
#     for start_coord in crop_locations_dict[item].keys():
#         for comparison_coord in crop_locations_dict[item][start_coord]:
#             if coord[0] == comparison_coord[0] and abs(coord[1] - comparison_coord[1]) == 1: # if to the immediate right or left of a previously identified coordinate
#                 crop_locations_dict[item][start_coord].append(coord)
#                 return
#             elif coord[1] == comparison_coord[1] and abs(coord[0] - comparison_coord[0]) == 1: # if to the immediate top or bottom of a previously identified coordinate
#                 crop_locations_dict[item][start_coord].append(coord)
#                 return
#             else:
#                 crop_locations_dict[item][coord] = [coord]
#                 return
#     return




# def check_plots(matrix):
#     global crop_locations_dict
#     for row_num, row in enumerate(matrix):
#         for col_num, item in enumerate(row):
#             coord = (row_num, col_num)
#             if item not in crop_locations_dict:
#                 crop_locations_dict[item] = {coord: [coord]} #subscripted for the first identified coordinate in a group
#                 logging.info(f"New Area Start at {coord}")
#             else:
#                 check_group(item,coord)

#     return

# def calculate_fence_price(data_dictionary):
#     total_fences = 0
#     for item in data_dictionary.values():
#         total_fences += item[0] * item[1]
    
#     return total_fences




"""
grouped_list = list of all coords assigned to a group

group_assignments = dictionary with lists of groupings?

"""
grouped_list = set()
final_groups = {}
edges_dict = {}


def check_neighbors(matrix,coords,item,temp_group):
    global grouped_list
    global edges_dict
    if coords in grouped_list:
        return
    coord_edges = 0    
    row_num, col_num = coords
    grouped_list.add(coords)
   

    if row_num == 0:
        coord_edges += 1
    if col_num == 0:
        coord_edges += 1
    if row_num == len(matrix) - 1:
        coord_edges += 1
    if col_num == len(matrix[0]) -1:
        coord_edges += 1

    if row_num < len(matrix)-1:
        if (row_num + 1, col_num) not in temp_group and matrix[row_num+1][col_num] == item:
            new_coords = (row_num + 1, col_num)
            temp_group.append(new_coords)
            temp_group = check_neighbors(matrix,new_coords,item,temp_group)
        elif matrix[row_num+1][col_num] != item:
            coord_edges += 1
    if row_num > 0:
        if (row_num - 1, col_num) not in temp_group and matrix[row_num-1][col_num] == item:
            new_coords = (row_num - 1, col_num)
            temp_group.append(new_coords)
            temp_group = check_neighbors(matrix,new_coords,item,temp_group)
        elif matrix[row_num-1][col_num] != item:
            coord_edges += 1
    if col_num < len(matrix[0]) - 1:
        if (row_num, col_num+1) not in temp_group and matrix[row_num][col_num+1] == item:
            new_coords = (row_num, col_num+1)
            temp_group.append(new_coords)
            temp_group = check_neighbors(matrix,new_coords,item,temp_group)
        elif matrix[row_num][col_num+1] != item:
            coord_edges += 1
    if col_num > 0:
        if (row_num, col_num-1) not in temp_group and matrix[row_num][col_num-1] == item:
            new_coords = (row_num, col_num-1)
            temp_group.append(new_coords)
            temp_group = check_neighbors(matrix,new_coords,item,temp_group)
        elif matrix[row_num][col_num-1] != item:
            coord_edges += 1
    
    edges_dict[coords] = coord_edges
    return temp_group



def build_area(matrix):
    
    global grouped_list
    global final_groups
    total_cost = 0
    
    while len(grouped_list) <= (len(matrix) * len(matrix[0])):  # continues
        
        for row_num, row in enumerate(matrix):
            for col_num, item in enumerate(row):
                coords = (row_num,col_num)
                if coords in grouped_list:
                    continue
                else:
                    temp_group = check_neighbors(matrix,coords,item,[(coords)])
                    print(temp_group)
                    # time.sleep(0.5)
                    area_perimeter = build_final_dict(temp_group)
                    print(area_perimeter)
                    # time.sleep(0.5)
                    total_cost += area_perimeter[0] * area_perimeter[1]
                    print(total_cost)
                    # time.sleep(0.5)


    
    return total_cost
                    
    
def find_corners(temp_group,matrix):
    corner_count = 0
    min_x = min([x[0] for x in temp_group])
    min_y = min([x[1] for x in temp_group])
    max_x = max([x[0] for x in temp_group])
    max_y = max([x[1] for x in temp_group])

    nump_garden = np.array(matrix)
    add_row = np.array([0 for x in range(len(nump_garden[0])-1)])
    nump_garden = np.vstack(add_top,nump_garden,add_top)
    add_column = np.array([[0] for x in range(len(nump_garden-1))])
    nump_garden = np.hstack(add_column,nump_garden,add_column) 
        
    return nump_garden    
    # sub_matrix = 
    # for row_num in range(min_x,max_x):
    #     for col_num in range(min_y,max_y):
            
                



def build_final_dict(temp_group):
    global edges_dict
    global final_groups
    sorted_temp_group = sorted(temp_group)
    total_area = len(sorted_temp_group)
    total_perimeter = 0
    for item in sorted_temp_group:
        total_perimeter += edges_dict[item]
    final_groups[sorted_temp_group[0]] = (total_area, total_perimeter)
    return final_groups[sorted_temp_group[0]]


# def final_calculation():
#     global final_groups
#     total_cost = 0
#     areas_perimeters = [x for x in final_groups.values()]
#     print(areas_perimeters)
#         # total_cost += value[0] * value[1]

#     return total_cost
    
    
data = fetch_data('https://adventofcode.com/2024/day/12/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
parsed_data = parse_data(data)
# build_area(parsed_data)
find_corners(parsed_data)
    
    





                
     
# if __name__ == "__main__":
#     data = fetch_data('https://adventofcode.com/2024/day/12/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
#     parsed_data = parse_data(data)
#     build_area(parsed_data)
#     final_calculation()
#     # initial_coords = (0,0)
#     # grouped_area = (check_neighbors(parsed_data,initial_coords,parsed_data[0][0],[initial_coords]))
#     # sorted_group = sorted(grouped_area)
#     # final_dict = build_final_dict(grouped_area,edges_dict)
#     # print(final_dict)
    
    
    

    


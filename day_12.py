# import defaultdict
# import logging
import time
# # import numpy as np
from pip._vendor import requests
# # import re

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(message)s',
#     handlers=[
#         logging.FileHandler("output.txt", mode='w'),  # Log to file
#         logging.StreamHandler()  # Log to console
#     ]
# )


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

# def parse_data(data):  ### creates matrix
#     parsed_data = []
#     rows = data.splitlines()
#     for row in rows:
#         parsed_data.append(list(row))
#     return parsed_data


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
# grouped_list = set()
# final_groups = {}
# edges_dict = {}
# corner_dict = {}
# corners_dict = {}

# def check_neighbors(matrix,coords,item,temp_group):
#     global grouped_list
#     global edges_dict
#     global corners_dict

#     if coords in grouped_list:
#         return
#     coord_edges = 0    
#     row_num, col_num = coords
#     grouped_list.add(coords)
#     corners_dict[coords] = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False}
   

#     if row_num == 0:
#         coord_edges += 1
#     if col_num == 0:
#         coord_edges += 1
#     if row_num == len(matrix) - 1:
#         coord_edges += 1
#     if col_num == len(matrix[0]) -1:
#         coord_edges += 1

#     if row_num < len(matrix)-1:
#         if (row_num + 1, col_num) not in temp_group and matrix[row_num+1][col_num] == item: #checking down
#             new_coords = (row_num + 1, col_num)
#             temp_group.append(new_coords)
#             temp_group = check_neighbors(matrix,new_coords,item,temp_group)
#         elif matrix[row_num+1][col_num] != item:
#             coord_edges += 1
#             corners_dict[coords][7] = True 
#     if row_num > 0:
#         if (row_num - 1, col_num) not in temp_group and matrix[row_num-1][col_num] == item: #checking up
#             new_coords = (row_num - 1, col_num)
#             temp_group.append(new_coords)
#             temp_group = check_neighbors(matrix,new_coords,item,temp_group)
#         elif matrix[row_num-1][col_num] != item:
#             coord_edges += 1
#             corners_dict[coords][3] = True
#     if col_num < len(matrix[0]) - 1: #checking right
#         if (row_num, col_num+1) not in temp_group and matrix[row_num][col_num+1] == item:
#             new_coords = (row_num, col_num+1)
#             temp_group.append(new_coords)
#             temp_group = check_neighbors(matrix,new_coords,item,temp_group)
#         elif matrix[row_num][col_num+1] != item:
#             coord_edges += 1
#             corners_dict[coords][5] = True
#     if col_num > 0: # checking left
#         if (row_num, col_num-1) not in temp_group and matrix[row_num][col_num-1] == item:
#             new_coords = (row_num, col_num-1)
#             temp_group.append(new_coords)
#             temp_group = check_neighbors(matrix,new_coords,item,temp_group)
#         elif matrix[row_num][col_num-1] != item:
#             coord_edges += 1
    
    
#     edges_dict[coords] = coord_edges
#     return temp_group



# def build_area(matrix):
    
#     global grouped_list
#     global final_groups
#     total_cost = 0
    
#     while len(grouped_list) <= (len(matrix) * len(matrix[0])):  # continues
        
#         for row_num, row in enumerate(matrix):
#             for col_num, item in enumerate(row):
#                 coords = (row_num,col_num)
#                 if coords in grouped_list:
#                     continue
#                 else:
#                     temp_group = check_neighbors(matrix,coords,item,[(coords)])
#                     # print(sorted(temp_group))
#                     # time.sleep(0.5)
#                     area_corners = build_final_dict(temp_group,matrix)
#                     # if area_corners[2] <= 25:
#                     #     print(area_corners)
#                     # #     time.sleep(0.5)
#                     # total_cost += area_corners[0] * area_corners[2]
#                     # print(total_cost)
#                     # time.sleep(0.5)


    
#     return total_cost
                    
    

    



# def build_final_dict(temp_group, matrix):
#     global edges_dict
#     global final_groups
#     global corners_dict
#     sorted_temp_group = sorted(temp_group)

#     edges_only = [x for x in sorted_temp_group if edges_dict[x] != 0]
    
#     sides = defaultdict(list)
#     for edge in edges_only:
#         (x1,y1),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     # total_area = len(sorted_temp_group)
#     # total_perimeter = 0
#     # corner_count = 0

#     # # Directions for diagonal and corresponding orthogonal neighbors
#     # diagonal_checks = {
#     #     (-1, -1): [(-1, 0), (0, -1)],  # Top-left
#     #     (-1, 1): [(-1, 0), (0, 1)],   # Top-right
#     #     (1, -1): [(1, 0), (0, -1)],   # Bottom-left
#     #     (1, 1): [(1, 0), (0, 1)]      # Bottom-right
#     # }

#     # # Initialize corners_dict for this group
    

#     # for item in sorted_temp_group:
#     #     corners_dict = {item: {i: False for i in range(1, 9)} for item in temp_group}
#     #     total_perimeter += edges_dict[item]
#     #     row_num, col_num = item

#     #     # Check diagonal neighbors for corners
#     #     for (dr, dc), neighbors in diagonal_checks.items():
#     #         diag_r, diag_c = row_num + dr, col_num + dc

#     #         # Ensure diagonal neighbor is within bounds and not part of the group
#     #         if 0 <= diag_r < len(matrix) and 0 <= diag_c < len(matrix[0]) and (diag_r, diag_c) not in temp_group:
#     #             # Check both corresponding orthogonal neighbors
#     #             orth1_r, orth1_c = row_num + neighbors[0][0], col_num + neighbors[0][1]
#     #             orth2_r, orth2_c = row_num + neighbors[1][0], col_num + neighbors[1][1]

#     #             if (
#     #                 (0 <= orth1_r < len(matrix) and 0 <= orth1_c < len(matrix[0]) and (orth1_r, orth1_c) not in temp_group)
#     #                 or
#     #                 (0 <= orth2_r < len(matrix) and 0 <= orth2_c < len(matrix[0]) and (orth2_r, orth2_c) not in temp_group)
#     #             ):
#     #                 # Valid corner detected
#     #                 corner_count += 1

#     # # Save group results
#     # final_groups[sorted_temp_group[0]] = (total_area, total_perimeter,corner_count)
    

#     # return final_groups[sorted_temp_group[0]]


# # def final_calculation():
# #     global final_groups
# #     total_cost = 0
# #     areas_perimeters = [x for x in final_groups.values()]
# #     print(areas_perimeters)
# #         # total_cost += value[0] * value[1]

# #     return total_cost
    
    
data = fetch_data('https://adventofcode.com/2024/day/12/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
# parsed_data = parse_data(data)
# # build_area(parsed_data)

    
    





                
     
# # if __name__ == "__main__":
# #     data = fetch_data('https://adventofcode.com/2024/day/12/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
# #     parsed_data = parse_data(data)
# #     build_area(parsed_data)
# #     final_calculation()
# #     # initial_coords = (0,0)
# #     # grouped_area = (check_neighbors(parsed_data,initial_coords,parsed_data[0][0],[initial_coords]))
# #     # sorted_group = sorted(grouped_area)
# #     # final_dict = build_final_dict(grouped_area,edges_dict)
# #     # print(final_dict)
    
    
    

    

""""chatgpt version"""
from collections import deque

# from collections import deque

def parse_map(input_map):
    return [list(row) for row in input_map.strip().splitlines()]

def find_regions(garden_map):
    rows, cols = len(garden_map), len(garden_map[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = []

    def bfs(x, y):
        plant_type = garden_map[x][y]
        queue = deque([(x, y)])
        region = set()
        boundary_edges = set()

        while queue:
            cx, cy = queue.popleft()
            if (cx, cy) in region:
                continue
            region.add((cx, cy))
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if garden_map[nx][ny] == plant_type:
                        if not visited[nx][ny]:
                            queue.append((nx, ny))
                    else:
                        # Add boundary edge
                        boundary_edges.add(((cx, cy), (cx + dx, cy + dy)))
                else:
                    # Edge to the map boundary
                    boundary_edges.add(((cx, cy), (cx + dx, cy + dy)))

        return region, boundary_edges

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region, edges = bfs(r, c)
                regions.append((region, edges))
                for cell in region:
                    visited[cell[0]][cell[1]] = True

    return regions

def count_sides(boundary_edges):
    # Track used edges to ensure distinct sides
    used_edges = set()
    sides = 0

    def trace_side(start_edge):
        stack = [start_edge]
        while stack:
            edge = stack.pop()
            if edge in used_edges:
                continue
            used_edges.add(edge)
            # Find connected edges
            for e in boundary_edges:
                if e in used_edges:
                    continue
                if e[0] == edge[1]:  # Forward connected
                    stack.append(e)
                elif e[1] == edge[1]:  # Reverse connected
                    stack.append((e[1], e[0]))

    for edge in boundary_edges:
        if edge not in used_edges:
            sides += 1
            trace_side(edge)

    return sides

def calculate_total_price(garden_map):
    regions = find_regions(garden_map)
    total_price = 0

    for region, edges in regions:
        area = len(region)
        sides = count_sides(edges)
        price = area * sides
        total_price += price

    return total_price

# Input processing
input_map = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

garden_map = parse_map(data)
total_price = calculate_total_price(garden_map)
print("Total Price:", total_price)
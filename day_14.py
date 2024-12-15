import re
import numpy as np
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
    
    data = data.splitlines()

    return data

def parse_data(data):
    robot_dict = []
    for line in data:
        nums = re.findall(r'-?\d+', line)
        # print(nums)
        if nums:
            robot_dict.append(((int(nums[0]),int(nums[1])),(int(nums[2]),int(nums[3]))))
    return robot_dict
    
"""global variables"""
# width = 101
# height = 103

# def matrix(): # be wary of the zero problem later
#     global width, height
#     bathroom_matrix = [[0 for y in range(width)] for x in range(height)]
#     np_bathroom = np.array(bathroom_matrix)
#     return np_bathroom

# def traverse_matrix(robot_dict,m):
#     final_locations = []
#     for item in robot_dict:
#         p = item
#         v = robot_dict[item]
#         final_locations.append((item,robot_travel(p,v,m)))
#     return final_locations

# def robot_travel(p,v,m):
#     global height,width
#     y, x = p
#     y_change, x_change = v

#     if m == 0:
#         return p
#     else:
#         x = (x + x_change * m) % height
#         y = (y + y_change * m) % width
#         print(f"new x, y = {x},{y}")
#         return (x,y)
    
# def draw_matrix(np_matrix,final_locations):
#     for item in final_locations:
#         x,y = item[1]
#         np_matrix[x][y] += 1
#         # print(np_matrix[x][y])
#     return np_matrix

# def quadrant_calculations(np_matrix):
#     global width
#     global height

    
#     quadrant1 = np_matrix[0:height // 2, 0:width // 2]  # Top-left
#     quadrant2 = np_matrix[height // 2 + 1:, 0:width // 2]  # Bottom-left
#     quadrant3 = np_matrix[0:height // 2, width // 2 + 1:]  # Top-right
#     quadrant4 = np_matrix[height // 2 + 1:, width // 2 + 1:]  # Bottom-right

#     q1sum = np.sum(quadrant1)
#     q2sum = np.sum(quadrant2)
#     q3sum = np.sum(quadrant3)
#     q4sum = np.sum(quadrant4)

#     total_sum = np.sum(np_matrix)

#     print(q1sum, q2sum, q3sum, q4sum, total_sum)

#     return q1sum * q2sum * q3sum * q4sum


# """
# To finish later:
# re-read instuctions for desired output
# should be ready to run for final locations

# """




# if __name__ == "__main__":
data = fetch_data('https://adventofcode.com/2024/day/14/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    
#     # data = 'p=0,4 v=3,-3 \n p=6,3 v=-1,-3 \n p=10,3 v=-1,2\np=2,0 v=2,-1\np=0,0 v=1,3\np=3,0 v=-2,-2\np=7,6 v=-1,-3\np=3,0 v=-1,-2\np=9,3 v=2,3\np=7,3 v=-1,2\np=2,4 v=2,-3\np=9,5 v=-3,-3'
#     # data = data.splitlines()
robot_dict = parse_data(data)
#     # print(robot_dict)
#     # robot_dict = {(2,4):(2,-3)}
#     # final_total = 0
#     # i = 0
#     # while final_total != 12:
#     # robot_travel((2,4),(2,-3),1)
#     new_locations = traverse_matrix(robot_dict,100)
#         # print(new_locations)
#         # # print(robot_dict)
#     bathroom_matrix = matrix()
#         # # print(bathroom_matrix.shape)
#     updated = draw_matrix(bathroom_matrix,new_locations)
#     # print(updated)
#     final_total = quadrant_calculations(updated)
#     print(final_total)
#     #     i += 1
#     # print(i)
#     # # print(updated)
#     # locations = np.where(bathroom_matrix == 1)
#     # print(list(zip(locations[0], locations[1])))
#     # final_pos = robot_travel((33, 89),(92, 70),1)
#     # print(final_pos)

tilesx = 101
tilesy = 103

safetyfactors = []
for t in range(max(tilesx, tilesy)):
    quads = [0, 0, 0, 0]
    for ((px, py), (vx, vy)) in robot_dict:
        x = (px+vx*t)%tilesx
        y = (py+vy*t)%tilesy
        if x != tilesx//2 and y != tilesy//2:
            x = x//(tilesx//2+1)
            y = y//(tilesy//2+1)
            quads[y*2+x] += 1
    safetyfactor = 1
    for quad in quads:
        safetyfactor *= quad
    safetyfactors.append((safetyfactor, t, quads))

for _, t, quads in sorted(safetyfactors)[:2]:
    if quads[0] > len(robot_dict)//4 < quads[2] or quads[1] > len(robot_dict)//4 < quads[3]:
        tx = t
    else:
        ty = t

p2 = tx+(pow(tilesx, -1, tilesy)*(ty-tx))%tilesy*tilesx # Chinese Remainder Theorem

locs = set()
for ((px, py), (vx, vy)) in robot_dict:
    x = (px+vx*p2)%tilesx
    y = (py+vy*p2)%tilesy
    locs.add((x, y))
print('\n'.join(''.join('#' if (x, y) in locs else ' ' for x in range(tilesx)) for y in range(tilesy)))

print(safetyfactors[100][0])
print(p2)
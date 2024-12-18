from pip._vendor import requests

url = 'https://adventofcode.com/2024/day/4/input'

session = "53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd"
headers = {
    'Cookie': f'session={session}',
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    # The input data as text
    data = response.text
else:
    data = None

data_lines = data.splitlines()
data_matrix = []
for line in data_lines:
    data_matrix.append(list(line))

# print(data_matrix)

# def letter_ids():
#     M_list = []
#     A_list = []
#     S_list = []
#     for row in range(len(data_matrix)):
#         for column, character in enumerate(data_matrix[row]):
#             if character == "M":
#                 M_list.append((row,column))
#             if character == "A":
#                 A_list.append((row,column))
#             if character == "S":
#                 S_list.append((row,column))

# lower_limit = len(data_matrix)-1
# right_limit = len(data_matrix[0])-1

# def find_M():
#     for row_num, row in enumerate(data_matrix):
#         for column_num, character in enumerate(row):
#             right = False
#             left = False
#             up = False
#             down = False
#             if character == "M":
#                 if column_num - 2 >= 0:
#                     left = True
#                 if column_num + 2 <= right_limit:
#                     right = True
#                 if row_num - 2 >= 0:
#                     up = True
#                 if row_num + 2 <= lower_limit:
#                     down = True
#                 m_coord = (row_num, column_num)
#                 dirs = {"up": up, "right": right, "left": left, "down": down}
#                 find_M_pair(m_coord,dirs)

# def find_M_pair(m_coord,dirs):
#     if dirs["right"]:
#         if data_matrix[m_coord[0]][m_coord[1]+2] == "M":
#             check_A(m_coord,dirs,"right")
#     if dirs["down"]:
#         if data_matrix[m_coord[0]+2][m_coord[1]] == "M":
#             check_A(m_coord,dirs,"down")

# def check_A(m_coord,dirs,direction):
#     if direction == "right":
#         if dirs["up"]:
#             if data_matrix[m_coord[0]-1][m_coord[1]+1] == "A":
#                 check_S(m_coord,"up-right")
#         if dirs["down"]:
#             if data_matrix[m_coord[0]+1][m_coord[1]+1] == "A":
#                 check_S(m_coord,"down-right")
#     if direction == "down":
#         if dirs["left"]:
#             if data_matrix[m_coord[0]+1][m_coord[1]-1] == "A":
#                 check_S(m_coord,"down-left")
#         if dirs["right"]:
#             if data_matrix[m_coord[0]+1][m_coord[1]+1] == "A":
#                 check_S(m_coord,"down-right")
    
# def check_S(m_coord,direction):
#     if direction == "up-right":
#         if data_matrix[m_coord[0]-2][m_coord[1]+2] == "S" and data_matrix[m_coord[0]-2][m_coord[1]] == "S":
#             add_coords((m_coord[0]-2,m_coord[1]))
#     if direction == "down-right":
#         if data_matrix[m_coord[0]+2][m_coord[1]] == "S" and data_matrix[m_coord[0]+2][m_coord[1]+2] == "S":
#             add_coords((m_coord[0],m_coord[1]))
#     if direction == "down-left":
#         if data_matrix[m_coord[0]+2][m_coord[1]] == "S" and data_matrix[m_coord[0]+2][m_coord[1]-2] == "S":
#             add_coords((m_coord[0],m_coord[1]-2))

# mas_coords = []

# def add_coords(coords):
#     mas_coords.append(coords)

# find_M()
# result = len(mas_coords)
# print(result)
# for coord in mas_coords:
#     print(coord)

# coords_to_check = [(137,9),(137,31),(137,137),(136,115)]
    
# coords_matrix = [[0,0,0],[0,0,0],[0,0,0]]

# for coord in coords_to_check:
#     for row_num, row in enumerate(coords_matrix):
#         for col_num, character in enumerate(coords_matrix):
#             coords_matrix[row_num][col_num] = data_matrix[coord[0]+row_num][coord[1]+col_num]
#     print(coords_matrix)

"""
Redo from Chat GPT:
"""

lower_limit = len(data_matrix) - 1
right_limit = len(data_matrix[0]) - 1

def find_M():
    for row_num, row in enumerate(data_matrix):
        for column_num, character in enumerate(row):
            if character == "M":
                m_coord = (row_num, column_num)
                # print(m_coord)
                find_pairs(m_coord)

def find_pairs(m_coord):
    row, col = m_coord

    # Directions for the other "M" in the "X"
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Right, Down, Left, Up

    for d_row, d_col in directions:
        m2_row, m2_col = row + d_row, col + d_col

        # Check if second "M" is valid
        if 0 <= m2_row <= lower_limit and 0 <= m2_col <= right_limit:
            if data_matrix[m2_row][m2_col] == "M":
                # print(m_coord, (m2_row,m2_col))
                # Check diagonals for "A" and "S"
                check_A_and_S(m_coord, (m2_row, m2_col))

def check_A_and_S(m1, m2):
    r1, c1 = m1
    r2, c2 = m2

    diag_A_coords = [  # Midpoint for "A"
    ]
    if r1 == r2:
        a_col = (c1 + c2) // 2
        a_row1 = r1 + 1
        a_row2 = r1 - 1
        # print(m1,m2,(a_row1,a_col))
        diag_A_coords.append((a_row1,a_col))
        # print(m1,m2,(a_row2,a_col))
        diag_A_coords.append((a_row2,a_col))
    
    if c1 == c2:
        a_row = (r1 + r2) // 2
        a_col1 = c1 + 1
        a_col2 = c1 - 1
        diag_A_coords.append((a_row,a_col1))
        diag_A_coords.append((a_row,a_col2))
    for coord in diag_A_coords:
        a_row,a_col = coord[0], coord[1]
        if 0 <= a_row <= lower_limit and 0 <= a_col <= right_limit:
            if data_matrix[a_row][a_col] == "A":
                # print(m1,m2,(a_row,a_col))
                # Check for "S" in corners
                check_S_corners(m1, m2, (a_row, a_col))

def check_S_corners(m1, m2, a):
    r1, c1 = m1
    r2, c2 = m2
    ar, ac = a

    # Possible "S" positions (corners)

    if r1 == r2:
        if ar > r1:
            sr = r1 + 2            
        if ar < r1:
            sr = r1 - 2
        sc1 = c1
        sc2 = c2
        s_coords = [(sr,sc1),(sr,sc2)]

    if c1 == c2:
        if ac > c1:
            sc = c1 + 2
        if ac < c1:
            sc = c1 -2
        sr1 = r1
        sr2 = r2
        s_coords = [(sr1,sc),(sr2,sc)]


    if all(0 <= sr <= lower_limit and 0 <= sc <= right_limit and data_matrix[sr][sc] == "S" for sr, sc in s_coords):
        s1= (s_coords[0][0], s_coords[0][1])
        s2 = (s_coords[1][0], s_coords[1][1])
        # print(m1,m2,a,s1,s2)
        add_coords(m1, m2, a, s1, s2)

mas_coords = []

def add_coords(m1, m2, a, s1, s2):
    full_set = [m1, m2, a, s1, s2]
    min_x = len(data_matrix[0])
    for coord in full_set:
        if coord[0] < min_x:
            min_x = coord[0]
    min_y = len(data_matrix)
    for coord in full_set:
        if coord[0] == min_x:
            if coord[1] < min_y:
                min_y = coord[1]
    min_set = (min_x,min_y)
    if min_set not in mas_coords:
        mas_coords.append(min_set)
    
    
    
    # if full_set not in mas_coords:
        # mas_coords.append(full_set)

find_M()
result1 = len(mas_coords)
set_mc = set(mas_coords)
result2 = len(set_mc)
print(result1, result2)
# for item in mas_coords:
    # print(len(item))
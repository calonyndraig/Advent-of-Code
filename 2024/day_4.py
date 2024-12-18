import requests

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


#### Part One
# upper_limit = 0
# lower_limit = len(data_matrix)-1
# left_limit = 0
# right_limit = len(data_matrix[0])-1

# upward_xmas = 0
# right_xmas = 0
# left_xmas = 0
# downward_xmas = 0
# diag_up_left = 0
# diag_up_right = 0
# diag_down_left = 0
# diag_down_right = 0


# coordinates_list = []

# for row_index, row in enumerate(data_matrix):
#     for col_index, character in enumerate(row):
#         if character == 'X':
#             char_row = row_index
#             char_col = col_index
#             if char_row - 3 >= upper_limit: # is it possible to look upwards?
#                 if data_matrix[row_index-1][col_index] == 'M': # checks for next letter
#                     if data_matrix[row_index-2][col_index] == 'A': #checks for A
#                         if data_matrix[row_index-3][col_index] == 'S':
#                             upward_xmas += 1
#                             coordinates_list.append((row_index,col_index))
                            
#             if char_row + 3 <= lower_limit: # is it possible to look downwards?
#                 if data_matrix[row_index+1][col_index] == 'M': # checks for next letter
#                     if data_matrix[row_index+2][col_index] == 'A': #checks for A
#                         if data_matrix[row_index+3][col_index] == 'S':
#                             downward_xmas += 1
#                             coordinates_list.append((row_index,col_index))
                            
#             if col_index - 3 >= left_limit: # is it possible to look right?
#                 if data_matrix[row_index][col_index-1] == 'M': # checks for next letter
#                     if data_matrix[row_index][col_index-2] == 'A': #checks for A
#                         if data_matrix[row_index][col_index-3] == 'S':
#                             right_xmas += 1
#                             coordinates_list.append((row_index,col_index))
                            
#             if col_index + 3 <= right_limit: # is it possible to look left?
#                 if data_matrix[row_index][col_index+1] == 'M': # checks for next letter
#                     if data_matrix[row_index][col_index+2] == 'A': #checks for A
#                         if data_matrix[row_index][col_index+3] == 'S':
#                             left_xmas += 1                            
#                             coordinates_list.append((row_index,col_index))
                            
#             if (char_row - 3 >= upper_limit) and (col_index - 3 >= left_limit): # is it possible to look upwards and to the left?
#                 if data_matrix[row_index-1][col_index-1] == 'M': # checks for next letter
#                     if data_matrix[row_index-2][col_index-2] == 'A': # checks for next letter
#                         if data_matrix[row_index-3][col_index-3] == 'S': # checks for next letter
#                             diag_up_left += 1
#                             coordinates_list.append((row_index,col_index))
                            
#             if (char_row - 3 >= upper_limit) and (col_index + 3 <= right_limit): # is it possible to look upwards and to the right?
#                 if data_matrix[row_index-1][col_index+1] == 'M': # checks for next letter
#                     if data_matrix[row_index-2][col_index+2] == 'A': # checks for next letter
#                         if data_matrix[row_index-3][col_index+3] == 'S': # checks for next letter
#                             diag_up_right += 1
#                             coordinates_list.append((row_index,col_index))
                            
#             if (char_row + 3 <= lower_limit) and (col_index - 3 >= left_limit): # is it possible to look down and to the left?
#                 if data_matrix[row_index+1][col_index-1] == 'M': # checks for next letter
#                     if data_matrix[row_index+2][col_index-2] == 'A': # checks for next letter
#                         if data_matrix[row_index+3][col_index-3] == 'S': # checks for next letter
#                             diag_down_left += 1
#                             coordinates_list.append((row_index,col_index))
                            
#             if (char_row + 3 <= lower_limit) and (col_index + 3 <= right_limit): # is it possible to look down and to the right?
#                 if data_matrix[row_index+1][col_index+1] == 'M': # checks for next letter
#                     if data_matrix[row_index+2][col_index+2] == 'A': # checks for next letter
#                         if data_matrix[row_index+3][col_index+3] == 'S': # checks for next letter
#                             diag_down_right += 1
#                             coordinates_list.append((row_index,col_index))
                            

# all = [upward_xmas,right_xmas,left_xmas,downward_xmas,diag_up_left,diag_up_right,diag_down_left,diag_down_right]
# # print(data_matrix[136][68],data_matrix[137][69], data_matrix[138][70], data_matrix[139][71])
# print(upward_xmas, downward_xmas,right_xmas,left_xmas,diag_up_left,diag_up_right,diag_down_left,diag_down_right)
# print(sum(all))

# coord_dict = {}


# for item in coordinates_list:
#     if item in coord_dict:
#         coord_dict[item] += 1
#     else:
#         coord_dict[item] = 1

# max_repeats = max(coord_dict.values())


# print(len(coordinates_list), max_repeats)

#### Part Two

upper_limit = 0
lower_limit = len(data_matrix)-1
left_limit = 0
right_limit = len(data_matrix[0])-1

identified_coords = {}

def find_M_Pair(row,col):
    if row + 2 <= lower_limit:
        if data_matrix[row+2][col] == "M":
            check_A(row,col,row+2,col)
    if col + 2 <= right_limit:
        if data_matrix[row][col+2] == "M":
            check_A(row,col,row,col+2)

def check_A(row1,col1,row2,col2):
    if col1 == col2:
        if data_matrix[max(row1,row2)-1][col1+1] == "A":
            check_s(row1,col1,row2,col2,max(row1,row2)-1,col1+1)
        if data_matrix[max(row1,row2)-1][col1-1] == "A":                                        
            check_s(row1,col1,row2,col2,max(row1,row2)-1,col1-1)
    if row1 == row2:
        if data_matrix[row1+1][max(col1,col2-1)] == "A":
            check_s(row1,col1,row2,col2,row1+1,max(col1,col2)-1)
        if data_matrix[row1-1][max(col1,col2-1)] == "A":
            check_s(row1,row2,col1,col2,row1-1,max(col1,col2-1))

def check_s(row1,col1,row2,col2,row_a,col_a):
    if col1 == col2:
        if col_a > col1:
            if data_matrix[row1][col1+2] == "S" and data_matrix[row2][col2+2] == "S":
                top_coord = (min(row1,row2,row_a), min(col1,col2,col_a))
                if top_coord in identified_coords:
                    identified_coords[top_coord] += 1
                else:
                    identified_coords[top_coord] = 1
        if col_a < col1:
            if data_matrix[row1][col1-2] == "S" and data_matrix[row2][col2-2] == "S":
                top_coord = (min(row1,row2,row_a), min(col1,col2,col_a))
                if top_coord in identified_coords:
                    identified_coords[top_coord] += 1
                else:
                    identified_coords[top_coord] = 1
    if row1 == row2:
        if row_a > row1:
            if data_matrix[row1+2][col1] == "S" and data_matrix[row2+1][col2] == "S":
                top_coord = (min(row1,row2,row_a), min(col1,col2,col_a))
                if top_coord in identified_coords:
                    identified_coords[top_coord] += 1
                else:
                    identified_coords[top_coord] = 1
        if row_a < row1:
            if data_matrix[row1-2][col1] == "S" and data_matrix[row2-2][col2] == "S":
                top_coord = (min(row1,row2,row_a), min(col1,col2,col_a))
                if top_coord in identified_coords:
                    identified_coords[top_coord] += 1
                else:
                    identified_coords[top_coord] = 1




for row_index, row in enumerate(data_matrix):
    for col_index, character in enumerate(row):
        if data_matrix[row_index][col_index] == 'M': # finds an initial M
            find_M_Pair(row_index,col_index)


top_coords_list = identified_coords.keys()

for i in range(10):
    print(top_coords_list[i])


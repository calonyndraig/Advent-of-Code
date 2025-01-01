"""For challenge found at https://adventofcode.com/2024/day/4"""

with open(r"input_files/day_04.txt","r") as file: # converts input into list of strings
    data = file.readlines()

def prep_data(data): # strips trailing space on matrix lines:
    return [x.strip() for x in data]

patterns = ['SSMM', 'MSSM', 'MMSS','SMMS'] # possible corner orders starting at top left

corners = [(-1,-1),(-1,1),(1,1),(1,-1)]

def check_corners(coord,matrix):
    a_x, a_y = coord
    corner_string = ''
    for corner in corners:
        new_x = a_x + corner[0]
        new_y = a_y + corner[1]
        corner_string += matrix[new_x][new_y]
    if corner_string in patterns:
        return True

def find_xmas(matrix):
    """Count XMAS occurences within matrix"""
    total_count = 0

    for i in range(1,len(matrix) - 1): # traverses matrix without outer edges
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 'A':
                if check_corners((i,j),matrix):
                    total_count += 1
    return total_count

matrix = prep_data(data)
print(find_xmas(matrix))
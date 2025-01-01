"""For challenge found at https://adventofcode.com/2024/day/4"""

with open(r"input_files/day_04.txt","r") as file: # converts input into list of strings
    data = file.readlines()

def prep_data(data): # strips trailing space on matrix lines:
    return [x.strip() for x in data]

directions = [(-1,0),  # (x,y)
              (1,0),   # x = row, y = col 
              (0,1),
              (0,-1),
              (-1,1),
              (-1,-1),
              (1,1),
              (1,-1)]

total_count = 0

def find_x_mas(coord, matrix, direction):
    """Checks given coordinate and direction for complete 'XMAS'"""
    
    letters_required = ["M","A","S"]
    x,y = coord
    new_x, new_y = direction
    
    for char in letters_required:
        x += new_x
        y += new_y
        if x < 0 or x > len(matrix)-1 or y < 0 or y > len(matrix[0])-1:
            return False
        elif matrix[x][y] == char:
            continue
        else:
            return False
    return True
        
def find_x(matrix):
    """iterates through the matrix to find all x's"""
    
    global total_count

    for row_num, row in enumerate(matrix):
        for col_num, char in enumerate(row):
            if char == 'X':
                for direction in directions:
                    if find_x_mas((row_num,col_num),matrix,direction):
                        total_count += 1

    return total_count                

matrix = prep_data(data)
print(find_x(matrix))

"""For challenge found at https://adventofcode.com/2024/day/6"""

with open(r"input_files/day_06.txt","r") as file: # converts input into list of strings
    matrix = [list(x.strip()) for x in file.readlines()]


guards = {'^' : [(-1,0),0], # up        For directional maker, assigns direction coords and an order number 
          '>' : [(0,1), 1], # right
          'v' : [(1,0), 2], # down
          '<' : [(0,-1),3], # left
        }

order_guards = {0:'^', 1:'>', 2:'v', 3:'<'}  # assigns new guard based on order number

def prep_data(matrix):
    """finds start position"""

    start_guards = [((i, j), guards[value]) for i, row in enumerate(matrix) for j, value in enumerate(row) if value in guards]
    startpos = start_guards[0]
    return startpos

def walk_matrix(matrix,startpos,direction,order):
    """traverses matrix, leaving 'X' markes where guard has been"""
    
    start_x, start_y = startpos
    dir_x, dir_y = direction
    new_x, new_y = start_x + dir_x, start_y + dir_y

    while 0 <= new_x and new_x < len(matrix) and 0 <= new_y and new_y < len(matrix[0]):
        # while loop exits when the guard is about to walk out of the matrix
        if matrix[new_x][new_y] == '.' or matrix[new_x][new_y] == 'X':
            # if path is clear, moves guard, marks previous position with "X"
            matrix[new_x][new_y] = matrix[start_x][start_y] 
            matrix[start_x][start_y] = "X"
            start_x, start_y = new_x, new_y
            new_x, new_y = new_x, new_y = start_x + dir_x, start_y + dir_y

        elif matrix[new_x][new_y] == '#':
            # if path is not clear, changes direction
            new_order = (order + 1) % 4
            matrix[start_x][start_y] = order_guards[new_order]
            direction = guards[matrix[start_x][start_y]][0]
            dir_x, dir_y = direction
            new_x, new_y = start_x + dir_x, start_y + dir_y
            order = new_order

    matrix[start_x][start_y] = "X" # finalizes final position with "X"
    
    return matrix

def count_xs(matrix):
    """counts total number of "X" markers in final matrix"""
    total_count = 0
    for i in matrix:
        for j in i:
            if j == "X":
                total_count += 1
    return total_count

startpos, direction_and_order = prep_data(matrix)
direction, order = direction_and_order
complete_matrix = walk_matrix(matrix,startpos,direction,order)
print(count_xs(complete_matrix))


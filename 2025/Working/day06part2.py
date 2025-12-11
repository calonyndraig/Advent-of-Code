import sys
# import time
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(6,2025)

math_lines = input.splitlines()

op_dict = ['+', '*']


def identify_col_starts(line):
    col_starts = []
    line += '  '  # add two spaces to avoid index error
    for i in range(len(line)):
        if line[i] in op_dict:
            digits = 0
            while i+1+digits < len(line) and line[i+1+digits] not in op_dict:
                digits += 1
            col_starts.append((i, digits))
    return col_starts

col_starts = identify_col_starts(math_lines[4])
print(col_starts)

### col_starts is a set of tuples with the index of the column start and the number of digits needed to parse


def create_exprs(col_info):
    index, digits = col_info
    nums =[]
    op = math_lines[4][index]
    
    for i in range(digits):
        next_num = math_lines[0][index+i] + math_lines[1][index+i] + math_lines[2][index+i] + math_lines[3][index+i]
        nums.append(int(next_num))

    nums.append(op)
    print(nums)
    return nums

def eval_expr(expr):

    op = expr[-1]
    num1 = expr[0]
    for num in expr[1:-1]:
        if op == '+':
            num1 += num
        elif op == '*':
            num1 *= num
    return num1

expr = (create_exprs(col_starts[5]))
print(expr)
result = eval_expr(expr)
print(result)
expr = (create_exprs(col_starts[-1]))
print(expr)
result = eval_expr(expr)
print(result)

                                                          

total = 0

for col in col_starts:

    next_expr = create_exprs(col)
    print("current expression", next_expr)
    if expr:
        subtotal = eval_expr(next_expr)
        total += subtotal

print(total)









#     if op_list[i] == '+':
#         use this function to get subtotal >>> op_dict['+'](int(num_1[i]), int(num_2[i]),int(num_3[i]),int(num_4[i]))
#     if op_list[i] == '*':
#         use this function to get subtotal >>> op_dict['*'](int(num_1[i]), int(num_2[i]),int(num_3[i]),int(num_4[i]))



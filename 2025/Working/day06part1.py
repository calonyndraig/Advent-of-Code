import sys
# import time
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(6,2025)

math_lines = input.splitlines()

split_lines = []
for line in math_lines:
    item = line.split()
    split_lines.append(item)

num_1 = split_lines[0]
num_2 = split_lines[1]
num_3 = split_lines[2]
num_4 = split_lines[3]
op_list = split_lines[4]


num_ops = len(split_lines[4])

op_dict = {
    '+': lambda w, x,y,z: w + x + y + z,
    '*': lambda w, x,y,z: w * x * y * z}

total = 0
for i in range(num_ops):
    # time.sleep(0.5)
    print(num_1[i],op_list[i],num_2[i],op_list[i],num_3[i],op_list[i],num_4[i])
    if op_list[i] == '+':
        total += op_dict['+'](int(num_1[i]), int(num_2[i]),int(num_3[i]),int(num_4[i]))
    if op_list[i] == '*':
        total += op_dict['*'](int(num_1[i]), int(num_2[i]),int(num_3[i]),int(num_4[i]))
    print(total)

print(total)
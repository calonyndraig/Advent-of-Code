import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(2,2025)

get_ranges = get_source.break_string_by_char(input,",")

def parse_range_list(list,char):
    range_list = []
    for item in list:
        start_end = get_source.break_string_by_char(item,char)
        start = int(start_end[0])
        end = int(start_end[1])
        print([start,end])
        range_list.append([start,end])
    return range_list

full_range_list = parse_range_list(get_ranges,"-")

invalid_ids = []

def check_id(id):
    string_id = str(id)
    if len(string_id) % 2 != 0:
        return False # if valid
    else:
        first_half = string_id[:len(string_id)//2]
        second_half = string_id[len(string_id)//2:]
        if first_half == second_half:
            return True # if invalid
        else:
            return False # if valid

def cycle_range(list_range):
    for i in range(list_range[0],list_range[1]+1):
        if i in invalid_ids:
            continue
        if check_id(i):
            invalid_ids.append(i)


for ids in full_range_list:
    # print(ids)
    cycle_range(ids)

print(sum(invalid_ids))
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

input = get_source.download_input(5,2025)

id_ranges_raw, ids = input.split("\n\n")

id_ranges_parsed = [(int(x), int(y)) for x,y in (line.split("-") for line in id_ranges_raw.splitlines())]

ids = [int(x) for x in ids.splitlines()]

def build_valid_list(id_ranges,ids):
    num_valid = 0
    for id in ids:
        for id_range in id_ranges:
            if id_range[0] <= id <= id_range[1]:
                num_valid += 1
                break
                
    

    return num_valid

print (build_valid_list(id_ranges_parsed,ids))
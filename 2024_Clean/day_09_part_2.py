"""For challenge found at https://adventofcode.com/2024/day/9"""

# Note: This one is INCOMPREHENSIBLY slow, but it does work.
# After days of trying new approaches, I must admit I don't have the
# knowledge or skill set to make this one any better.  
# Time to move on in hopes I learn more and that something
# like this feels easier to me in the future.


import os
import sys
from time import time

# Fallback to script directory if current working directory is incorrect
script_dir = os.path.dirname(sys.argv[0])
file_path = os.path.join(script_dir, "input_files/day_09.txt")

with open(file_path, "r") as file:
    image = file.read().strip()
    # creates disk image as single string

def unpack(string):
    """unpacks string into larger data list"""

    unpacked = []

    for idx, char in enumerate(string):
        multiplier = int(char)
        if idx % 2 == 0:
            unpacked.append((int(idx/2), multiplier))
        else:
            unpacked.append((".", multiplier))

    return unpacked

def compress(disk_list):
    """fills in blank spaces in list"""
    
    moving_downward = len(disk_list)-1
    moving_upward = 0

    while moving_downward > 0:
        while disk_list[moving_downward][0] == ".":
            moving_downward -= 1
            if moving_downward <= 0:
                break
        while disk_list[moving_upward][0] != ".":
            moving_upward += 1
            if moving_upward >= len(disk_list)-1 or moving_upward >= moving_downward:
                break
        
        if moving_downward <= 0:
            break
        if moving_upward >= moving_downward:
            moving_downward -= 1
            moving_upward = 0
            continue

        space_needed = disk_list[moving_downward][1]
        space_available = disk_list[moving_upward][1]

        if space_needed <= space_available:
            remaining = space_available-space_needed
            remaining_insert = (".", space_available-space_needed)
            new_upper = (".", space_needed)
            new_lower = disk_list[moving_downward]
            disk_list[moving_upward] = new_lower
            disk_list[moving_downward] = new_upper
            if remaining > 0:
                temp_list1 = disk_list[0:moving_upward+1]
                temp_list2 = [remaining_insert]
                temp_list3 = disk_list[moving_upward+1:]
                disk_list = temp_list1 + temp_list2 + temp_list3
                moving_downward += 1
            moving_downward -= 1
            moving_upward = 0
            
        else:
            moving_upward += 1
            continue

    return disk_list

def convert_list(disk_list):
    """unpacks tuples in disk_list into single list"""

    expanded_list = []

    for item in disk_list:
        char, multiplier = item
        for i in range(multiplier):
            expanded_list.append(char)
            
    return expanded_list

def check_sum(compressed_list):
    """creates final checksum for return"""

    checksum = 0
    
    for idx, block in enumerate(compressed_list):
        if block != ".":
            checksum += idx * int(block)

    return checksum

unpacked_list = unpack(image)
compressed_list = compress(unpacked_list)
expanded_list = convert_list(compressed_list)
print(check_sum(expanded_list))

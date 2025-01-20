"""For challenge found at https://adventofcode.com/2024/day/9"""

import os
import sys

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
            for i in range(multiplier):
                unpacked.append(idx/2) # file ID increases on even idx
        else:
            for i in range(multiplier):
                unpacked.append('.')

    return unpacked

def compress(disk_list):
    """fills in blank spaces in list"""

    left = 0
    right = len(disk_list)-1

    while left <= right:
        while disk_list[left] != ".":
            left += 1
        while disk_list[right] == ".":
            right -= 1

        if left >= right: # if last movement crosses left and right,
            break # prevents an extra swap

        disk_list[right], disk_list[left] = disk_list[left], disk_list[right]

    return disk_list

def check_sum(compressed_list):
    """creates final checksum for return"""

    checksum = 0
    
    for idx, block in enumerate(compressed_list):
        if block == ".":
            continue
        checksum += idx * int(block)

    return checksum
       

unpacked_list = unpack(image)
compressed_list = compress(unpacked_list)
print(check_sum(compressed_list))
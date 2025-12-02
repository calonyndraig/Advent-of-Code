import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

strings = get_source.download_input(5,2015)

string_list = get_source.string_convert_to_list(strings)

def list_pairs(string):
    pairs = []
    for i in range(len(string)-1):
        pair = string[i] + string[i+1]
        pairs.append(pair)
    return pairs

def has_repeated_pair(string):
    pairs = list_pairs(string)
    pair_dict = {}
    for i in range(len(pairs)):
        pair = pairs[i]
        if pair in pair_dict: 
            if i - pair_dict[pair] > 1: # if pair is found in the dictionary and the indices are not overlapping
                return True
        else:
            pair_dict[pair] = i # new pair is stored with the index of its first occurrence
    return False

def has_skipped_repeat(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def naughty_nice(string):
    if has_repeated_pair(string) and has_skipped_repeat(string):
        return True #nice
    return False #naughty

nice_strings = 0
for string in string_list:
    if naughty_nice(string):
        nice_strings += 1

print(nice_strings)
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

strings = get_source.download_input(5,2015)

string_list = get_source.string_convert_to_list(strings)

vowels = ['a','e','i','o','u']

excluded = ['ab','cd','pq','xy']

def naughty_nice(string):
    
    for item in excluded:
        if item in string:
            return False #naughty
        
    vowels_found = 0

    for char in string:
        if char in vowels:
            vowels_found += 1

    if vowels_found < 3:
        return False #naughty
    
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True #nice
        
    return False #naughty

nice_strings = 0
for string in string_list:
    if naughty_nice(string):
        nice_strings += 1
    
print(nice_strings)
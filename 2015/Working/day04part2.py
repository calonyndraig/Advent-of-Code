import hashlib
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

starting_key = get_source.download_input(4,2015)

zeroes = 6

prefix = "0" * zeroes # creates a string of zeroes

n = 1 # first digit to append to string 

while True: # infinite loop until value is found
    string_to_hash = starting_key + str(n) # adds n to end of string
    print(string_to_hash)
    hashed_string = hashlib.md5(string_to_hash.encode()).hexdigest() # creates md5 hash of string
    if hashed_string.startswith(prefix): # checks if hash starts with prefix
        break
    n += 1

print(hashed_string, string_to_hash, n)    

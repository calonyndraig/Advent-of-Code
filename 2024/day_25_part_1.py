from collections import deque

"""parsing and prepping data"""

with open("day_25_input.txt","r") as file:
    data = file.read()

data_separated = data.split("\n")

locks_and_keys = []

new_list = []
for item in data_separated:
    if item == '':
        locks_and_keys.append(new_list)
        new_list = []
    else:
        new_list.append(item)

"""Coding challenge"""
    
def count_pins(lock_or_key):
    pin_count = [0,0,0,0,0]
    for i in range(1,6):
        for j in range(0,5):
            if lock_or_key[i][j] == "#":
                pin_count[j] += 1
    return pin_count

lock_pins = []
key_pins = []


for item in locks_and_keys:
    pin_count = count_pins(item)
    if item[0] == "#####":
        lock_pins.append(pin_count)
    if item[0] == ".....":
        key_pins.append(pin_count)

matching_sets = []

def try_key(lock,key):
    for i in range(0,5):
        if lock[i] + key[i] <= 5:
            continue
        else:
            return False
    return True

combinations = []
for key in key_pins:
    for lock in lock_pins:
        combinations.append((tuple(key),tuple(lock)))

for key, lock in combinations:
    if try_key(lock,key):
        matching_sets.append((lock,key))

print(len(matching_sets))



""""CONFIRMED WORKS!  NO TOUCHY!"""



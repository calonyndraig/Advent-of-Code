"""For challenge found at https://adventofcode.com/2024/day/1"""

with open(r"input_files/day_01.txt") as file:  #converts input into list of strings
    data = file.readlines()

def prep_data(data):
    """Parses data into two lists of locations"""

    location_list_1 = []
    location_list_2 = []

    for item in data:
        locations = item.split('  ')
        location_list_1.append(int(locations[0]))
        location_list_2.append(int(locations[1][0:6]))
    
    return location_list_1, location_list_2

def calc_total_distance(location_list_1,location_list_2):
    """Calculates overall distance between two sorted lists"""

    location_list_1.sort()
    location_list_2.sort()

    total_distance = 0

    for i in range(len(location_list_1)):
        total_distance += abs(location_list_1[i] - location_list_2[i])

    return total_distance


loc1, loc2 = prep_data(data)
print(calc_total_distance(loc1, loc2))


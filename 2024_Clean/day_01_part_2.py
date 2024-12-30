"""For challenge found at https://adventofcode.com/2024/day/1"""

with open(r"input_files/day_01.txt") as file: #converts input into list of strings
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

def calc_simularity(location_list_1, location_list_2):
    """Calculates simularity score between two lists"""

    similarity_score = 0

    for item in location_list_1:
        similarity_score += item * location_list_2.count(item)

    return similarity_score

loc1, loc2 = prep_data(data)
print(calc_simularity(loc1, loc2))
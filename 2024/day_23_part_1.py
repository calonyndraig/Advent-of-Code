
"""parsing input"""

with open("day_23_input.txt","r") as file:
    connections = [line.strip() for line in file.readlines()]

connection_list = []

for item in connections:
    tuple = set(item.split('-'))
    connection_list.append(tuple)

"""coding notes:

ultimate goal = number of 3-way connections with 't' computers 
"""

possible_comps = ['t' + chr(x) for x in range(97,123)]

connection_dict = {}

total_connections = 0

for connection in connection_list:
    for comp in connection:
        if comp in possible_comps:
            temp_list = [item for item in connection if item != comp]
            connected_comp = temp_list[0]
            if comp not in connection_dict:
                connection_dict[comp] = [connected_comp]
            else:
                connection_dict[comp].append(connected_comp)

triangles = []

for key in connection_dict.keys():
    values = list(connection_dict[key])
    left = 0
    right = left + 1
    while left < len(values) - 1:
        while right <= len(values) - 1:
            if set((values[left], values[right])) in connection_list:
                new_set = set((values[left],values[right],key))
                if new_set not in triangles:
                    triangles.append(new_set)
            right += 1
        left += 1
        right = left + 1

print(len(triangles))

"""CONFIRMED WORKS!!!"""
    

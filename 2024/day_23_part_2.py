import networkx as nx
"""parsing input"""

with open("day_23_input.txt","r") as file:
    connections = [line.strip() for line in file.readlines()]

connection_list = []

for item in connections:
    tuple = set(item.split('-'))
    connection_list.append(tuple)

"""coding notes:

ultimate goal = find largest set of cliques, then use all elements to create
alphabetical password
"""

comp_graph = nx.Graph(connection_list)

cliques = list(nx.find_cliques(comp_graph))

largest_clique = max(cliques,key=len)

password_elements = sorted(largest_clique)
password = ''
for item in password_elements:
    password += (item + ',')

print(password) # note: remove final comma before copy/paste

"""CONFIRMED WORKS"""


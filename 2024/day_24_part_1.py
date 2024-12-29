from collections import deque

"""initializing data"""
with open("2024\day_24_input.txt") as file:
    unparsed_data = file.read()
    
lines = unparsed_data.strip().split("\n")


gates_to_compute = []
completed_gates = {}
to_compute = deque()

for line in lines:
    if ':' in line:
        key, value = line.split(': ')
        completed_gates[key] = int(value)
    elif '->' in line:
        gate1, operator, gate2, _, output_gate = line.split(' ')
        to_compute.append(tuple((gate1,operator,gate2,output_gate))) 

operator_dict = {'AND': lambda x,y: AND_operator(x,y),
                 'OR' : lambda x,y: OR_operator(x,y),
                 'XOR' : lambda x,y: XOR_operator(x,y)}

def custom_sort_key(item):
    starts_with_xy = (item[0].startswith('x') or item[0].startswith('y') or
                      item[2].startswith('x') or item[2].startswith('y'))
    return (not starts_with_xy, item)

to_compute = deque(sorted(to_compute, key=custom_sort_key))


def AND_operator(gate1,gate2):
    if completed_gates[gate1] == 1 and completed_gates[gate2] == 1:
        return 1
    else:
        return 0

def OR_operator(gate1,gate2):
    if completed_gates[gate1] == 1 or completed_gates[gate2] == 1:
        return 1
    else:
        return 0

def XOR_operator(gate1,gate2):
    if completed_gates[gate1] != completed_gates[gate2]:
        return 1
    else:
        return 0

def parse_deque(deque):
    while deque:
        gate1, operator, gate2, output_gate = deque.popleft()
        if output_gate in completed_gates:
            continue
        elif gate1 in completed_gates and gate2 in completed_gates:
            result = operator_dict[operator](gate1,gate2)
            completed_gates[output_gate] = result
        else:
            deque.append(tuple((gate1, operator, gate2,output_gate)))
    return completed_gates

parse_deque(to_compute)

z_gates = sorted([x for x in completed_gates.keys() if x.startswith('z')])

print(z_gates)
output_binary = ''

for item in z_gates:
    output_binary = str(completed_gates[item]) + output_binary

print(output_binary)

result = int(output_binary,2)

print(result)

""""CONFIRMED WORKS!  DO NOT TOUCH!"""



        




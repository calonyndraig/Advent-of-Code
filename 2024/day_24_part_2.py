from collections import deque
from itertools import combinations

"""initializing data"""
with open("day_24_input.txt") as file:
    unparsed_data = file.read()
    
lines = unparsed_data.strip().split("\n")

completed_gates = {}
gate_simulation = []


for line in lines:
    if ':' in line:
        key, value = line.split(': ')
        completed_gates[key] = int(value)
    elif '->' in line:
        gate1, operator, gate2, _, output_gate = line.split(' ')
        gate_simulation.append(tuple((gate1,operator,gate2,output_gate)))

z_gates =[]

for i in range(46):
    if i < 10:
        num = str(0) + str(i)
    else:
        num = str(i)
    new_gate = 'z' + num
    z_gates.insert(0,new_gate)


"""STARTING PART TWO SPECIFIC STUFF HERE"""

def create_binary(letter):
    gates = sorted([x for x in completed_gates.keys() if x.startswith(letter)])
    output_binary = ''
    for item in gates:
        output_binary = str(completed_gates[item]) + output_binary
    return output_binary

def create_desired_binary(x,y):
    z = bin(int((create_binary(x)), 2) + int((create_binary(y)), 2))[2:]
    return z

desired_z_gates = create_desired_binary('x','y')

expected_outputs = {}

for index, char in enumerate(list(desired_z_gates)):
    expected_outputs[z_gates[index]] = char

gate_combos = {}
re_completed_gates = {}

def simulate_circuit(gates, inputs):  # takes gates undetermined + inputs determined, returns new outputs dict
    wire_values = inputs.copy()
    outputs = {}
    unresolved_gates = gates.copy()
    print(unresolved_gates)
    while unresolved_gates:
        remaining_gates = []
        for gate in unresolved_gates:
            print("testing unresolved gate")
            if gate in re_completed_gates:
                outputs[out] = completed_gates[gate]
                wire_values[out] = completed_gates[gate]
            else:
                a, op, b, out = gate
                if a in wire_values and b in wire_values:
                    if op == "AND":
                        outputs[out] = wire_values[a] & wire_values[b]
                    elif op == "OR":
                        outputs[out] = wire_values[a] | wire_values[b]
                    elif op == "XOR":
                        outputs[out] = wire_values[a] ^ wire_values[b]
                    wire_values[out] = outputs[out]
                    re_completed_gates[gate] = outputs[out]
                else:
                    print("count not test, moving to remaining gates")
                    remaining_gates.append(gate)
            print(f"unresolvedgates = {len(unresolved_gates)},remaininggates = {len(remaining_gates)}")
        unresolved_gates = remaining_gates

    filtered_outputs = {key:value for key, value in outputs.items() if key.startswith('z')}
    return filtered_outputs

def find_correct_swaps(gates, inputs, expected_outputs, n_swaps=4):
    output_wires = [gate[3] for gate in gates] # output gate in gate_simulation
    all_swaps = combinations(output_wires, 2 * n_swaps) # combination list of all output swaps
    
    for swap_set in all_swaps:
        print("swapping gates")
        swapped_gates = apply_swaps(gates, swap_set) #swaps the outputs in the gate simulation
        print("simulating new circuit")
        outputs = simulate_circuit(swapped_gates, inputs) #Simulates the cicuits with the swaps
        print('testing outputs')
        if outputs == expected_outputs: 
            return sorted(swap_set) #only returns list of swaps if they work
    return None

def apply_swaps(gates, swap_set):
    swaps = list(zip(swap_set[::2], swap_set[1::2]))
    swapped_gates = gates.copy() #creates simulated gates copy
    for i, gate in enumerate(swapped_gates): 
        output_wire = gate[3]  # The output wire of the current gate
        for a, b in swaps:
            if output_wire == a:
                swapped_gates[i] = (*gate[:3], b)  # Swap a -> b
            elif output_wire == b:
                swapped_gates[i] = (*gate[:3], a)  # Swap b -> a
    return swapped_gates

swaps = find_correct_swaps(gate_simulation,completed_gates,expected_outputs)
print(swaps)
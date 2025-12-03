import sys
from pathlib import Path
from functools import lru_cache

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

import get_source

commands = get_source.download_input(7,2015)

command_list = get_source.string_convert_to_list(commands)

instructions_list ={} # creates dictionary of wires with instructions

for command in command_list:
    expr, target = command.split(" -> ") 
    instructions_list[target] = expr.split()

# after commands have been split into list, proceed with connecting one to the next

def is_number(expr): # checks to see if expression is a single number
    return expr.isdigit()

@lru_cache(maxsize=None)
def evaluate_wire(wire): # primary function, evaluates a single wire
    
    if is_number(wire): # check if wire already has a number
        return int(wire)
    
    expr = instructions_list[wire] # pull expression from dictionary

    if len(expr) == 1: # if instructions directly point to a number or to a single item in the target list
        return evaluate_wire(expr[0]) & 0xFFFF # feed the current expression back into the evaluate_wire function
    
    if len(expr) == 2: # if there are exactly two items in the expression (i.e., "NOT" and a second target):
        op, x = expr
        assert op == "NOT"
        return(~evaluate_wire(x)) & 0xFFFF # pulls the not operator version of the wire / flips the bits
    
    # if length of the expression is more than two, it should by default be 3.

    x, op, y = expr

    if op == "AND":
        return(evaluate_wire(x) & evaluate_wire(y)) & 0xFFFF
    
    elif op == "OR":
        return (evaluate_wire(x) | evaluate_wire(y)) & 0xFFFF
    
    elif op == "LSHIFT":
        return (evaluate_wire(x) << int(y)) & 0xFFFF
    
    elif op == "RSHIFT":
        return (evaluate_wire(x) >> int(y)) & 0xFFFF



print(evaluate_wire("a"))

    


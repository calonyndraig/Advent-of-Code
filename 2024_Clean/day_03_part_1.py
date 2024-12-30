"""For challenge found at https://adventofcode.com/2024/day/3"""

import re

with open(r"input_files/day_03.txt","r") as file: # converts input into long string
    data = file.read()

def prep_data(data):
    """Finds all valid commands"""

    function_list = re.findall("mul\(\d+\,\d+\)", data)
    return function_list

def multiply(command):
    """Parses and executes command"""

    num1,num2 = re.findall("\d+",command)
    return int(num1) * int(num2)
                               
def solution(function_list):
    """Completes overall calculation"""

    solution = 0
    
    for item in function_list:
        multiple = multiply(item)
        solution += multiple
    
    return solution

function_list = prep_data(data)
print(solution(function_list))
import re

with open(r"input_files/day_03.txt","r") as file:
    data = file.read()

def prep_data(data):
    function_list = re.findall("mul\(\d+\,\d+\)", data)
    return function_list

def multiply(command):
    num1,num2 = re.findall("\d+",command)
    return int(num1) * int(num2)
                               
def solution(function_list):
    solution = 0
    for item in function_list:
        multiple = multiply(item)
        solution += multiple
    return solution

function_list = prep_data(data)
print(solution(function_list))
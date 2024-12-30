import re

with open(r"input_files/day_03.txt","r") as file:
    data = file.read()

def prep_data(data):
    function_list = re.findall("do\(\)|mul\(\d+\,\d+\)|don\'t\(\)",data)
    return function_list

def compile_commands(function_list):
    do_ind = True
    do_list = []
    for item in function_list:
        if item == "don't()":
            do_ind = False
        elif item == "do()":
            do_ind = True
        elif do_ind:
            do_list.append(item)
    return do_list

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
do_list = compile_commands(function_list)
print(solution(do_list))
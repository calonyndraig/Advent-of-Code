import requests
import copy
import re


def fetch_data(url,session):
    headers = {
    'Cookie': f'session={session}',
        }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # The input data as text
        data = response.text
    else:
        data = None

    return data


data = fetch_data('https://adventofcode.com/2024/day/17/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
data = data.splitlines()
register_data = []
for line in data[0:3]:
    item = re.findall(r'\d+',line)
    register_data.append(item[0])

register_A = int(register_data[0])
register_B = int(register_data[1])
register_C = int(register_data[2])

instructions_list = re.findall(r'\d',data[4])
instructions_list = [int(x) for x in instructions_list]



## challenge bits###

## A four digit set of instructions includes:
## 1[0]. Determines what instruction to follow
## 2[1]. Operand
## 3[2]. Determines what instruction to follow
## 4[3]. Operand
##       Halts program 

# register_A = 729  # test data
# register_B = 0     # test data
# register_C = 0      # test data

# instructions_list = [0,1,5,4,3,0]  # test data

target_output = ''
for i in instructions_list:
    if target_output == '':
        target_output = f'{i}'
    else:
        target_output += f",{i}"

instruction_pointer = 0
operand_pointer = 1
instruction_pointer_jump = True
output = ''

halt_program = False
part2_result_output = None

combo_operands = {4: lambda: register_A,
                    5: lambda: register_B,
                    6: lambda: register_C,
                    7: "invalid program"
                    }  # 0 through 3 are literal, 8 and greater are not used

def instructions_0(operand,part=1):
    global register_A
    x = register_A
    if operand in combo_operands:
        y = combo_operands[operand]() ** 2
    else:
        y = 2 ** operand
    register_A = int(x/y)

def instructions_1(operand,part=1):
    global register_B
    x = register_B
    y = operand
    register_B = x ^ y

def instructions_2(operand,part=1):
    global register_B
    x = combo_operands[operand]()
    result = x % 8
    register_B = result

def instructions_3(operand,part=1):
    global instruction_pointer
    global instruction_pointer_jump
    global operand_pointer
    if register_A != 0:
        instruction_pointer = operand
        operand_pointer = instruction_pointer + 1
        instruction_pointer_jump = False

def instructions_4(operand,part=1):
    global register_B, register_C
    x = register_B
    y = register_C
    register_B = x ^ y

def instructions_5(operand,part=1):
    global output
    global part2_result_output
    x = combo_operands[operand]()
    result = x % 8
    if part == 2:
        part2_result_output = result
    elif output == '':
        output = f"{result}"
    else:
        output += f",{result}"

    # print(f"Current output: {output}")
    # if len(output) <= len(target_output):
    #     halt_program = output == target_output[0:len(output)]
    #     # if not halt_program:
    #     #     # print("Current match, continuing")
    #     # else:
    #         # print("Halting program...")

    
def instructions_6(operand,part=1):
    global register_A
    global register_B
    x = register_A
    if operand in combo_operands:
        y = 2 ** combo_operands[operand]()
    else:
        y = operand ** 2
    register_B = int(x/y)

def instructions_7(operand,part=1):
    global register_A
    global register_C
    x = register_A
    if operand in combo_operands:
        y = 2 ** combo_operands[operand]()
    else:
        y = operand ** 2
    register_C = int(x/y)    



instruction_map = {0: instructions_0,
                    1: instructions_1,
                    2: instructions_2,
                    3: instructions_3,
                    4: instructions_4,
                    5: instructions_5,
                    6: instructions_6,
                    7: instructions_7
                    }

      



def run_program(starting_A,part=1):
    global register_A, register_B, register_C, instruction_pointer, operand_pointer, instruction_pointer_jump, output, halt_program
    register_A = starting_A
    register_B = 0
    register_C = 0
    instruction_pointer = 0
    operand_pointer = instruction_pointer + 1
    instruction_pointer_jump = True
    output = ''    
    while instruction_pointer < len(instructions_list) - 1:
        instruction = instructions_list[instruction_pointer]
        operand = instructions_list[operand_pointer]
        instruction_map.get(instruction,lambda x: None)(operand,part)
        if part2_result_output:
            return part2_result_output
        if not instruction_pointer_jump:
            instruction_pointer_jump = True
        else:
            instruction_pointer += 2
            operand_pointer = instruction_pointer + 1
    return output




current_digit = len(instructions_list)-1
current_register_A_list = [0]

while current_digit >= 0:
    next_register_A_list = []
    desired_output = instructions_list[current_digit]  # starts backwards with last digit
    print(desired_output, current_digit)
    for reg_A in current_register_A_list:
        new_register_A = reg_A * 8
        for y in range(8):
            current_register_A = new_register_A + y
            print(f"Running program with {current_register_A}...")
            NewOutput = run_program(current_register_A, 2)
            print(f"Part 2 Result = {part2_result_output}")
            print(current_register_A, NewOutput, NewOutput==desired_output)
            if NewOutput == desired_output:
                next_register_A_list.append(current_register_A)

    current_digit -= 1
    current_register_A_list = copy.deepcopy(next_register_A_list)

print(current_register_A_list)







# starting_A = -1
# while output != target_output:
#     starting_A += 1
#     print(f"testing Starting_A = {starting_A}")
#     halt_program = False
#     output = run_program(starting_A)
    

# print(starting_A)


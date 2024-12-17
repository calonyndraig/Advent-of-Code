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

instructions_string = ''
for item in instructions_list:
    if instructions_string == '':
        instructions_string += str(item)
    else: 
        instructions_string += f',{str(item)}'
Originalprogram = tuple(map(int, instructions_string.split(",")))

print(Originalprogram)


OriginalRegisterList = (register_A,register_B,register_C)
OriginalRegisterT = tuple(OriginalRegisterList)

print(OriginalRegisterList)
print(OriginalRegisterT)


def Program(RegA, RegisterTuple, Part):
    ProgramLength = len(Originalprogram)
    Register = {}
    for v, r in enumerate(["A","B","C"]):
        Register[r] = RegisterTuple[v]
    Pointer = 0
    OutputList = []
    Register["A"] = RegA

    def Combo(Operand):
        if Operand < 4:
            return Operand
        if Operand == 4:
            return Register["A"]
        if Operand == 5:
            return Register["B"]
        if Operand == 6:
            return Register["C"]
        else:
            print("7 combo detected")

    while Pointer < ProgramLength-1:
        PointerJump = True
        Operator, Operand = Originalprogram[Pointer:Pointer+2]
        if Operator == 0: #adv
            Numerator = Register["A"]
            Denom = 2**Combo(Operand)
            Register["A"] = Numerator // Denom
        elif Operator == 1: #bxl
            B = Register["B"]
            Register["B"] = B ^ Operand
        elif Operator == 2: #bst
            Register["B"] = Combo(Operand) % 8
        elif Operator == 3: #jnz
            if Register["A"] != 0:
                Pointer = Operand
                PointerJump = False
        elif Operator == 4: #bxc
            B, C = Register["B"], Register["C"]
            Register["B"] = B ^ C
        elif Operator == 5: #out
            Output = Combo(Operand) % 8
            if Part == 2:
                return Output, Register["A"]
            OutputList.append(Output)

        elif Operator == 6: #bdv
            Numerator = Register["A"]
            Denom = 2**Combo(Operand)
            Register["B"] = Numerator // Denom
        elif Operator == 7: #cdv
            Numerator = Register["A"]
            Denom = 2**Combo(Operand)
            Register["C"] = Numerator // Denom

        if PointerJump:
            Pointer += 2

    OutputString = ""
    for t in OutputList:
        OutputString += str(t)
        OutputString += ","
    OutputString = OutputString[:-1]
    if Part == 1:
        return OutputString
    else:
        return True, OutputString

Part1Answer = Program(OriginalRegisterT[0],OriginalRegisterT,1)


Place = len(Originalprogram)-1
CurrentRegAs = [0]

while Place >= 0:
    NextRegAs = []
    ExpectedOutput = Originalprogram[Place]
    #print(ExpectedOutput, Place)
    for RA in CurrentRegAs:
        NewRA = RA*8
        for y in range(8):
            CRA = NewRA + y
            NewOutput, PassedA = Program(CRA, OriginalRegisterT, 2)
            #print(CRA, NewOutput, NewOutput==ExpectedOutput, PassedA)
            if NewOutput == ExpectedOutput:
                NextRegAs.append(CRA)

    Place -= 1
    CurrentRegAs = copy.deepcopy(NextRegAs)

print(CurrentRegAs)

Part2Answer = min(CurrentRegAs)

print(Program(Part2Answer,OriginalRegisterT,1))

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")
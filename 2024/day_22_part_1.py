import math

""" data parsed into list of integers"""
with open("day_22_input.txt","r") as file:
    input_list = file.readlines()

input_list = [int(x) for x in input_list]

"""notes on building code"""

# step 1 = num * 64, mix result into num

# step 2 = new num / 32, round down to nearest int; mix result into new num; prune new num

# step 3 = multiply result by 2048, mix into result, then prune

# mixing = calculate bitwise XOR

# pruning = modulo 16777216

def mix_prune(num1, num2):
    return (num1 ^ num2) % 16777216

def mixing(num1, num2):
    return num1 ^ num2

def pruning(num):
    return num % 16777216

def step_one(num):
    num2 = num * 64
    return mix_prune(num,num2)

def step_two(num):
    num2 = abs(math.floor(num / 32))
    new_num = mixing(num,num2)
    return pruning(new_num)

def step_three(num):
    new_num = num * 2048
    next_num = mixing(num,new_num)
    return pruning(next_num)


def next_secret_num(num):
    # print(f"Original secret number: {num}")
    num = step_one(num)
    # print(f"After step one: {num}")
    num = step_two(num)
    # print(f"After step two: {num}")
    num = step_three(num)
    # print(f"After step three: {num}")
    return num


total = 0

for item in input_list:
    print(f"Starting new item: {item}")
    secret_num = item
    for i in range(2000):
        secret_num = next_secret_num(secret_num)
    print(f"Final secret number: {secret_num}")
    total += secret_num
    print(f"Current sum total: {total}")

print(total)
    
"""Confirmed solution!!!"""
    
import math

""" data parsed into list of integers"""
with open("day_22_input.txt","r") as file:
    input_list = file.readlines()

input_list = [int(x) for x in input_list]

"""notes on building code"""

# step 1 = num * 64, mix result into num, prune

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


"""part 1 calculations"""

# total = 0

# for item in input_list:
#     print(f"Starting new item: {item}")
#     secret_num = item
#     for i in range(2000):
#         secret_num = next_secret_num(secret_num)
#     print(f"Final secret number: {secret_num}")
#     total += secret_num
#     print(f"Current sum total: {total}")

# print(total)
    
"""Part 1 solution Confirmed"""
    
"""Part 2 coding notes"""

def determine_price(num):
    return num % 10

# ultimate goal = calculating number of bananas you can get
# bananas = first number of certain sequence of differences

def build_price_list(num,generations):
    prices = []
    next_num = num
    for i in range(generations):
        price = determine_price(next_num)
        prices.append(price)
        next_num = next_secret_num(next_num)
    return prices

large_sequence_dict = {}
max_bananas = 0

def build_sequence_dict(prices):
    sequence_dict = {}
    for index, item in enumerate(prices[0:-4]):
        current_price = prices[index+4]
        if current_price <= 0:
            continue
        sequence = []
        for i in range(1,5):
            difference = prices[index+i] - prices[index + i - 1]
            sequence.append(difference)
        sequence = tuple(sequence)
        if sequence not in sequence_dict:
            # or current_price > sequence_dict[sequence]
            sequence_dict[sequence] = current_price
    return sequence_dict

def update_global_sequence_list(sequence_dict):
    global max_bananas
    for key, value in sequence_dict.items():
        if key not in large_sequence_dict:
            large_sequence_dict[key] = value
        else:
            large_sequence_dict[key] += value
        if large_sequence_dict[key] > max_bananas:
            max_bananas = large_sequence_dict[key]
    return large_sequence_dict


for item in input_list:
    price_list = build_price_list(item,2001)
    new_sequence_building = build_sequence_dict(price_list)
    new_global_dict = update_global_sequence_list(new_sequence_building)
    
print(max_bananas)

"""CONFIRMED TO WORK!  DON'T TOUCH IT!"""
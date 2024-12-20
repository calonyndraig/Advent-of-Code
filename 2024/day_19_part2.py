import re
import copy
from functools import lru_cache
from collections import Counter, defaultdict
from pip._vendor import requests

"""data parsing"""

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

data = fetch_data('https://adventofcode.com/2024/day/19/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")

data = data.splitlines()

available_towels = data[0].split(', ')
sorted_towels = sorted(available_towels, key=lambda x: (len(x),x))
reversed_towels = []
for towel in reversed(sorted_towels):
    reversed_towels.append(towel)




desired_designs = data[2:]


"""solution decoding"""

def is_possible(design,towels_list):
    towels_list = set(towels_list)
    n = len(design)
    dp = [False] * (n+1)
    dp[0] = True

    used_towels = [set() for _ in range(n+1)]
    used_towels[0] = set()

    for i in range(1,n+1):
        for j in range(i):
            substring = design[j:i]
            if substring in towels_list and dp[j] and substring not in used_towels:
                dp[i] = True
                used_towels[i] = used_towels[j] | {substring}
                break
    return dp[n]

# total_possible = 0
# for design in desired_designs:
#     true_false = is_possible(design,sorted_towels)
#     if true_false:
#         total_possible += 1

# print(total_possible)
    
# def find_configurations(design, towels_list):
#     def recurse_helper(design, used_towels):    
#         if not design:
#             return [[]]
#         configurations = []
#         for towel in towels_list:
#             if towel not in used_towels and design.startswith(towel):
#                 remaining_design = design[len(towel):]
                
#                 for sub_composition in recurse_helper(remaining_design, used_towels):
#                     configurations.append([towel]+sub_composition)
#         return configurations
#     return len(recurse_helper(design,set()))



# def find_configurations(design, towels_list):
    

#     n = len(design)
#     dp = defaultdict(list)  # dp[i] stores all configurations for design[:i]
#     dp[0] = [[]]  # Base case: 1 way to compose an empty design

#     for i in range(1, n + 1):
#         for towel in towels_list:
#             if i >= len(towel) and design[i - len(towel):i] == towel:
#                 print(design[i - len(towel):i])
#                 for config in dp[i - len(towel)]:
#                     dp[i].append(config + [towel])

#     return len(dp[n])  # Count the number of configurations for the full design



total_possible = 0

def part_two():
    towels = available_towels
    displays = desired_designs

    @lru_cache(maxsize=2000)
    def num_ways(cur):
        if len(cur) == 0:
            return 1
        total_num_ways = 0
        for towel in towels:
            l_towel = len(towel)
            if towel == cur[-l_towel:]:
                total_num_ways += num_ways(cur[:-l_towel])

        return total_num_ways

    total_num_ways = 0
    for display in displays:
        total_num_ways += num_ways(display)

    return total_num_ways



"""Test cases"""

print(part_two())
# print("brwrr")
# print(find_configurations('brwrr',['r','wr','b','g','bwu','rb','gb','br']))
# print('bggr')
# print(find_configurations('bggr',['r','wr','b','g','bwu','rb','gb','br']))
# print('gbbr')
# print(find_configurations('gbbr',['r','wr','b','g','bwu','rb','gb','br']))
# print('rrbgbr')
# print(find_configurations('rrbgbr',['r','wr','b','g','bwu','rb','gb','br']))
# print('ubwu')
# print(find_configurations('ubwu',['r','wr','b','g','bwu','rb','gb','br']))
# print('bwurrg')
# print(find_configurations('bwurrg',['r','wr','b','g','bwu','rb','gb','br']))
# print('brgr')
# print(find_configurations('brgr',['r','wr','b','g','bwu','rb','gb','br']))
# print('bbrgwb')
# print(find_configurations('bbrgwb',['r','wr','b','g','bwu','rb','gb','br']))

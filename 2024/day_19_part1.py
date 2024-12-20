import re
import copy
from collections import Counter
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

total_possible = 0
for design in desired_designs:
    true_false = is_possible(design,sorted_towels)
    if true_false:
        total_possible += 1

print(total_possible)
    
"""Test cases"""

# print(is_possible('brwrr',['r','wr','b','g','bwu','rb','gb','br']))
# print(is_possible('bggr',['r','wr','b','g','bwu','rb','gb','br']))
# print(is_possible('gbbr',['r','wr','b','g','bwu','rb','gb','br']))
# print(is_possible('rrbgbr',['r','wr','b','g','bwu','rb','gb','br']))
# print(is_possible('ubwu',['r','wr','b','g','bwu','rb','gb','br']))
# print(is_possible('bwurrg',['r','wr','b','g','bwu','rb','gb','br']))
# print(is_possible('brgr',['r','wr','b','g','bwu','rb','gb','br']))
# print(is_possible('bbrgwb',['r','wr','b','g','bwu','rb','gb','br']))

import math
# import numpy as np
from pip._vendor import requests
# import re


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

    data = data.split()
    for index, item in enumerate(data):
        data[index] = int(data[index])

    return data

data_memo = {}


def single_stone(num,blinks_remaining):
    global data_memo

    if (num,blinks_remaining) in data_memo:
        return data_memo[((num,blinks_remaining))]
    
    if blinks_remaining == 0:
        data_memo[(num,0)] = 1
        return 1
    
    if num == 0:
        result = single_stone(1,blinks_remaining-1)
        data_memo[(num,blinks_remaining)] = result
        return result
            
    num_length = int(math.log10(abs(num))) + 1
            
    if num_length % 2 == 0 and num_length !=0:            
        first_half = int(num // (10 ** (num_length / 2)))
        second_half = int(num - (first_half * (10 ** (num_length / 2))))
        first_result = single_stone(first_half,blinks_remaining-1)
        second_result = single_stone(second_half,blinks_remaining-1)
        result = first_result + second_result
        data_memo[(num,blinks_remaining)] = result
        return result
    
    else:
        result = single_stone(num*2024,blinks_remaining-1)
        data_memo[(num, blinks_remaining)] = result
        return result
    
def all_stones(data,blinks):
    stones_total = 0
    data_copy = sorted(data)
    for item in data_copy:
        result = single_stone(item,blinks)
        stones_total += result
    return stones_total
         

if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/11/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    print(all_stones(data,75))
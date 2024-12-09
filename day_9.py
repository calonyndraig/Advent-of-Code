# import numpy as np
from pip._vendor import requests
# import re
import copy


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

def re_string(data):
    uncompressed_data = []
    j = 0
    for index,char in enumerate(data):
        increase_j = False
        if index % 2 == 0:
            for i in range(int(char)):
                uncompressed_data.append(str(j))
        else:
            if (int(char)) == 0:
                increase_j = True
            for i in range(int(char)):
                uncompressed_data.append(".")
                increase_j = True
        
        if increase_j:
            j += 1
    return uncompressed_data
 
def compress(uncompressed_data):
    j = len(uncompressed_data)-1
    data_sum = 0
    for index,item in enumerate(uncompressed_data):
        if j > index:
            if item == ".":
                while uncompressed_data[j] == ".":
                    j -= 1
                uncompressed_data[index], uncompressed_data[j] = uncompressed_data[j],uncompressed_data[index]
                j -= 1
    # compressed_data = ''.join(uncompressed_data)      
    return uncompressed_data

def calculate(uncompressed_data):
    checksum = 0
    for index,item in enumerate(uncompressed_data):
        if item.isdigit(): 
            checksum += index * int(item)
    return checksum



if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/9/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    test_data = "2333133121414131402"
    new_string = re_string(test_data)
    compressed = compress(new_string)
    num = calculate(compressed)
    print(num)
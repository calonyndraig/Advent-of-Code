import copy
import json
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

    data.splitlines()
    

    correct_data = [int(x) for x in data[0:-1] if x!= "\n"]
    
    # correct_data.append(7)

    return correct_data

def re_string(correct_data):
    uncompressed_data = []
    for index,item in enumerate(correct_data):
        if index % 2 == 0:
            uncompressed_data.append((index/2,item))
        else:
            uncompressed_data.append(('.',item))
    return uncompressed_data
 
def compress(uncompressed_data):
    j = len(uncompressed_data) - 1
    i = 0
    while j >= 0:
        i = 0
        if uncompressed_data[j][0] != '.':
            needed_length = uncompressed_data[j][1]
            swapped = False
            while i < j and not swapped:
                if uncompressed_data[i][0] == '.' and uncompressed_data[i][1] >= needed_length:            
                    item_to_swap = ('.', needed_length)
                    remaining_item = ('.', uncompressed_data[i][1] - needed_length)
                    uncompressed_data[j], uncompressed_data[i] = item_to_swap, uncompressed_data[j]
                    uncompressed_data.insert(i+1,remaining_item)
                    swapped = True
                else:
                    i += 1     
        j -= 1
    return uncompressed_data

def re_expand(data):
    new_list = []
    for item in data:
        for i in range(item[1]):
            new_list.append(item[0])


    return new_list




            
         


def calculate(compressed_data):
    checksum = 0   
    for index,item in enumerate(compressed_data):
        if item != ".":
            to_add = item*index
            checksum += to_add
        
    return checksum

def send_to_json(data,filename):
    with open (filename, "w") as file:
        json.dump(data[0:-1],file)



if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/9/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    # print(data[-1])
    # print(len(data))
    # print(data[-1])
    expanded = re_string(data)
    # print(expanded[-5:])
    # send_to_json(expanded,"expanded_list.json")
    compressed = compress(expanded)
    # send_to_json(compressed,"compressed_list.json")
    reexpanded = re_expand(compressed)
    # send_to_json(reexpanded,"reexpanded_list.json")
    calculated = calculate(reexpanded)
    print(calculated)
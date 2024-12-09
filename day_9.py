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
            for i in range(item):
                uncompressed_data.append(index/2)
        else:
            for i in range(item):
                uncompressed_data.append(".")
    return uncompressed_data
 
def compress(data):
    j = len(data)-1


        
        if j > index and item == ".":
            index = i
            needed_length = 1
            

            while data[j] == "." and j > index:
                j -= 1
            if j < index:
                break
            
            
            
            else:
                data[index], data[j] = data[j], data[index]
    return data

def calculate(compressed_data):
    checksum = 0
    for index,item in enumerate(compressed_data):
        # print(item)
        if item != ".": 
            to_add = index * int(item)
            checksum += to_add
    return checksum

def send_to_json(data,filename):
    with open (filename, "w") as file:
        json.dump(data[0:-1],file)



if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/9/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    # print(data[-1])
    expanded = re_string(data)
    print(expanded[-10:])
    send_to_json(expanded,"expanded_list.json")
    compressed = compress(expanded)
    send_to_json(compressed,"compressed_list.json")
    calculated = calculate(compressed)
    print(calculated)
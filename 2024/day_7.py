# import numpy as np
from pip._vendor import requests
# import re

url = 'https://adventofcode.com/2024/day/6/input'

session = "53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd"
headers = {
    'Cookie': f'session={session}',
}
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

def parse_data(data):
    parsed_data = []
    rows = data.splitlines()
    for row in rows:
        temp_list = []
        entry = row.split(' ')
        for item in entry:
            if item[-1] == ':':
                temp_list.append(int(item[0:-1]))
            else:
                temp_list.append(int(item))
        parsed_data.append(temp_list)
    return parsed_data
                
def goals_and_items(entry):
    goal = entry[0]
    items = entry[1:]
    return goal, items

def testing(goal,items,currentresult=0):
    if not items:
        return goal == currentresult
    if currentresult > goal:
        return False
    
    next_number = items[0]
    remaining_numbers = items[1:]
    

    alt_next_number = int(str(currentresult)+str(next_number))

    if testing(goal,remaining_numbers,currentresult+next_number):
        return True
    if testing(goal,remaining_numbers,currentresult*next_number):
        return True
    
    
    if testing(goal,remaining_numbers,currentresult+alt_next_number):
        return True
    if testing(goal,remaining_numbers,currentresult*alt_next_number):
        return True

def chat_gpt_help(goal,items,current_result=0):
    if not items:
        return current_result == goal
    
    next_number = items[0]
    remaining_numbers = items[1:]
    
    # Add
    if chat_gpt_help(goal, remaining_numbers, current_result + next_number):
        return True
    # Multiply
    if chat_gpt_help(goal, remaining_numbers, current_result * next_number):
        return True
    # Concatenate
    if chat_gpt_help(goal, remaining_numbers, int(str(current_result) + str(next_number))):
        return True
    
    return False
            


if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/7/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    parsed_data = parse_data(data)
    calibration_sum = 0
    for item in parsed_data:
        goal_test_list = goals_and_items(item)
        print(f"testing, {item}")
        if chat_gpt_help(goal_test_list[0],goal_test_list[1]):
            calibration_sum += goal_test_list[0]
    print(calibration_sum)

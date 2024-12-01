import requests
import time

url = 'https://adventofcode.com/2024/day/1/input'

session = "53616c7465645f5f3d0359100dde556a580def32a5eccfcc5230a4e689e11e4c1d7bfd5d5bda1d1b9dd6916f8b3a7cdf204f8190adebc75f257a2eb2bc5c003c"
headers = {
    'Cookie': f'session={session}',
}


response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # The input data as text
    data = response.text
else:
    data = None
list1 = []
list2 = []
even_odd = 0
newnum = ''
for char in data:
    if char.isdigit():
        newnum += char
    else:
        if even_odd % 2 == 0:
            list1.append(newnum)
        if even_odd % 2 != 0:    
            list2.append(newnum)
        newnum = ''
        even_odd += 1

list1 = sorted([int(x) for x in list1 if x != ''])
list2 = sorted([int(x) for x in list2 if x != ''])

total_diff = 0
for i in range(len(list1)):
    current_diff = abs(list1[i] - list2[i])
    total_diff += current_diff

print(total_diff)

total_sim = 0
for item in list1:
    if item in list2:
        count = list2.count(item)
        score = item * count
        total_sim += score

print(total_sim)
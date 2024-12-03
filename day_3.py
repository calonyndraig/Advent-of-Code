import requests
import re

url = 'https://adventofcode.com/2024/day/3/input'

session = "53616c7465645f5f3d0359100dde556a580def32a5eccfcc5230a4e689e11e4c1d7bfd5d5bda1d1b9dd6916f8b3a7cdf204f8190adebc75f257a2eb2bc5c003c"
headers = {
    'Cookie': f'session={session}',
}


# response = requests.get(url, headers=headers)
response = requests.get(url,headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # The input data as text
    data = response.text
else:
    data = None

# print(data)

pattern = r'do\(\)|mul\(\d+,\d+\)|don\'t\(\)'

matches = re.findall(pattern, data)

print(matches)
do_ind = True
do_funcs = []
dont_funcs = []
for item in matches:
    if item == "do()":
        do_ind = True
    elif item == "don't()":
        do_ind = False
    elif do_ind:
        do_funcs.append(item)
    elif not do_ind:
        dont_funcs.append(item)

# print(do_funcs[0:5])
# print(dont_funcs[0:5])
    


pattern = r'\d+,\d+'

def mul(x,y):
    """multiplies two terms"""
    return(x*y)

total_mults = 0

for item in do_funcs:
    inputs = re.findall(pattern,item)
    for item in inputs:
        variables = item.split(',')
        # print(variables)
        total_mults += (mul(int(variables[0]),int(variables[1])))

print(total_mults)
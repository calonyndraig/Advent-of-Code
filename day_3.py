import requests
import re

url = 'https://adventofcode.com/2024/day/3'

# session = "53616c7465645f5f3d0359100dde556a580def32a5eccfcc5230a4e689e11e4c1d7bfd5d5bda1d1b9dd6916f8b3a7cdf204f8190adebc75f257a2eb2bc5c003c"
# headers = {
#     'Cookie': f'session={session}',
# }


# response = requests.get(url, headers=headers)
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # The input data as text
    data = response.text
else:
    data = None

print(data)
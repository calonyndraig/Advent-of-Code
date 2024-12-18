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

    return data

# def parse_data(data):  ### creates matrix
#     parsed_data = []
#     rows = data.splitlines()
#     for row in rows:
#         parsed_data.append(list(row))
#     return parsed_data

if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/9/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    print(type(data))
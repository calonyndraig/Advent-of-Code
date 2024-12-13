# import numpy as np
import re
from sympy import symbols, Eq, solve
from pip._vendor import requests



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

    data_sets = data.split('\n\n')
    number_sets = []
    for item in data_sets:
        numbers = re.findall(r'\d+', item)
        numbers = list(map(int, numbers))
        number_sets.append(numbers)
    return number_sets

def find_solutions(number_set):
    solutions = []
    #unpacks variables
    x1,y1,x2,y2,Px,Py = number_set

    a, b = symbols('a b', integer=True)
    
    eq1 = Eq(x1 * a + x2 * b, Px)
    eq2 = Eq(y1 * a + y2 * b, Py)

    solutions = solve((eq1, eq2), (a, b), dict=True)
    
    return solutions

def calculate_cost_prizes(solutions):
    if not solutions:
        return None
    else:
        min_cost = float('inf')
        for sol in solutions:
            a_val, b_val = sol[a], sol[b]
            cost = 3*a_val + b_val
            if cost < min_cost:
                min_cost = cost
        prize = 1
        return min_cost, prize



if __name__ == "__main__":
    data = fetch_data('https://adventofcode.com/2024/day/13/input',"53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd")
    for number_set in data:
        solutions = find_solutions(number_set)
        if calculate_cost_prizes(solutions):
            cost,prices = calculate_cost_prizes(solutions)
            print(cost,prices)
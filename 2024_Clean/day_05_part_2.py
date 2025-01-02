"""For challenge found at https://adventofcode.com/2024/day/5"""

with open(r"input_files/day_05.txt","r") as file: # converts input into list of strings
    data = [x.strip() for x in file.readlines()]


def prep_data(data):
    """Sorts data into a dictionary of rules and a list of orders"""
    rules = {}
    orders = []
    for item in data:
        if '|' in item:
            key,value = item.split('|')
            if key in rules:
                rules[key].append(value)
            else:
                rules[key] = [value]
        if ',' in item:
            order = item.split(',')
            orders.append(order)

    return rules,orders

def order_correct(rules, order):
    """Traverses order backwards and returns false if order breaks rules"""

    order.reverse()
    for index, page in enumerate(order):
        for i in range(index+1, len(order)):
            if page in rules:
                if order[i] in rules[page]:
                    return False
    return True

def fix_order(rules,order):
    """Corrects the order based on rules"""
    left = 0
    right = 1

    while left < len(order) and right < len(order):
        if order[left] in rules[order[right]]:
            order[left], order[right] = order[right], order[left]
            if left > 0:
                left -= 1
                right -= 1
        else:
            right += 1
            left += 1
    return order


def total_middle_pages(orders,rules):
    """Traverses orders and totals middle pages"""
    
    result = 0
    for order in orders:
        if not order_correct(rules,order):
            corrected_order = fix_order(rules,order)
            index = len(corrected_order) // 2
            result += int(corrected_order[index])
    return result

rules,orders = prep_data(data)
print(total_middle_pages(orders,rules))
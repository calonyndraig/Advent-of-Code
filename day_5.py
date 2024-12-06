from pip._vendor import requests
import re

url = 'https://adventofcode.com/2024/day/5/input'

session = "53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd"
headers = {
    'Cookie': f'session={session}',
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    # The input data as text
    data = response.text
else:
    data = None

twoparts = data.split("\n\n")
rules = twoparts[0]


rules_split = rules.split("\n")

rules_dict = {}
for item in rules_split:
    nums = item.split('|')
    if not nums[0] in rules_dict:
        rules_dict[nums[0]] = [nums[1]]
    else:
        rules_dict[nums[0]].append(nums[1])

print_updates = twoparts[1]
update_rows = print_updates.split("\n")

updates_list = []
for item in update_rows:
    updates_list.append(item.split(','))
middle_pages_totaled = 0

# print(updates_list)
safe_prints_list = []
unsafe_prints_list = []
changes_count = []
for item in updates_list:
    itemflipped = item[::-1]
    update = True
    for index, page in enumerate(itemflipped):
        if page in rules_dict:
            # print(f"page in dictionary, rules = {rules_dict[page]}")
            for index in range(index+1,len(itemflipped)):
                if itemflipped[index] in rules_dict[page]:
                    # print(f"item breaks rule, {itemflipped[index]}")
                    update = False
                    break
    if update:
        safe_prints_list.append(item)
        center_item_index = len(item) // 2
        if item[center_item_index] == '':
            break
        else:
            center_item = int(item[center_item_index])
            middle_pages_totaled += center_item
    else:
        unsafe_prints_list.append(item)


def re_arrange(unsafe_list,changes=0):
    list_flipped = unsafe_list[::-1]
    changed = True
    while changed:
        changed = False
        for index, page in enumerate(list_flipped):
            if page in rules_dict:
                for sub_index in range(index+1,len(list_flipped)):
                    if list_flipped[sub_index] in rules_dict[page]:
                        list_flipped.insert(sub_index+1,page)
                        list_flipped.remove(page)
                        changed = True
                        changes += 1
                if changed:
                    break    
    changes_count.append(changes)
    center_item_index = len(list_flipped) // 2
    center_item = int(list_flipped[center_item_index])
    return center_item

rearranged_middle_pages = 0
for item in unsafe_prints_list:
    rearranged_middle_pages += re_arrange(item)

print(rearranged_middle_pages)
print(sum(changes_count))


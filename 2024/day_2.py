import requests
import time




def split_reports(data):
    report_list = []
    for line in data:
        report = line.split(' ')
        report_ints = [int(x) for x in report]
        report_list.append(report_ints)
    return report_list

def check_adjacent(report):
    for i in range(len(report)-1):
        difference = abs(report[i]-report[i+1])
        # print("Difference", difference)
        if difference  >= 1  and difference <= 3:
            continue
        else:
            return False
    return True

def check_increasing(report):
    report_increasing = sorted(report)
    if report_increasing == report:
        return True
    else:
        return False

def check_decreasing(report):
    report_decreasing = sorted(report,reverse=True)
    if report_decreasing == report:
        return True
    else: 
        return False

def check_safe(report,modified=False):
    increasing = check_increasing(report)
    decreasing = check_decreasing(report)
    adjacent = check_adjacent(report)
    # print("Increasing", increasing)
    # print("Decreasing", decreasing)
    # print("Adjacent", adjacent)
    if (increasing or decreasing) and adjacent:
        print("Is Safe")
        return True
    if not modified:
        # print("Checking modifications")
        return check_modified(report)
    else:
        return False

def check_modified(report):
    for i in range(len(report)):
        report_copy = report.copy()
        del report_copy[i]
        # print("Checking modified:", report_copy)
        mod_safe = check_safe(report_copy,modified=True)
        if mod_safe:
            # print("Modification is safe")
            return True
    return False

            




# print("Safe Reports", safereports)
            
url = 'https://adventofcode.com/2024/day/2/input'

session = "53616c7465645f5fc1fe684fb1f69a6b41ac2b62bd1750416b41a269ae6a524fc41139a82c1124eb6003e39f8fcc8be904a4994139cab73e3e065fa38ec386cd"
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

if data:
    data = data.splitlines()
reports = split_reports(data)

safe_reports = 0

for i in range(len(reports)):
    # print("Now Checking:", reports[i])
    safecheck = check_safe(reports[i])
    if safecheck:
        safe_reports += 1

print(safe_reports)

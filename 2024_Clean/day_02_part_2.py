"""For challenge found at https://adventofcode.com/2024/day/2"""

with open(r"input_files/day_02.txt") as file: #converts input into list of strings
    data = file.readlines()

def prep_data(data):
    """Converts string into lists of numbers (i.e., reports)"""

    report_list = []
    
    for item in data:
        temp_list = [int(x) for x in item.split(' ')]
        report_list.append(temp_list)
    
    return report_list

def safe_unsafe(report):
    """Marks report as either safe or unsafe"""
    
    for i in range(len(report)-1): # are report differences within specifications
        if abs(report[i+1] - report[i]) > 3 or abs(report[i+1] - report[i]) < 1:
            return False
    
    if report == sorted(report) or report == sorted(report,reverse=True): # are reports ascending or descending
        return True
    
    return False

def count_reports(report_list):
    """Counts number of safe reports in list"""

    total_count = 0
    
    for report in report_list:
        if safe_unsafe(report):
            total_count += 1
        
        else: # if not safe     
            for index in range(len(report)): # removes one element at a time
                report_copy = report[:index] + report[index+1:]
                
                if safe_unsafe(report_copy): # if safe is possible, break
                    total_count += 1
                    break
    
    return total_count

report_list = prep_data(data)
print(count_reports(report_list))
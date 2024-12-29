
with open(r"input_files/day_02.txt") as file:
    data = file.readlines()

def prep_data(data):
    report_list = []
    for item in data:
        temp_list = [int(x) for x in item.split(' ')]
        report_list.append(temp_list)
    return report_list

def safe_unsafe(report):
    for i in range(len(report)-1):
        if abs(report[i+1] - report[i]) > 3 or abs(report[i+1] - report[i]) < 1:
            return False
    if report == sorted(report) or report == sorted(report,reverse=True):
        return True
    return False

def count_reports(report_list):
    total_count = 0
    for report in report_list:
        if safe_unsafe(report):
            total_count += 1
        else:
            for index in range(len(report)):
                report_copy = report[:index] + report[index+1:]
                if safe_unsafe(report_copy):
                    total_count += 1
                    break
    return total_count

report_list = prep_data(data)
print(count_reports(report_list))
import csv
import re

with open("emp_tab.txt") as emp_file:
    strip_out = (line.strip() for line in emp_file)
    print(strip_out)
    lines = (line.split("|") for line in strip_out if line)
    lines_list = []
    for i in lines:
        for j in i:
            k = j.strip()
            if k != '':
                if re.match(r'^[^\+*.*\+*$]',k):
                    lines_list.append(k)
    print(lines_list)
    cnt = 0
    new_lis = []
    for i in lines_list:
        new_lis.append(i)
        cnt += 1
        if cnt == 5:#number of columns 
            print(new_lis)
            with open("employee_csv.csv" , mode='a') as csv_file:
                csv_read = csv.writer(csv_file)
                csv_read.writerow(new_lis)
            cnt = 0
            new_lis = []
            continue
    # for i in lines_list[0:5]:
    #     print(i)




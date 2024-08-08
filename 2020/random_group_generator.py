import csv
import random


name_list = []
with open("name_list.csv",mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
        name_list += i
#print(name_list)
name_list1 = name_list.copy()
four_groups = []
groups = []



for i in range(0,4):
    length_of_namelist = len(name_list1) // 4
    for j in range(length_of_namelist):
        name = random.choice(name_list)
        groups.append(name)
        name_list.remove(name)
        length_of_namelist -= 1
    four_groups.append(groups)
    print(four_groups[i])
    groups = []
#print(four_groups)

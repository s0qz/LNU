# salary_revision.py
#
# Author: Samuel Berg
# Date: 11-Sep-2022

from statistics import median
salaries = []
temp = input('Provide salaries: ')
salaries = temp.split(' ')
avg = 0

for i in range(len(salaries)):
    salaries[i] = int(salaries[i])
    avg += salaries[i]

avg /= len(salaries)
salaries.sort()

print('Median: ', round(median(salaries)))
print('Average: ', round(avg))
print('Gap: ', (max(salaries) - min(salaries)))

import calendar
from tabulate import tabulate

year = int(input('Введите год: '))

if calendar.isleap(year): 
    februrary = 29
else: 
    februrary = 28

rezult = 0
array = [31, februrary, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(12):
    for c in range(array[i] + 1):
        print(array[i])
        rezult += c//10 + c%10
print(rezult)

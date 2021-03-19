import re

file = open('regex_sum_1075457.txt')

arr = list()

for line in file:
    words = line.strip()
    number = re.findall('[0-9]+', words)
    if number == []: continue
    # print(number)
    for i in number: arr.append(i)
print(arr)
print(type(arr))
print(len(arr))
sum = 0
for i in arr: sum += int(i)
print(sum) 

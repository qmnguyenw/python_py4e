import re
import sys

valid_arr = []

while True:
    # input number
    number = input('Enter number: ')

    if number != 'done':
        try:
            number = int(number)
            valid_arr.append(number)
        except:
            print('Invalid Number')
    else:
        break

print('---')
print(valid_arr)
print('Num count:', len(valid_arr))
print('Sum:', sum(valid_arr))
avg = 0
try:
    avg = (sum(valid_arr)/len(valid_arr))
except:
    avg = 0
print('Average is:', avg)
import re
import sys

valid_arr = []

while True:
    # input number
    number = input('Enter number: ')

    if number != 'done':
        if len(number) == 0:
            print('No number found')
            continue
        else:
            try:
                number = int(number)
                print(number)
                valid_arr.append(number)
            except:
                print('Invalid input')
    else:
        break

print(valid_arr)
print('Maximum is', max(valid_arr))
print('Minimum is', min(valid_arr))
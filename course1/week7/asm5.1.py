count = 0
total = 0

while True:
    input_str = input('Enter Number: ')
    if input_str == 'done':
        break
            
    try:
        input_val = int(input_str)
        count += 1
        total += input_val
    except:
        print('Invalid input')
        continue

print('All Done!!!')
print(total, count, total/count)

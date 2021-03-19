# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 

def isMaxNum(arr):
    max = arr[0]
    for item in arr:
        if item > max:
            max = item
    return max

def isMinNum(arr):
    min = arr[0]
    for item in arr:
        if item < min:
            min = item
    return min

arr = []
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": 
        break
    else:
        try:
            num = int(num)
            arr.append(num)
            largest = isMaxNum(arr)
            smallest = isMinNum(arr)
            # print('ok')
        except:
            print('Invalid input')
    # print(num)

print("Maximum is", largest)
print("Minimum is", smallest)
strr = input('enter:')

strrr = strr.split(',')
arr = []
for i in range(len(strrr)):
    arr.append(int(strrr[i]))

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
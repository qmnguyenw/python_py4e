list1= input('enter list:')

listStr = list1.split(',')
listNum = []
try:
    for i in range(len(listStr)):
        listNum.append(int(listStr[i]))


    for i in range(len(listNum)):
        minIndex = i
        for j in range(i+1, len(listNum)):
            if listNum[minIndex] > listNum[j]:
                minIndex = j
        listNum[minIndex], listNum[i] = listNum[i], listNum[minIndex]

    filterList = []
    for item in listNum:
        if item not in filterList:
            filterList.append(item)

except:
    print('re-enter')

print(listNum)
print(filterList)

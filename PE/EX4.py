list1 = input('enter:')
listNum = []
list2 = list1.split(',')
for i in range(len(list2)):
    listNum.append(int(list2[i]))

listNum = sorted(listNum, reverse=True)



posStr = int(input('enter pos:'))
listNum.remove(listNum[posStr-1])

print(listNum)


sstr = input('enter:') 
ssstr = sstr[::-1]

if ssstr == sstr:
    print("bruh")
else:
    print("Lmao")


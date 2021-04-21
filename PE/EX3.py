ls = []
post1 = 0
post2 = 0


stlist = input('enter list:')
post1 = int(input('enter pos1:'))
post2 = int(input('enter pos2:'))

ls = stlist.split(',')

lsNumber = []
for i in range(len(ls)):
    lsNumber.append(int(ls[i]))

lsNumber[post1-1], lsNumber[post2-1] = lsNumber[post2-1], lsNumber[post1-1]
print(lsNumber)
lstr = "to to to to to quang quang quang phong phong"
lstr1 = lstr.split(" ")
d = {}
for i in range(len(lstr1)):
    d[lstr1[i]] = d.get(lstr1[i], 0) + 1

MostFreWord = None
MostCount = None
for Word, count in d.items():
    if MostCount is None or MostCount < count:
        MostFreWord = Word
        MostCount = count

print('Most freword:', MostFreWord)
print('Count:', MostCount)

    

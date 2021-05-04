# counts = dict()
# counts = {'key1':2, 'key4':5} # dict
# names = ['key1', 'key2', 'key4'] # list
# demo_set = {1,2,3} # set
# ar = (1,2,3,2) # tuple

# # for name in names:
# #     if name not in counts:
# #         counts[name] = 1
# #     else:
# #         counts[name] += 1

# for name in names:
#     counts[name] = counts.get(name, 0) + 1

# print(list(counts))
# print(counts.keys())
# print(counts.items())

# print(counts)


# ----

# new 
# counts = dict()
# print('Enter a line of text: ')
# line = input('')

# words = line.split()

# print('Words:', words)

# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)

# sort item in dictionary by value 
# # c1
# c = {'a': 10, 'b': 1, 'c': 22}
# tmp = list()
# for k, v in c.items():
#     list.append((v,k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)
# # c2
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# dict(sorted(x.items(), key=lambda item: item[1]))
# # c3
# text='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008\nReturn-Path: \n<postmaster@collab.sakaiproject.org>\nReceived: from stephen (stephen.marquard@uct.ac.za from Sat jan jan jan)'
# from collections import defaultdict
# d = defaultdict(int)
# for w in text.lower().split():
#     d[w] += 1
# for w in sorted(d, key=d.get, reverse=True):
#     print(w, d[w])


# the top 10 most common words 
# fhand = open('romeo.txt')
counts = {'key1':2, 'key4':5, 'key5':1}
print(counts)
# counts = dict()

# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

print(sorted([(v,k) for k,v in counts.items()]))
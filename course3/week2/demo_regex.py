import re

# hand = open('regex_sum.txt')

# # for line in hand:
# #     line = line.rstrip()
# #     if line.find('rewarding') > 0:
# #         print(line.find('rewarding'))
# #         print(line)

# for line in hand:
#     line = line.rstrip()
#     if re.search('rewarding', line):
#         print(line)

# -- 
# x = 'From: Using the things: chad'
# y = re.findall('^F.+:',x) # greedy matching
# z = re.findall('^F.+?:',x) # non-greedy matching
demo = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+',demo)
# y = re.findall('\S@\S',demo)
# y = re.findall('From (\S+@\S+)',demo) # search follow regex but only return things inside ()
# y = re.findall('@([^ ]*)',demo) # search follow regex but only return things inside ()
# y = re.findall('@([^S]*)',demo) # search follow regex but only return things inside ()
# y = re.findall('@([^S+]*)',demo) # search follow regex but only return things inside ()
# y = re.findall('^From .*@([^ ]*)',demo) # search follow regex but only return things inside ()

print(y)

# --
# file = open('course3\week2\mbox-short.txt')

# numlist = list()

# for line in file:
#     line = line.strip()
#     stuff = re.findall('([0-9.]+)', line)
#     if len(stuff) != 1: 
#         continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Max', max(numlist))


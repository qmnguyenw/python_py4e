# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name.strip(), 'r')

counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    email = line.strip().split()[1]
    counts[email] = counts.get(email, 0) + 1

print(counts)

# find the common words / max values in dictionary 
# c1: find the max value - print the item contain max value
# common_email = max(counts.values())
# key_list = list(counts.keys())
# value_list = list(counts.values())
# position = value_list.index(common_email)
# print(position)
# print(key_list[position])
# # --
# print(list(counts.keys())[list(counts.values()).index(common_email)])

# c2: tradition way
commonword_value = None
commonword_key = None
for k, v in counts.items():
    if commonword_value is None or commonword_value < v:
        commonword_value = v
        commonword_key = k

print(commonword_key, commonword_value)

# c3
# commonword_value = max(counts.values())
# commonword_key = None
# for k, v in counts.items():
#     if v == commonword_value:
#         commonword_key = k

# print(commonword_key, commonword_value)
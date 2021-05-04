fname = "mbox-short.txt"
# int variable
fh = open(fname.strip())
email_dict = dict()

# loop get email
for line in fh:
    if line.startswith('From '):
        email = line.strip().split()[1]
        email_dict[email] = email_dict.get(email, 0) + 1

# print(email_dict)

bigcount = None
bigword = None
# max frequency 
for word, count in list(email_dict.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# Show
print(bigword, bigcount)
print(bigword, 'sent the greatest number of email messages with', bigcount, ' times')
   

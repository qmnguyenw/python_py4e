# Get the name of the file and open it
# name = input('Enter file: ')
# handle = open(name, 'r')

# Sample text
handle = 'hello big boy \n new city here'

# Count word frequency
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None

for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# Show
print(bigword, bigcount)
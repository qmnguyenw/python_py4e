'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
total = 0
count = 0
fname = 'mbox-short.txt'
try:
    fh = open(fname.strip())
except:
    print('File cannot be opened:', fname)
    quit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    # sample_form = line.rstrip()
    # number_field = line.rstrip().split(' ')[1]
    number_field = line.rstrip()[line.find(' ')+1:]
    total += float(number_field)
    count += 1
    # print(number_field)
# print("Done")
print('Average spam confidence:', total/count)

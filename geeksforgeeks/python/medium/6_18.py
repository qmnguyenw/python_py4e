How to obtain the line number in which given word is present using Python?



To obtain the line number from the file where the given word is present,
create a list in which each index contains the content of each line. To do so
follow the below instruction.

First, we need a file to read from. So, create a file inside Jupiter notebook
using the magic function as shown below:

    
    
    %%writefile geeks.txt 
    Hello, I am Romy 
    I am a content writer at GfG 
    Nice to meet you 
    Hello, hii all fine
    

Or you can use any _.txt file._  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# READ FILE

df = open("geeks.txt")

 

# read file

read = df.read()

 

# return cursor to

# the beginning

# of the file.

df.seek(0)

read  
  
---  
  
 __

 __

 **Output:**

  

  

> ‘Hello, I am Romy\nI am a content writer at GfG\nNice to meet you\nHello,
> hii all fine’

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create empty list

arr = []

 

# count number of

# lines in the file

line = 1

for word in read:

 if word == '\n':

 line += 1

print("Number of lines in file is: ", line)

 

for i in range(line):

 # readline() method,

 # reads one line at

 # a time

 arr.append(df.readline())  
  
---  
  
 __

 __

 **Output:**

    
    
    Number of lines in file is: 4
    ['Hello, I am Romy\n',
    'I am a content writer at GfG\n', 
    'Nice to meet you\n',
    'Hello, hii all fine']
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Function that will return

# line in which word is present

def findline(word):

 for i in range(len(arr)):

 if word in arr[i]:

 print(i+1, end=", ")

 

 

findline("Hello")  
  
---  
  
 __

 __

 **Output:**

    
    
    1, 4
    Hello is presnt in 1st and 4th line.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


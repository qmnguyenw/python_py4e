Python – Copy contents of one file to another file



Given two text files, the task is to write a Python program to copy contents
of the first file into the second file.

The text files which are going to be used are _second.txt_ and _first.txt_ :

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201215110106/Screenshot182-660x172.png)

 **Method #1:** Using ****File handling to read and append

We will open _first.txt_ in _‘r’_ mode __ and will read the contents of
_first.txt._ After that, we will open _second.txt_ in ‘a’ mode and will append
the content of _first.txt_ into _second.txt_.

  

  

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# open both files

with open('first.txt','r') as firstfile,
open('second.txt','a') as secondfile:

 

 # read content from first file

 for line in firstfile:

 

 # append content to second file

 secondfile.write(line)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201215110825/Screenshot183-660x171.png)

 **Method #2:** Using ****File handling to read and write

We will open _first.txt_ in _‘r’_ mode __ and will read the contents of
_first.txt._ After that, we will open _second.txt_ in ‘w’ mode and will write
the content of _first.txt_ into _second.txt_.

 **Example:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# open both files

with open('first.txt','r') as firstfile,
open('second.txt','a') as secondfile:

 

 # read content from first file

 for line in firstfile:

 

 # write content to second file

 secondfile.write(line)  
  
---  
  
 __

 __


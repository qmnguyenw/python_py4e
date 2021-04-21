Python program to copy odd lines of one file to other



Write a python program to read contents of a file and copy only the content of
odd lines into new file.

 **Examples:**

    
    
    **Input :** Hello
            World
            Python
            Language
    **Output :** Hello
             Python
    
    **Input :** Python
            Language
            Is
            Easy
    **Output :** Python
             Is
    

### Approach to the problem

 **1)** Open file name bcd.txt in read mode and assign it to fn.  
 **2)** Open file name nfile.txt in write mode and assign it to fn1.  
 **3)** Read the content line by line of the file fn and assign it to cont.  
 **4)** Access each element from 0 to length of cont.  
 **5)** Check if i is not divisible by 2 then write the content in fn1 else
pass.  
 **6)** Close the file fn1.  
 **7)** Now open nfile.txt in read mode and assign it to fn1.  
 **8)** Read the content of the file and assign it to cont1.  
 **9)** Print the content of the file and then close the file fn and fn1 .

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# open file in read mode

fn = open('bcd.txt', 'r')

 

# open other file in write mode

fn1 = open('nfile.txt', 'w')

 

# read the content of the file line by line

cont = fn.readlines()

type(cont)

for i in range(0, len(cont)):

 if(i % 2 ! = 0):

 fn1.write(cont[i])

 else:

 pass

 

# close the file

fn1.close()

 

# open file in read mode

fn1 = open('nfile.txt', 'r')

 

# read the content of the file

cont1 = fn1.read()

 

# print the content of the file

print(cont1)

 

# close all files

fn.close()

fn1.close()  
  
---  
  
 __

 __

    
    
    **Output :** Python
             Is
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save


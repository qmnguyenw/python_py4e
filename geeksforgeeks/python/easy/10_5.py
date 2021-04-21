Python program to reverse the content of a file and store it in another file



Given a text file. The task is to reverse as well as stores the content from
an input file to an output file.  
This reversing can be performed in two types.

  * **Full reversing:** In this type of reversing all the content gets reversed.   

  * **Word to word reversing:** In this kind of reversing the last word comes first and the first word goes to the last position.   

**Example 1:** Full Reversing  

    
    
    **Input:** Hello Geeks
           for geeks!
            
    
    **Output:**!skeeg rof
            skeeG olleH
            
    
    
    

**Example 2:** Word to word reversing  

    
    
    **Input:** 
            Hello Geeks
            for geeks!
    
    **Output:**
             geeks! for
             Geeks Hello
    
    
    

**Example 1:** Full Reversing  
**Text file:**  

![python-reverse-file-input](https://media.geeksforgeeks.org/wp-
content/uploads/20200115173039/python-reverse-file-input.png)

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Open the file in write mode

f1 = open("output1.txt", "w")

 

# Open the input file and get 

# the content into a variable data

with open("file.txt", "r") as myfile:

 data = myfile.read()

 

# For Full Reversing we will store the 

# value of data into new variable data_1 

# in a reverse order using [start: end: step],

# where step when passed -1 will reverse 

# the string

data_1 = data[::-1]

 

# Now we will write the fully reverse 

# data in the output1 file using 

# following command

f1.write(data_1)

 

f1.close()  
  
---  
  
 __

 __

 **Output:**  

![python-reverse-file-output-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200115173210/python-reverse-file-output-1.png)

**Example 2:** Reversing the order of lines. We will use the above text file
as input.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Open the file in write mode

f2 = open("output2.txt", "w")

 

 

# Open the input file again and get 

# the content as list to a variable data

with open("file.txt", "r") as myfile:

 data = myfile.readlines()

 

# We will just reverse the 

# array using following code

data_2 = data[::-1]

 

# Now we will write the fully reverse 

# list in the output2 file using 

# following command

f2.writelines(data_2)

 

f2.close()  
  
---  
  
 __

 __

 **Output:**  

![python-reverse-file-output-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200115173434/python-reverse-file-output-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


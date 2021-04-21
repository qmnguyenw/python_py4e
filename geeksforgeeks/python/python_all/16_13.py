Python program to capitalize the first letter of every word in the file



The following article contains programs to read a file and capitalize the
first letter of every word in the file and print it as output. To capitalize
the first letter we will use the **title() function** in python. The title
function in python is the Python String Method which is used to convert the
first character in each word to Uppercase and the remaining characters to
Lowercase in the string and returns the new string.

 **Examples:**

    
    
    # Content of the file serves as input
    **Input:** hello world
    **Output:** Hello World
    
    # Content of the file serves as input
    **Input:** geeks for geeks
    **Output:** Geeks For Geeks
    

**Approach:**

  * We will take the content of the file as input.
  * We will open the file and save its content by using the **open() function** in python.
  * Printing the content after altering it.

 **Input File:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201114115035/Screenshot20201114115013-660x401.jpg)

Content of the gfg.txt file

Below is the Implementation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to read a file and capitalize

# the first letter of every word in the file.

 

# A file named "gfg", will be opened with the 

# reading mode. 

file_gfg = open('gfg.txt', 'r')

 

# This will traverse through every line one by one

# in the file

for line in file_gfg:

 

 # This will convert the content

 # of that line with capitalized

 # first letter of every word

 output = line.title()

 

 # This will print the output

 print(output)  
  
---  
  
 __

 __

 **Output:**

> Geeksforgeeks Is A Computer Science Portal For Geeks. It Contains Well
> Written, Well Thought And Well Explained Computer Science And Programming
> Articles, Quizzes Etc.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


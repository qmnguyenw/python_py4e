Python program to read character by character from a file



Given a text file. The task is to read the text from the file character by
character.

 **Function used:**

>  **Syntax:** file.read(length)
>
>  **Parameters:** An integer value specified the lenght of data to be read
> from the file.
>
>  **Return value:** Returns the read bytes in form of a string.
>
>  
>
>
>  
>

 **Examples 1:** Suppose the text file looks like this.

![pythonfile-input1](https://media.geeksforgeeks.org/wp-
content/uploads/20200115193150/python-reverse-file-input1.png)

 __

 __  
 __

 __

 __  
 __  
 __

# Demonstrated Python Program

# to read file character by character

 

 

file = open('file.txt', 'r')

 

while 1:

 

 # read by character

 char = file.read(1) 

 if not char: 

 break

 

 print(char)

 

file.close()  
  
---  
  
 __

 __

 **Output**

![python-read-character](https://media.geeksforgeeks.org/wp-
content/uploads/20200115193650/python-read-character-output-2.png)

 **Example 2:** REading more than one charactes at a time.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Read character by character

 

 

with open('file.txt') as f:

 

 while True:

 

 # Read from file 

 c = f.read(5)

 if not c:

 break

 

 # print the character

 print(c)  
  
---  
  
 __

 __

 **Output**

![python-read-character-by-character-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200115193508/python-read-character-by-character-1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


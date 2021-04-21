Count number of lines in a text file in Python



 **Prerequisites:** File Handling in Python

Counting the number of characters is important because almost all the text
boxes that rely on user input have a certain limit on the number of characters
that can be inserted. For example, the character limit on a Facebook post is
63, 206 characters. Whereas, for a tweet on Twitter the character limit is 140
characters and the character limit is 80 per post for Snapchat.

This program in Data file handling in Python emphasizes the counting the
number of lines in a text file in Python.

 **Approach:**

  * Open the file in read mode and assign a file object named “file”.
  * Assign 0 to the counter variable.
  * Read the content of the file using **read** function and assign it to a variable named “Content”.
  * Create a list of the Content where the elements are split wherever they encounter an “\n”.
  * Traverse the list using a for loop and iterate the Counter variable respectively.
  * Further the value now present in the variable Counter is displayed which is the required action in this program.

 **Below is the implementation.**

  

  

Let’s suppose the text file looks like this –

![python-count-line](https://media.geeksforgeeks.org/wp-
content/uploads/20200217193402/python-count-line.png)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count the

# number of lines in a text file

 

 

# Opening a file

file = open("gfg.txt","r")

Counter = 0

 

# Reading from file

Content = file.read()

CoList = Content.split("\n")

 

for i in CoList:

 if i:

 Counter += 1

 

print("This is the number of lines in the file")

print(Counter)  
  
---  
  
 __

 __

 **Output:**

    
    
    This is the number of lines in the file
    4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Create an empty text file with current date as its name



In this article, we will learn how to create a text file names as the current
date in it. For this, we can use now() method of datetime module.

The datetime module supplies classes for manipulating dates and times in both
simple and complex ways. While date and time arithmetic is supported, the
focus of the implementation is on efficient attribute extraction for output
formatting and manipulation.

Let’s see a code example and try to understand it better.

 __

 __  
 __

 __

 __  
 __  
 __

# Python script to create an empty file

# with current date as name.

 

# importing datetime module

import datetime

 

# datetime.datetime.now() to get 

# current date as filename.

filename = datetime.datetime.now()

 

# create empty file

def create_file():

 # Function creates an empty file

 # %d - date, %B - month, %Y - Year

 with open(filename.strftime("%d %B %Y")+".txt", "w") as
file:

 file.write("")

 

# Driver Code

create_file()  
  
---  
  
 __

 __

 **Output:**

    
    
    01 August 2019.txt

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


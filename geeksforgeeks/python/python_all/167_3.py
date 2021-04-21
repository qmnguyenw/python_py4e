Rename all file names in your directory using Python



Given multiple files in a directory having different names, the task is to
rename all those files in sorted order.

We can use OS module in order to do this operation. The OS module in python
provides functions for interacting with the operating system and provides a
portable way of using operating system dependent functionality. We can go to
the current working directory using os.getcwd() method and rename the files
with os.rame() method.

Below is the Python implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to rename all file

# names in your directory 

import os

 

os.chdir('D://Geeksforgeeks')

print(os.getcwd())

COUNT = 1

 

# Function to increment count 

# to make the files sorted.

def increment():

 global COUNT

 COUNT = COUNT + 1

 

 

for f in os.listdir():

 f_name, f_ext = os.path.splitext(f)

 f_name = "geek" + str(COUNT)

 increment()

 

 new_name = '{} {}'.format(f_name, f_ext)

 os.rename(f, new_name)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/old_name.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


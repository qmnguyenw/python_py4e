How to check file size in Python?



 **Prerequisites:**

  * os 
  * pathlib

Given a file, the task here is to generate a Python Script to print its size.
This article explains 2 methods to do so.

###  **Approach**

  * Import module
  * Get file size

###  **File in use**

 **Name:** Data.csv

 **Size:** 226 bytes

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201212141142/5-660x489.JPG)

  

  

 **Method1: Using pathlib**

Path().stat().st_size() function of pathlib module gets the size of any type
of the file and the output of this function will be the size of the file in
bytes.

 **Syntax:**

    
    
    Path('filename').stat().st_size()

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from pathlib import Path

 

sz = Path('Data.csv').stat().st_size

 

print(sz)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201204174604/55-660x243.JPG)

 **Method 2: With Os module**

  

  

os.path.getsize() function only works with os Library, with the help of
importing this library we can use this to get the size of any type of file and
the output of this function will be the size of the file in bytes.

 **Syntax:**

    
    
    getsize(filename)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

sz = os.path.getsize("Data.csv")

 

print(sz)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201212143253/5-660x180.JPG)

We got the result as 226 bytes

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


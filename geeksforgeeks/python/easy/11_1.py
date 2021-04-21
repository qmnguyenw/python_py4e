Python File truncate() Method



 **Prerequisites:**

  * File Objects in Python
  * Reading and Writing to files in Python

Truncate() method truncate the file’s size. If the optional size argument is
present, the file is truncated to (at most) that size. The size defaults to
the current position. The current file position is not changed. Note that if a
specified size exceeds the file’s current size, the result is platform-
dependent: possibilities include that the file may remain unchanged, increase
to the specified size as if zero-filled, or increase to the specified size
with undefined new content.  
To truncate the file, you can open the file in append mode or write mode.

 **Syntax:**

    
    
    fileObject.truncate(size)
    

**Example:**  
See the below image for file size.

![Python-truncate-input](https://media.geeksforgeeks.org/wp-
content/uploads/20191125171504/Python-truncate-input.png)

  

  

Let’s change the file size to 100 bytes.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# truncate() method

 

fp = open('file1.txt', 'w')

 

# Truncates the file to specified

# size

fp.truncate(100)

 

# Closing files

fp.close()  
  
---  
  
 __

 __

 **Output:**

![python-truncate-output](https://media.geeksforgeeks.org/wp-
content/uploads/20191125171923/python-truncate-output.png)

#### With statement

In the above approaches, every time the file is opened it is needed to be
closed explicitly. If one forgets to close the file, it may introduce several
bugs in the code, i.e. many changes in files do not go into effect until the
file is properly closed. To prevent this with statement can be used. with
statement in Python is used in exception handling to make the code cleaner and
much more readable. It simplifies the management of common resources like file
streams. Observe the following code example on how the use of with statement
makes code cleaner. There is no need to call file.close() when using with
statement. The with statement itself ensures proper acquisition and release
of resources.

Let’s change the above file to 50 bytes

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# truncate method using with statement

 

with open('file1.txt', 'w') as fp:

 fp.truncate(50)  
  
---  
  
 __

 __

 **Output:**  
![python-truncate-output](https://media.geeksforgeeks.org/wp-
content/uploads/20191125172347/python-truncate-output-2.png)

 **Note:** To know more about with statement click here.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


How to delete data from file in Python



When we no longer require data, we usually prefer to erase or delete it so
that space can be used up by other data that is important to us. Python too
supports file handling and allows users to handle files i.e., to read and
write files, along with many other file handling options, to operate on files.

>  **Refer to the below articles to get the idea about file handling in
> Python.**
>
>   * File Handling in Python
>   * Reading and Writing to text files in Python
>

Here, we will be learning different approaches that are used while deleting
data from the file in Python.

 **Method 1: When the entire data along with the file, it is in, has to be
deleted!**

os.remove() method in Python is used to remove or delete a file path. This
method can not remove or delete a directory. If the specified path is a
directory then OSError will be raised by the method. os.rmdir() can be used to
remove directory.

  

  

 **Example:**

 **Before execution:**

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200116225251/gfg-delete-1-before.jpg)

 __

 __  
 __

 __

 __  
 __  
 __

# code to delete entire data along with file

import os

 

# check if file exists

if os.path.exists("sample.txt"):

 os.remove("sample.txt")

 

 # Print the statement once

 # the file is deleted 

 print("File deleted !") 

 

else:

 

 # Print if file is not present 

 print("File doesnot exist !")   
  
---  
  
__

__

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200116225653/gfg-delete-1.jpg)

**After execution:**

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200116225749/gfg-delete-1-after.jpg)

 **Note:** For more information, refer to Python | os.remove() method

 **Method 2: When the entire data has to be deleted but not the file it is in
!**

  

  

Truncate() method truncate the file’s size. If the optional size argument is
present, the file is truncated to (at most) that size. The size defaults to
the current position. The current file position is not changed. Note that if a
specified size exceeds the file’s current size, the result is platform-
dependent: possibilities include that the file may remain unchanged, increase
to the specified size as if zero-filled, or increase to the specified size
with undefined new content. To truncate the file, you can open the file in
append mode or write mode.

 **Example:**

 **Before execution:**

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200116231519/gfg-delete-2-before.jpg)

 __

 __  
 __

 __

 __  
 __  
 __

# code to delete entire data

# but not the file, it is in

 

 

# open file 

f = open("sample.txt", "r+") 

 

# absolute file positioning

f.seek(0) 

 

# to erase all data 

f.truncate()   
  
---  
  
__

__

**Output:**

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200116233223/gfg-delete-2.jpg)

 **After execution:**

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200116233256/gfg-delete-2-after.jpg)

 **Note:** For more information, refer to Python File truncate() Method.

 **Method 3: Delete a particular data from the file**

This can be done by following ways:

  1. Open file in read mode, get all the data from the file. Reopen the file again in write mode and write all data back, except the data to be deleted
  2. Rewrite file in a new file except for the data we want to delete. faster)

Let us see the first one.

 **Example:**

 **Before execution:**

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200116235201/gfg-delete-2-before1.jpg)

 __

 __  
 __

 __

 __  
 __  
 __

# code to delete a particular

# data from a file

 

# open file in read mode

with open("sample.txt", "r") as f:

 

 # read data line by line 

 data = f.readlines()

 

# open file in write mode

with open("sample.txt", "w") as f:

 

 for line in data :

 

 # condition for data to be deleted

 if line.strip("\n") != "Age : 20" : 

 f.write(line)  
  
---  
  
 __

 __

 **Output:**

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200117014714/gfg-delete-3.jpg)

 **After execution:**

![python-delete-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200117014746/gfg-delete-3-after.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


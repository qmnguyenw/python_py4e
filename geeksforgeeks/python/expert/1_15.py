Python – os.replace() method



 **Prerequisite:** OS module in Python.

 **os.replace()** method in Python is used to rename the file or directory. If
destination is a directory, **OSError** will be raised. If the destination
exists and is a file, it will be replaced without error if the action
performing user has permission. This method may fail if the source and
destination are on different filesystems.

>  **Syntax:** os.replace(source, destination, *, src_dir_fd=None,
> dst_dir_fd=None2)
>
>  **Parameter:**
>
>   *  **source:** Name of file or directory which we want to rename.
>   *  **destination:** Name which we want to give in destination.
>   *  **src_dir_id :** This parameter stores the source directory’s or file,  
>  file descripter referring to a directory.
>   *  **dst_dir_fd:** It is a file descriptor referring to a directory,  
>  and the path to operate. It should be relative,  
>  path will then be relative to that directory. If  
>  the path is absolute, dir_fd is ignored.
>

>
>  **Return Type:** This method does not return any value.
>
>  
>
>
>  
>

 **Code #1** : Use of os.replace() method to rename a file.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.replace() method

# importing os module

import os

# file name

file = "f.txt"

# File location which to rename

location = "d.txt"

# Path

path = os.replace(file, location)

# renamed the file f.txt to d.txt

print("File %s is renamed successfully" % file)  
  
---  
  
 __

 __

 **Output:**

    
    
    File f.txt is renamed successfully

 **Code #2** : Handling possible erros. (If necessary permissions are given
then output will be as shown in below)

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.replace() method

# importing os module

import os

# Source file path

source = './file.txt'

# destination file path

dest = './da'

# try renaming the source path

# to destination path

# using os.rename() method

try:

 os.replace(source, dest)

 print("Source path renamed to destination path successfully.")

# If Source is a file

# but destination is a directory

except IsADirectoryError:

 print("Source is a file but destination is a directory.")

# If source is a directory

# but destination is a file

except NotADirectoryError:

 print("Source is a directory but destination is a file.")

# For permission related errors

except PermissionError:

 print("Operation not permitted.")

# For other errors

except OSError as error:  
  
---  
  
 __

 __

 **Output:**

    
    
    Source is a file but destination is a directory.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


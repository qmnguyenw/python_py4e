Delete a directory or file using Python



Python provides different methods and functions for removing files and
directories. One can remove the file according to their need. Various methods
provided by Python are –

  * Using os.remove()
  * Using os.rmdir()
  * Using shutil.rmtree()

## Using os.remove()

 **OS module** in Python provides functions for interacting with the operating
system. All functions in os module raise **OSError**in the case of invalid
or inaccessible file names and paths, or other arguments that have the correct
type, but are not accepted by the operating system.

os.remove() method in Python is used to remove or delete a file path. This
method **can not remove or delete a directory**. If the specified path is a
directory then OSError will be raised by the method.

>  **Syntax:** os.remove(path, *, dir_fd = None)
>
>  **Parameter:**  
>  **path:** A path-like object representing a file path. A path-like object
> is either a string or bytes object representing a path.  
>  **dir_fd (optional):** A file descriptor referring to a directory. The
> default value of this parameter is None.  
> If the specified path is absolute then dir_fd is ignored.
>
>  
>
>
>  
>
>
>  **Note:** The ‘*’ in parameter list indicates that all following parameters
> (Here in our case ‘dir_fd’) are keyword-only parameters and they can be
> provided using their name, not as positional parameter.
>
>  **Return Type:** This method does not return any value.

 **Example 1:** Suppose the file contained in the folder are:  
![python-os.remove](https://media.geeksforgeeks.org/wp-
content/uploads/20191125183910/python-os.remove-input.png)

We want to delete the file1 from the above folder. Below is the
implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.remove() method

 

# importing os module 

import os 

 

# File name 

file = 'file1.txt'

 

# File location 

location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"

 

# Path 

path = os.path.join(location, file) 

 

# Remove the file 

# 'file.txt' 

os.remove(path)   
  
---  
  
__

__

**Output:**  
![python-os.remove](https://media.geeksforgeeks.org/wp-
content/uploads/20191125184203/python-os.remove-output.png)

 **Example 2:** If the specified path is a directory.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.remove() method

 

# importing os module 

import os 

 

# Directory name

dir = "Nikhil"

 

# Path 

location = "D:/Pycharm projects/GeeksforGeeks/Authors/"

path = os.path.join(location, dir)

 

# Remove the specified 

# file path 

os.remove(path) 

print("% s has been removed successfully" % dir) 

 

# if the specified path 

# is a directory then 

# 'IsADirectoryError' error 

# will raised 

 

# Similarly if the specified 

# file path does not exists or 

# is invalid then corresponding 

# OSError will be raised   
  
---  
  
__

__

**Output:**

    
    
    Traceback (most recent call last):
      File "osremove.py", line 11, in 
        os.remove(path)
    IsADirectoryError: [Errno 21] Is a directory: 'D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil'
    

**Example 3:** Handling error while using os.remove() method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.remove() method

 

# importing os module 

import os 

 

# path 

path = 'D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil'

 

# Remove the specified 

# file path 

try: 

 os.remove(path) 

 print("% s removed successfully" % path) 

except OSError as error: 

 print(error) 

 print("File path can not be removed")   
  
---  
  
__

__

**Output:**

    
    
    [Errno 21] Is a directory: 'D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil'
    File path can not be removed
    

**Note:** To know more about os.remove() click here.

## Using os.rmdir()

os.rmdir() method in Python is used to remove or delete a empty directory.
**OSError **will be raised if the specified path is not an empty directory.

>  **Syntax:** os.rmdir(path, *, dir_fd = None)
>
>  **Parameter:**  
>  **path:** A path-like object representing a file path. A path-like object
> is either a string or bytes object representing a path.  
>  **dir_fd (optional):** A file descriptor referring to a directory. The
> default value of this parameter is None.  
> If the specified path is absolute then dir_fd is ignored.
>
>  **Note:** The ‘*’ in parameter list indicates that all following parameters
> (Here in our case ‘dir_fd’) are keyword-only parameters and they can be
> provided using their name, not as positional parameter.
>
>  **Return Type:** This method does not return any value.

 **Example 1:** Suppose the directories are –

![python-os.rmdir](https://media.geeksforgeeks.org/wp-
content/uploads/20191125192432/python-os.rmdir-input.png)

We want to remove the directory Geeks. Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.rmdir() method

 

# importing os module 

import os 

 

# Directory name 

directory = "Geeks"

 

# Parent Directory 

parent = "D:/Pycharm projects/"

 

# Path 

path = os.path.join(parent, directory) 

 

# Remove the Directory 

# "Geeks" 

os.rmdir(path)   
  
---  
  
__

__

**Output:**

![python-os.rmdir](https://media.geeksforgeeks.org/wp-
content/uploads/20191125192658/python-os.rmdir-output.png)

 **Example 2:** Handling errors while using os.rmdir() method,

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.rmdir() method

 

# importing os module 

import os

 

# Directory name 

directory = "GeeksforGeeks"

 

# Parent Directory 

parent = "D:/Pycharm projects/"

 

# Path 

path = os.path.join(parent, directory)

 

# Remove the Directory

# "GeeksforGeeks"

try:

 os.rmdir(path)

 print("Directory '% s' has been removed successfully" %
directory)

except OSError as error:

 print(error)

 print("Directory '% s' can not be removed" % directory)

 

# if the specified path

# is not an empty directory 

# then permission error will 

# be raised 

 

# similarly if specified path 

# is invalid or is not a 

# directory then corresponding 

# OSError will be raised   
  
---  
  
__

__

**Output:**

    
    
    [WinError 145] The directory is not empty: 'D:/Pycharm projects/GeeksforGeeks'
    Directory 'GeeksforGeeks' can not be removed
    

**Note:** To know more about os.rmdir() click here.

## Using shutil.rmtree()

shutil.rmtree() is used to delete an entire directory tree, path must point to
a directory (but not a symbolic link to a directory).

>  **Syntax:** shutil.rmtree(path, ignore_errors=False, onerror=None)
>
>  **Parameters:**  
>  **path:** A path-like object representing a file path. A path-like object
> is either a string or bytes object representing a path.  
>  **ignore_errors:** If ignore_errors is true, errors resulting from failed
> removals will be ignored.  
>  **oneerror:** If ignore_errors is false or omitted, such errors are handled
> by calling a handler specified by onerror.

 **Example 1:** Suppose the directory and sub-directories are as follow.

 **# Parent directory:**  
![python-shutil.rmtree](https://media.geeksforgeeks.org/wp-
content/uploads/20191125194649/python-shutil.rmtree-input1.png)

 **# Directory inside parent directory:**  
![python-shutil.rmtree](https://media.geeksforgeeks.org/wp-
content/uploads/20191125194719/python-shutil.rmtree-input2.png)

 **# File inside the sub-directory:**  
![python-shutil.rmtree](https://media.geeksforgeeks.org/wp-
content/uploads/20191125194750/python-shutil.rmtree-input3.png)

We want to remove the directory Authors. Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# shutil.rmtree()

 

import shutil

import os

 

# location

location = "D:/Pycharm projects/GeeksforGeeks/"

 

# directory

dir = "Authors"

 

# path

path = os.path.join(location, dir)

 

# removing directory

shutil.rmtree(path)  
  
---  
  
 __

 __

 **Output:**

![python-shutil.rmtree](https://media.geeksforgeeks.org/wp-
content/uploads/20191125195230/python-shutil.rmtree-output.png)

 **Example 2:** By passing ignore_errors = True.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# shutil.rmtree()

 

import shutil

import os

 

# location

location = "D:/Pycharm projects/GeeksforGeeks/"

 

# directory

dir = "Authors"

 

# path

path = os.path.join(location, dir)

 

# removing directory

shutil.rmtree(path, ignore_errors = False)

 

# making ignore_errors = True will not raise 

# a FileNotFoundError  
  
---  
  
 __

 __

 **Output:**

> Traceback (most recent call last):  
> File “D:/Pycharm projects/gfg/gfg.py”, line 16, in  
> shutil.rmtree(path, ignore_errors=False)  
> File “C:\Users\Nikhil
> Aggarwal\AppData\Local\Programs\Python\Python38-32\lib\shutil.py”, line 730,
> in rmtree  
> return _rmtree_unsafe(path, onerror)  
> File “C:\Users\Nikhil
> Aggarwal\AppData\Local\Programs\Python\Python38-32\lib\shutil.py”, line 589,
> in _rmtree_unsafe  
> onerror(os.scandir, path, sys.exc_info())  
> File “C:\Users\Nikhil
> Aggarwal\AppData\Local\Programs\Python\Python38-32\lib\shutil.py”, line 586,
> in _rmtree_unsafe  
> with os.scandir(path) as scandir_it:  
> FileNotFoundError: [WinError 3] The system cannot find the path specified:
> ‘D:/Pycharm projects/GeeksforGeeks/Authors’

 **Example 3:** By passing onerror  
In onerror a function should be passed which must contain three parameters.

  *  **function –** function which raised the exception.
  *  **path –** path name passed which raised the exception while removal
  *  **excinfo –** exception info raised by sys.exc_info()

Below is the implementation

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# shutil.rmtree()

 

import shutil

import os

 

 

# exception handler

def handler(func, path, exc_info):

 print("Inside handler")

 print(exc_info)

 

 

# location

location = "D:/Pycharm projects/GeeksforGeeks/"

 

# directory

dir = "Authors"

 

# path

path = os.path.join(location, dir)

 

# removing directory

shutil.rmtree(path, onerror = handler)  
  
---  
  
 __

 __

 **Output:**

> Inside handler  
> (, FileNotFoundError(2, ‘The system cannot find the path specified’), )  
> Inside handler  
> (, FileNotFoundError(2, ‘The system cannot find the file specified’), )

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


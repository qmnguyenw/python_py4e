How to print all files within a directory using Python?



In this article, we will learn “How to print all files within a directory
using Python?”. To do this task we are using the os module in Python. So,
let’s discuss some concepts related to that.

The os module is one of the most popular Python modules for automating the
systems calls and operations of an operating system. With a rich set of
methods and an easy-to-use API, the os module is one of the standard packages
and comes pre-installed with Python.

For this article, the following methods from the os module will be required:

 **1\. os.startfile():** This method prints the contents of a given file.

>  **Syntax:** os.startfile(path, operation=’open’)
>
>  
>
>
>  
>
>
>  **Parameters:**
>
>   *  **path –** String containing the path to a given file
>   *  **operation –** A string containing one of the following **‘command
> verbs’**
>     *  **‘print’** **–** Prints the file pertaining to path
>     *  **‘edit’ –** Opens the file in the default text-editor for editing
>     *  **‘properties’ –** Opens the properties window of the given file
>     *  **‘find’ –** Initiates a search starting from directory mentioned in
> the path
>     *  **‘open’** – Opens the application/file pertaining to the path. If
> the given file is not an executable file, its associated application is
> opened
>

 **2\. os.listdir():** This method lists all the files and directories within
a given directory. For more detailed coverage of this method consisting of
examples and use-cases, please refer here.

>  **Syntax:** _os.listdir(path=’.’)_
>
>  _ **Parameters:**_
>
>   *  _ **path** **–** String containing the path of the directory containing
> the files to be printed_
>

>
>  _ **Returns:**_ A list containing the names of all the sub -directories and
> files present in the corresponding directory.

 **3\. os.path.isfile()** : As we can only print the given folder’s
subdirectories, we’ll use this method to check if a given entity is either a
file or a directory. For more detailed coverage of this method consisting of
examples and use cases, please refer here.

>  **Syntax:** os.path.isfile(path)
>
>  **Parameters:**
>
>   *  **path –** String containing the path of the entity being checked
>

>
>  **Returns: True** if path coresponds to a file, else returns **False**

 **Note:** Aside from the above modules, you’ll also need a fully functional
printer connected to your PC!

  

  

 **Implementation**

The line of code “time.sleep(5)” of the given script is completely optional
and is just there to avoid any un-necessary glitching or overlapping of the
operations in consecutive files. For reading more about the time.sleep()
method, please refer to here.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Import libraries

import os

import time

 

# Insert the directory path in here

path = ''

 

# Extracting all the contents in the directory corresponding to path

l_files = os.listdir(path) 

 

# Iterating over all the files

for file in l_files:

 

 # Instantiating the path of the file

 file_path = f'{path}\\{file}'

 

 # Checking whether the given file is a directory or not

 if os.path.isfile(file_path):

 try:

 # Printing the file pertaining to file_path

 os.startfile(file_path, 'print')

 print(f'Printing {file}')

 

 # Sleeping the program for 5 seconds so as to account the 

 # steady processing of the print operation.

 time.sleep(5)

 except:

 # Catching if any error occurs and alerting the user

 print(f'ALERT: {file} could not be printed! Please check\

 the associated softwares, or the file type.')

 else:

 print(f'ALERT: {file} is not a file, so can not be printed!')

 

print('Task finished!')  
  
---  
  
 __

 __

 **Output:**

The demo was done on a Windows 10 machine. The environment is as follows:

  * Path of the directory containing files being printed: “Local Disk (D):/Files”
  * Files in the given directory:
    *  **Dir** **–** A sample subdirectory
    *  **File_a.pdf –** A sample .pdf file
    *  **File_b.txt –** A sample .txt file
    *  **File_c.docx –** A sample .docx file

https://media.geeksforgeeks.org/wp-
content/uploads/20210209153545/PrintingFilesUsingPythonDemo.mp4

 **Note:** Since os.startfile() is only available in Windows operating system,
so macOS and Linux users might experience some issues while running the script
given in the article.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


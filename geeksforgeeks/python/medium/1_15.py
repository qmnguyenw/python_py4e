Python – Loop through files of certain extensions



A directory is capable of storing multiple files and python can support
mechanism to loop over them. In this article we will see different methods to
iterate over certain files in a given directory or subdirectory.

 **Path containing different files:** This will be used for all methods.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210130153033/fff11-660x524.JPG)

 **Method 1: Using** **listdir()**

In this method we will use **os.listdir()** function which is in the os
library. This function returns a list of names of files present in the
directory and in no order.

  

  

So to get specific type of file from a particular directory we need to iterate
through the directory and subdirectory and print the file with specific
extension.

 **Syntax:**

> listdir(path)

 **Approach**

  * Import the os library and pass the directory in the os.listdir() function.
  * Create a tuple having the extensions that you want to fetch.
  * Through a loop iterate over all the files in the directory an print the file having particular extension.
  * The endswith() function checks if the file ends that particular extension or not is its does then it prints the file name.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the library

import os

 

# giving directory name

dirname = 'D:\\AllData'

 

# giving file extension

ext = ('.exe', 'jpg')

 

# iterating over all files

for files in os.listdir(dirname):

 if files.endswith(ext):

 print(files) # printing file name of desired extension

 else:

 continue  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210130144858/file2.JPG)

  

  

 **Method 2: Using** **scandir()**

This method uses **os.scandir()** function returns an iterator that is used to
access the file. The entries are yielded in arbitrary order. It lists the
directories or files immediately under that directory.

 **Syntax:**

> scandir(path)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import os

 

# directory name

dirname = 'D:\\AllData'

 

# extensions

ext = ('.exe', 'jpg')

 

# scanning the directory to get required files

for files in os.scandir(dirname):

 if files.path.endswith(ext):

 print(files) # printing file name  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210204171405/vv1.JPG)

 **Method 3: Using** **walk()**

In this method we will use the **os.walk()** function which yields us three
tuples namely:-(dirpath, dirnames, filenames). Since, it is a recursive
process it will iterate over all descendant files in subdirectories and prints
the file name. Further approach is same as above method.

 **Syntax:**

> walk(path)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import os

 

# giving directory name

folderdir = 'D:\\AllData'

 

# giving file extensions

ext = ('.pdf', '.mkv')

 

# iterating over directory and subdirectory to get desired result

for path, dirc, files in os.walk(folderdir):

 for name in files:

 if name.endswith(ext):

 print(name) # printing file name  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210130151205/f3.JPG)

 **Method 4: Using** **glob**

In this method we will use the glob.iglob() function which comes under the
glob library. Glob is a general term used to define techniques to match
specified patterns according to rules related to Unix shell. Linux and Unix
systems and shells also support glob and also provide function glob() in
system libraries.

In Python, the glob module is used to retrieve files/pathnames matching a
specified pattern. The glob function accepts the directory/path and the
\\\\**\\\ pattern tells to look for the files with specific extension in
subfolders also that needs to be recursive process so recursive should be set
to True.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import glob

 

# accesing and printing files in directory and subdirectory

for filename in glob.glob('D:\\AllData\\**\\*.exe',
recursive=True):

 print(filename) # print file name  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210130153128/ot1.JPG)

 **Method 5: Using path()**

This method uses the **Path()** function from the **pathlib** module. The path
function accepts the directory name as argument and in glob function ‘**/*’
pattern is used to find files of specific extensions. It is also recursive
function and lists all file of same directory and sub-directory.

 **Syntax:**

> path(path)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

from pathlib import Path

 

# directory name

dirname = 'D:\\AllData'

 

# giving directory name to Path() function

paths = Path(dirname).glob('**/*.exe',)

 

# iterating over all files

for path in paths:

 print(path) # printing file name  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210204172537/vv2.JPG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


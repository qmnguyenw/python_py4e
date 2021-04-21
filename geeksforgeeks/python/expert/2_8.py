List all files of certain type in a directory using Python



In python, there are several built-in modules and methods for file handling.
These functions are present in different modules such as os, glob etc. This
article helps you find out many of the functions in one place which gives you
a brief knowledge about how to list all the files of a certain type in a
directory by using python programming.

So there are three certain extensions such as

  * Using os. walk()
  * Using os. listdir()
  * Using glob. glob()

 **Directory used:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201204233346/Screenshot-1555-2-300x169.png)

image of root folder having path name D:\GFG

 _ **Using os.walk() function**_

In python programming, there are different os modules which enable several
methods to interact with the file system. As mentioned above it has walk()
function which helps us to list all the files in the specific path by
traversing the directory either by a bottom-up approach or by a top-down
approach and return 3 tuples such as root, dir, files

Here root is the root directory or root folder, dir is the subdirectory of the
root directory and files is the files under the root directory and it’s a
subdirectory.

  

  

 **Syntax:**

> os.walk(r’pathname’)

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import os

# traverse whole directory

for root, dirs, files in os.walk(r'D:\GFG'):

 # select file name

 for file in files:

 # check the extension of files

 if file.endswith('.png'):

 # print whole path of files

 print(os.path.join(root, file))  
  
---  
  
 __

 __

 **Output:**

> D:\GFG\gfg_png_file.png

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201204235528/Screenshot159-300x168.png)

The output of os.walk() function

 _ **Using os. listdir() function**_

Os has another method which helps us find files on the specific path known as
listdir(). It returns all the file names in the directory specified in the
location or path as a list format in random order. It excludes the ‘.’ and
‘..’ if they are available in the input folder.

 **Syntax:**

> os.listdir(r’pathname’)
>
>  
>
>
>  
>

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import os

# return all files as a list

for file in os.listdir(r'D:\GFG'):

 # check the files which are end with specific extention

 if file.endswith(".png"):

 # print path name of selected files

 print(os.path.join(r'C:\GFG\Screenshots', file))  
  
---  
  
 __

 __

 **Output:**

> D:\GFG\gfg_png_file.png

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201204233349/Screenshot-1574-300x169.png)

The output of os.listdir() function

 _ **Using glob. glob() function:**_

In the previous examples, we have to iterate over a list of files in a
directory having name match with the particular extensions or patterns. But
glob modules gives the facility to find a list of files with particular
extensions or pattern. This function has two parameters one is path-name with
a specific pattern which filters out all the files and returns the files as a
list. Another Parameter named as recursive by default it is off means false.
When its value is true then the function searches its directory along with its
subdirectory. All wild cards are allowed here like’?’,’*’ etc.

 **Syntax:**

> glob.glob(path name, recursive=True)

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import glob

import os

# glob.glob() return a list of file name with specified pathname

for file in glob.glob(r''D: \GFG' + "**/*.png",
recursive=True):

 # print the path name of selected files

 print(os.path.join(r''D: \GFG', file))  
  
---  
  
 __

 __

 **Output:**

> D:\GFG\gfg_png_file.png

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201204233349/Screenshot-1574-300x169.png)

The output of glob.glob() function

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


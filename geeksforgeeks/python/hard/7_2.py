Python | Sort and store files with same extension



Have you ever wanted to find any particular file in a folder, but then
completely freak out when you find that folder to be a hell of a mess? Well,
Python is a rescue here.  
Using Python OS-module and shutil module, we can organize the files with same
extensions and store in separate folders.

Look at the image shown below –  
![Unorganized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190518232734/unorganized.jpg)

This folder is fully unorganized. If you are told to find a particular file in
this folder (or maybe an even larger folder with thousands of files), you will
be stuck and become completely dumbstruck. It might be very tough (even
impossible) to find a file from this ocean of mess. This problem can be solved
using Python with a few lines of code. Let’s see how can we do this.

Below is the Python implementation –

 __

 __  
 __

 __

 __  
 __  
 __

import os

import shutil

 

# Write the name of the directory here,

# that needs to get sorted

path = '/path/to/directory'

 

 

# This will create a properly organized 

# list with all the filename that is

# there in the directory

list_ = os.listdir(path)

 

# This will go through each and every file

for file_ in list_:

 name, ext = os.path.splitext(file_)

 

 # This is going to store the extension type

 ext = ext[1:]

 

 # This forces the next iteration,

 # if it is the directory

 if ext == '':

 continue

 

 # This will move the file to the directory

 # where the name 'ext' already exists

 if os.path.exists(path+'/'+ext):

 shutil.move(path+'/'+file_,
path+'/'+ext+'/'+file_)

 

 # This will create a new directory,

 # if the directory does not already exist

 else:

 os.makedirs(path+'/'+ext)

 shutil.move(path+'/'+file_,
path+'/'+ext+'/'+file_)  
  
---  
  
 __

 __

 **Output:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190518234039/organized.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save


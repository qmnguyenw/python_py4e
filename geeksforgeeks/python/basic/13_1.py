Python | os.listdir() method



 _ **os.listdir()**_ method in python is used to get the list of all files and
directories in the specified directory. If we don’t specify any directory,
then list of files and directories in the current working directory will be
returned.

>  ** _Syntax:_** os.listdir(path)
>
>  ** _Parameters:_**  
>  path (optional) : path of the directory
>
>  ** _Return Type:_** This method returns the list of all files and
> directories in the specified path. The return type of this method is _list_.

 **Code #1:** use of os.listdir() method

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.listdir() method

 

# importing os module 

import os

 

# Get the list of all files and directories

# in the root directory

path = "/"

dir_list = os.listdir(path)

 

print("Files and directories in '", path, "' :") 

 

# print the list

print(dir_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    Files and directories in ' / ' :
    ['sys', 'run', 'tmp', 'boot', 'mnt', 'dev', 'proc', 'var', 'bin', 'lib64', 'usr', 
    'lib', 'srv', 'home', 'etc', 'opt', 'sbin', 'media']
    

  
**Code #2:** use of os.listdir() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.listdir() method

 

# importing os module 

import os

 

# Get the path of current working directory

path = os.getcwd()

 

# Get the list of all files and directories

# in current working directory

dir_list = os.listdir(path)

 

 

print("Files and directories in '", path, "' :") 

# print the list

print(dir_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    Files and directories in ' /home/ihritik ' :
    ['.rstudio-desktop', '.gnome', '.ipython', '.cache', '.config', '.ssh', 'Public',
    'Desktop', '.pki', 'R', '.bash_history', '.Rhistory', '.oracle_jre_usage', 'Music', 
    '.ICEauthority', 'Documents', 'examples.desktop', '.swipl-dir-history', '.local', 
    '.gnupg', '.profile', 'Pictures', '.keras', '.viminfo', '.thunderbird', 'Templates',
    '.bashrc', '.bash_logout', '.sudo_as_admin_successful', 'Videos', 'images', 
    'tf_wx_model', 'Downloads', '.mozilla', 'geeksforgeeks']
    

  
**Code #3:** omitting path parameter

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.listdir() method

 

# importing os module 

import os

 

 

# If we do not specify any path

# os.listdir() method will return

# the list of all files and directories

# in current working directory

 

dir_list = os.listdir()

 

print("Files and directories in current working directory :") 

 

# print the list

print(dir_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    Files and directories in current working directory :
    ['.rstudio-desktop', '.gnome', '.ipython', '.cache', '.config', '.ssh', 'Public',
    'Desktop', '.pki', 'R', '.bash_history', '.Rhistory', '.oracle_jre_usage', 'Music', 
    '.ICEauthority', 'Documents', 'examples.desktop', '.swipl-dir-history', '.local', 
    '.gnupg', '.profile', 'Pictures', '.keras', '.viminfo', '.thunderbird', 'Templates',
    '.bashrc', '.bash_logout', '.sudo_as_admin_successful', 'Videos', 'images', 
    'tf_wx_model', 'Downloads', '.mozilla', 'geeksforgeeks']
    

As we can see the output of _Code #2_ and _Code #3_ are same. So if we omit
the path parameter os.listdir() method will return the list of all files and
directories in the current working directory.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


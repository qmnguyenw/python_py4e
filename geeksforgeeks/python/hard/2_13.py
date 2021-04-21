How to uncompress a “.tar.gz” file using Python ?



.tar.gz files are made by the combination of TAR packaging followed by a GNU
zip (gzip) compression. These files are commonly used in Unix/Linux based
system as packages or installers. In order to read or extract these files, we
have to first decompress these files and after that expand them with the TAR
utilities as these files contain both .tar and .gz files.

In order to extract or un-compress “.tar.gz” files using python, we have to
use the tarfile module in python. This module can read and write .tar files
including .gz, .bz compression methods.

### Approach

  * Import module
  * Open .tar.gz file
  * Extract file in a specific folder
  * Close file

###  **File in use**

 **Name:** gfg.tar.gz

**Link to download this file:** Click here

 **Contents:**

  

  

![](https://media.geeksforgeeks.org/wp-content/uploads/20201212183550/6.PNG)

“gfg.tar.gz” file

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the "tarfile" module

import tarfile

 

# open file

file = tarfile.open('gfg.tar.gz')

 

# extracting file

file.extractall('./Destination_FolderName')

 

file.close()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201212182031/1.PNG)

A folder named “Destination_Folder” is created.

![](https://media.geeksforgeeks.org/wp-content/uploads/20201212182032/2.PNG)

Files are uncompressed inside the “Destination_Folder”

 **Example:** Printing file names before extracting

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the "tarfile" module

import tarfile

 

# open file

file = tarfile.open('gfg.tar.gz')

 

# print file names

print(file.getnames())

 

# extract files

file.extractall('./Destination_FolderName')

 

# close file

file.close()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201212182911/3.PNG)

 **Example :** Extract a specific file

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the "tarfile" module

import tarfile

 

# open file

file = tarfile.open('gfg.tar.gz')

 

# extracting a specific file

file.extract('sample.txt', './Destination_FolderName')

 

file.close()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20201212183214/4.PNG)

A new folder named “Destination_FolderName” is created

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201212183216/5-660x106.PNG)

‘sample.txt’ is uncompressed inside the “Destination_FolderName”

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


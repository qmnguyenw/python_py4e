Python Program to delete a file



Ever wanted to delete a file, that too from a Python program, with a few lines
of code? Well, you are in the right place. Today we are going to learn how we
are going to be deleting a file by using Python.

 **Note:** We will be importing the os library and going to use the
os.remove() function to remove the desired file. If you don’t have os library,
then open **Command Prompt** and write **pip install os** , to install the
required os library.

Below is the Python implementation –

 __

 __  
 __

 __

 __  
 __  
 __

import os

print ("Enter 'quit' for exiting the program")

filename = input('Enter the name of the file, that is to be deleted :
')

if filename == 'quit':

 exit()

else:

 print ('\nStarting the removal of the file !')

 os.remove(filename)

 

 print ('\nFile, ', filename, 'The file deletion is successfully
completed !!')

 

   
  
---  
  
__

__

**Output:**  
 **The desired file to be deleted:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190617181938/desired.png)

 **Sample run of the program**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190617181941/aa5.png)

  

  

 **When we enter the name of the file to be deleted:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190617181944/sacsasaf.png)

 **The deletion:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190617181946/deletion1.png)

 **The Working:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190617181954/Jun1720196_17PM.gif)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


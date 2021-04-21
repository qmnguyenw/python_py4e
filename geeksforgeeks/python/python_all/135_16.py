Python | Merge two text files



Given two text files, the task is to merge the data and store in a new text
file. Let’s see how can we do this task using Python.

To merge two files in Python, we are asking user to enter the name of the
primary and second file and make a new file to put the unified content of the
two data into this freshly created file.

In order to do this task, we have to import shutil & pathlib libraries.
You can install the libraries using this command –

    
    
    pip install shutil
    pip install pathlib

Also, place the two text files on the Desktop.

 **First text file:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190709213532/xzcccewwrty.png)

  

  

 **Second text file:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190709213530/xzzzzxxz.png)

Below is the Python implementation –

 __

 __  
 __

 __

 __  
 __  
 __

import shutil

from pathlib import Path

 

firstfile = Path(r'C:\Users\Sohom\Desktop\GFG.txt')

secondfile = Path(r'C:\Users\Sohom\Desktop\CSE.txt')

 

newfile = input("Enter the name of the new file: ")

print()

print("The merged content of the 2 files will be in", newfile)

 

with open(newfile, "wb") as wfd:

 

 for f in [firstfile, secondfile]:

 with open(f, "rb") as fd:

 shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)

 

print("\nThe content is merged successfully.!")

print("Do you want to view it ? (y / n): ")

 

check = input()

if check == 'n':

 exit()

else:

 print()

 c = open(newfile, "r")

 print(c.read())

 c.close()  
  
---  
  
 __

 __

 **Output:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190715181537/fsdghjhtgfdsghdsgds.png)

 **The updated merged text file:**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190715181723/ewdfrds.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


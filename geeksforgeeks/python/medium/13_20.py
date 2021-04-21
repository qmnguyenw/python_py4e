Run python script from anywhere in linux



In Linux, there is a way to execute python files from anywhere. This can be
done by typing several commands in the terminal.

### Prerequisite:

  *  **Basic Shell Commands in Linux**
  *  **Basics of python**

### Steps:

  * At first, open the terminal and go to the home directory. To go the home directory type the following command.
    
        cd ~

  * Create a folder and a python script inside that folder. Let the name of the folder be “check” and name of the script be “file1”. Type the following command to perform the above operations.
    
    
    mkdir check
    cd check
    touch file1.py
    

  * Then type this script in the file1.py

 __

 __  
 __

 __

 __  
 __  
 __

import os

i = 1

 

# Write the path where to create the directories

path ="/home / dev / test/"

try:

 while i<5:

 os.mkdir(path+"file"+str(i))

 i+= 1

except OSError:

 print("File creation failed !!")  
  
---  
  
 __

 __

This script will create 4 directories in the specified path.

  * Then to find where the python is installed in the system type the below commands.  
For python 2.7

    
        which python

For python 3

    
        which python3

  * Copy the output and add this in the starting of the script e.g if output is /usr/bin/python3 then write the below command in the starting of the script.
    
        #!/usr/bin/python3

So the python script would look like

  

  

 __

 __  
 __

 __

 __  
 __  
 __

#! usr / bin / python3

import os

i = 1

# Write the path where to create the directories

path ="/home / dev / test/"

try:

 while i<5:

 os.mkdir(path+"file"+str(i))

 i+= 1

except OSError:

 print("File creation failed !!")  
  
---  
  
 __

 __

  * Type the following command to get the path of the working directory, starting from the root.
    
        pwd

Let it be /home/usr/check

  * Add this path in $PATH variable. For this type in terminal
    
        sudo nano .bashrc

Before this command make sure that you are in the home directory.  
Then add this line in the file

    
        export PATH=$PATH:/home/dev/check

This will get added to the path variable. Then type

    
         source ~/.bashrc

  * Close the terminal and open again. Now we can run the python file directly from anywhere in the terminal by typing the file name
    
        file1.py

This will create the four directories in the check folder. Now any python file
placed in the check directory we can be executed from anywhere in the terminal
by typing the file name.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


File Searching using Python



There may be many instances when you want to search a system.Suppose while
writing an mp3 player you may want to have all the ‘.mp3’ files present. Well
here’s how to do it in a simple way.  
This code searches all the folders in the file it’s being run. If you want
some other kinds of files just change the extension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to search .mp3 files in current

# folder (We can change file type/name and path

# according to the requirements.

import os

 

# This is to get the directory that the program 

# is currently running in.

dir_path = os.path.dirname(os.path.realpath(__file__))

 

for root, dirs, files in os.walk(dir_path):

 for file in files: 

 

 # change the extension from '.mp3' to 

 # the one of your choice.

 if file.endswith('.mp3'):

 print (root+'/'+str(file))  
  
---  
  
 __

 __

os is not an external ibrary in python. So I feel this is the simplest and the
best way to do this.

This article is contributed by **soumith kumar**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


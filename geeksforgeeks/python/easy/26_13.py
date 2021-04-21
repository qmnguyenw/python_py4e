os.walk() in Python



How to traverse file system in Python ? Suppose we have given below file
structure in our system and we want to traverse all it’s branches completely
from top to bottom ?  
![Example file system](https://media.geeksforgeeks.org/wp-
content/uploads/osWalk-1.jpg)

### How does os.walk() work in python ?

OS.walk() generate the file names in a directory tree by walking the tree
either top-down or bottom-up. For each directory in the tree rooted at
directory top (including top itself), it yields a 3-tuple (dirpath, dirnames,
filenames).

  *  ** _root :_** Prints out directories only from what you specified.
  *  ** _dirs :_** Prints out sub-directories from root.
  *  ** _files :_** Prints out all files from root and directories.

 __

 __  
 __

 __

 __  
 __  
 __

# Driver function

import os

if __name__ == "__main__":

 for (root,dirs,files) in os.walk('Test', topdown=true):

 print (root)

 print (dirs)

 print (files)

 print ('--------------------------------')  
  
---  
  
 __

 __

Output:

    
    
    ![Output](https://media.geeksforgeeks.org/wp-content/uploads/Output-2.png)
    

This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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


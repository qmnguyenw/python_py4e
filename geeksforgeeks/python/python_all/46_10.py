Python program to find files having a particular extension using RegEx



 **Prerequisite:** Regular Expression in Python

Many of the times we need to search for a particular type of file from a list
of different types of files. And we can do so with only a few lines of code
using python. And the cool part is we don’t need to install any external
package, python has a built-in package called **re** , with which we can
easily write the program for performing this task.

 **Approach:**

  * This program searches for the files having **“.xml”** extension from a list of different files.
  * Make a regular expression/pattern : “\\.xml$”
  * Here **re.search()** function is used to check for a match anywhere in the string (name of the file). It basically returns the match object when the pattern is found and if the pattern is not found it returns null.
  * The functionality of different Metacharacters used here:
    1. \ It is used to specify a special meaning of character after it. It is also used to escape special characters.
    2. $ The string ends with the pattern which is before it.
  * Here “.xml” pattern is searched and processed.

Below is the implementation:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import re

 

# list of different types of file

filenames = ["gfg.html", "geeks.xml", 

 "computer.txt", "geeksforgeeks.jpg"]

 

for file in filenames:

 # search given pattern in the line 

 match = re.search("\.xml$", file)

 

 # if match is found

 if match:

 print("The file ending with .xml is:",

 file)  
  
---  
  
 __

 __

  
 **Output:**

    
    
    The file ending with .xml is: geeks.xml

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


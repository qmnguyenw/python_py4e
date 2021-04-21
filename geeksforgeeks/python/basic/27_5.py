Python | sep parameter in print()



The separator between the arguments to print() function in Python is space by
default (softspace feature) , which can be modified and can be made to any
character, integer or string as per our choice. The ‘sep’ parameter is used to
achieve the same, it is found only in python 3.x or later. It is also used for
formatting the output strings.  

**Examples:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#code for disabling the softspace feature

print('G','F','G', sep='')

#for formatting a date

print('09','12','2016', sep='-')

#another example

print('pratik','geeksforgeeks', sep='@')  
  
---  
  
 __

 __

 **Output:**  

    
    
    GFG
    09-12-2016
    pratik@geeksforgeeks

The sep parameter when used with the end parameter it produces awesome
results. Some examples by combining the sep and end parameters.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

print('G','F', sep='', end='')

print('G')

#\n provides new line after printing the year

print('09','12','2016', sep='-', end='\n')

print('prtk','agarwal', sep='', end='@')

print('geeksforgeeks')  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    GFG
    09-12-2016
    prtkagarwal@geeksforgeeks

Note: Please change the language from Python to Python 3 in the online ide.
****  
Go to your interactive python ide by typing python in your cmd ( windows ) or
terminal ( linux )  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#import the below module and see what happens

import antigravity

#NOTE - it wont work on online ide  
  
---  
  
 __

 __

This article is contributed by **Pratik Agarwal**. If you like GeeksforGeeks
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


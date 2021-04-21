numpy.arange() in Python



 **About :**  
 **arange([start,] stop[, step,][, dtype]) :** Returns an array with evenly
spaced elements as per the interval. The interval mentioned is half opened
i.e. [Start, Stop)  
 **Parameters :**

    
    
    **start :** [optional] start of interval range. By default start = 0
    **stop  :** end of interval range
    **step  :** [optional] step size of interval. By default step size = 1,  
    For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. 
    **dtype :** type of output array
    

**Return:**

    
    
    Array of evenly spaced values.
    Length of array being generated  = **Ceil((Stop - Start) / Step)**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Programming illustrating

# numpy.arange method

 

import numpy as geek

 

print("A\n", geek.arange(4).reshape(2, 2), "\n")

 

print("A\n", geek.arange(4, 10), "\n")

 

print("A\n", geek.arange(4, 20, 3), "\n")  
  
---  
  
 __

 __

Output :

    
    
    A
     [[0 1]
     [2 3]]
    
    A
     [4 5 6 7 8 9]
    
    A
     [ 4  7 10 13 16 19]
    
    

**Note 1:**  
These NumPy-Python programs won’t run on onlineID, so run them on your systems
to explore them.

 **Note 2:**  
The advantage of numpy.arange() over the normal in-built range() function is
that it allows us to generate sequences of numbers that are not integers. For
example

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python Programming illustrating

# numpy.arange method

 

import numpy as np

 

# Printing all numbers from 1 to 2 in steps of 0.1

print(np.arange(1, 2, 0.1))  
  
---  
  
 __

 __

Output:

    
    
    [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]
    

If you try it with the range() function, you get a TypeError.

This article is contributed by **Mohit Gupta_OMG 😀**. If you like
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


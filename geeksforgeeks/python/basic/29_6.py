trunc() in Python



 **Truncate in Python**

There are many built-in modules in python. Out of these module there is one
interesting module known as math module which have several functions in it
like, ceil, floor, truncate, factorial, fabs, etc.

Out of these functions there is an interesting function called **truncate**
which behaves as a ceiling function for negative number and floor function for
positive number.

In case of positive number

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show output of floor(), ceil()

# truncate() for a positive number.

import math

print math.floor(3.5) # floor

print math.trunc(3.5) # work as floor

print math.ceil(3.5) # ceil  
  
---  
  
 __

 __

Output:

  

  

    
    
    3.0
    3
    4.0

In case of negative number

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show output of floor(), ceil()

# truncate() for a negative number.

import math

print math.floor(-3.5) # floor 

print math.trunc(-3.5) # work as ceil

print math.ceil(-3.5) # ceil  
  
---  
  
 __

 __

Output:

    
    
    -4.0
    -3
    -3.0

This is because the ceiling function is used to round up, i.e., towards
positive infinity and floor function is used to round down, i.e., towards
negative infinity.

But the truncate function is used to round up or down towards zero.

Diagrammatic representation of truncate function:-  
![inf](https://media.geeksforgeeks.org/wp-content/uploads/charge.jpg)

This article is contributed by **Arpit Agarwal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article and mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


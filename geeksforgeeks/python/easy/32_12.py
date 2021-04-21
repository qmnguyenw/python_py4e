Partial Functions in Python



Partial functions allow us to fix a certain number of arguments of a function
and generate a new function.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

from functools import partial

 

# A normal function

def f(a, b, c, x):

 return 1000*a + 100*b + 10*c + x

 

# A partial function that calls f with

# a as 3, b as 1 and c as 4.

g = partial(f, 3, 1, 4)

 

# Calling g()

print(g(5))  
  
---  
  
 __

 __

 **Output:**

    
    
    3145
    

In the example we have pre-filled our function with some constant values of a,
b and c. And g() just takes a single argument i.e. the variable x.

 **Another Example :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from functools import *

 

# A normal function

def add(a, b, c):

 return 100 * a + 10 * b + c

 

# A partial function with b = 1 and c = 2

add_part = partial(add, c = 2, b = 1)

 

# Calling partial function

print(add_part(3))  
  
---  
  
 __

 __

 **Output:**

    
    
    312
    

  * Partial functions can be used to derive specialized functions from general functions and therefore help us to reuse our code.
  * This feature is similar to bind in C++.

This article is contributed by **Mayank Rawat** .If you like GeeksforGeeks and
would like to contribute, you can also write an article using
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


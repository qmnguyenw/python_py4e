copyreg — Register pickle support functions



The copyreg module defines functions which are used by pickling specific
objects while pickling or copying. This module provides configuration
information about object constructors(may be factory functions or class
instances) which are not classes.

 **copyreg.constructor(object)**  
This function is used for declaring object as a valid constructor. An object
is not considered as a valid constructor if it is not callable. This function
raises TypeError if the object is not callable.

 **copyreg.pickle(type, function, constructor=None)**  
This is used to declare function as a “reduction” function for objects of type
type. function should return either a string or a tuple containing two or
three elements.  
The constructor parameter is optional. It is a callable object which can be
used to reconstruct the object when called with the tuple of arguments
returned by function at pickling time. TypeError is raised if object is a
class or constructor is not callable.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to illustrate

# use of copyreg module 

import copyreg, copy, pickle 

 

class B(object): 

 def __init__(self, a): 

 self.a = a 

 

def pickle_b(b): 

 print("pickling a C instance...") 

 return C, (b.a, ) 

 

copyreg.pickle(B, pickle_b) 

b = B(1) 

d = copy.copy(b) 

print (d) 

 

r = pickle.dumps(b) 

print (r)   
  
---  
  
__

__

**Output :**

  

  

    
    
    pickling a C instance...
    
    pickling a C instance...
    b'\x80\x03c__main__\nC\nq\x00K\x01\x85q\x01Rq\x02.'
    

This article is contributed by **Aditi Gupta**. If you like GeeksforGeeks and
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


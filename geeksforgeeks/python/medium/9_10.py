Difference between __sizeof__() and getsizeof() method – Python



Memory management is of utmost priority when we write large chunks of code. So
in addition to good coding knowledge, it is important to be able to write
programs, so as to handle memory efficiently.  
So let us look at the two ways of getting the size of a particular object in
Python.  
These are getsizeof() method and __sizeof() method.  
 **getsizeof()** is a system-specific method and hence we have to import the
sys module to use it. A sample code is as shown below for calculating the size
of a list.

 __

 __  
 __

 __

 __  
 __  
 __

import sys

a =[1, 2]

b =[1, 2, 3, 4]

c =[1, 2, 3, 4]

d =[2, 3, 1, 4, 66, 54, 45, 89]

print(sys.getsizeof(a))

print(sys.getsizeof(b))

print(sys.getsizeof(c))

print(sys.getsizeof(d))  
  
---  
  
 __

 __

Output:

    
    
    72
    88
    88
    120

getsizeof() method calls the __sizeof__() method o the object with an
additional garbage collector overhead. Hence the size returned by the
getsize() method will be more than that returned by the __sizeof()__ method.  
For example, the getsizeof() method returns 64 bytes for an empty list and
then 8 bytes for every additional element.

Now let’s look at the **__sizeof__()** method. It returns the size of the
object without any overhead.

 __

 __  
 __

 __

 __  
 __  
 __

w=[1, 2]

x =[4, 5, 7, 9]

y =[2, 8, 6, 56, 45, 89, 88]

z =[54, 45, 12, 23, 24, 90, 20, 40]

print(w.__sizeof__())

print(x.__sizeof__())

print(y.__sizeof__())

print(z.__sizeof__())  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    56
    72
    96
    104

For example, the __sizeof__() method returns 40 bytes for an empty list and
then 8 bytes for every additional element.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


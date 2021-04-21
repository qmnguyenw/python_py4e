range() vs xrange() in Python



range() and xrange() are two functions that could be used to iterate a certain
number of times in for loops in Python. In Python 3, there is no xrange , but
the range function behaves like xrange in Python 2.If you want to write code
that will run on both Python 2 and Python 3, you should use range().

 **range()** – This returns a range object (a type of iterable).  
 **xrange()** – This function returns the **generator object** that can be
used to display numbers only by looping. Only particular range is displayed on
demand and hence called “ **lazy evaluation** “.

Both are implemented in different ways and have different characteristics
associated with them. The points of comparisons are:

  * Return Type
  * Memory
  * Operation Usage
  * Speed

 **Return Type**

range() returns – **range** object.  
xrange() returns – **xrange()** object.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate range() vs xrange()

# on basis of return type

 

# initializing a with range()

a = range(1,10000)

 

# initializing a with xrange()

x = xrange(1,10000)

 

# testing the type of a

print ("The return type of range() is : ")

print (type(a))

 

# testing the type of x

print ("The return type of xrange() is : ")

print (type(x))  
  
---  
  
 __

 __

Output:

  

  

    
    
    The return type of range() is : 
    <type 'list'>
    The return type of xrange() is : 
    <type 'xrange'>
    

**Memory**

The variable storing the **range** created by range() **takes more memory** as
compared to variable storing the range using xrange(). The basic reason for
this is the return type of range() is list and xrange() is xrange() object.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate range() vs xrange()

# on basis of memory

 

import sys

 

# initializing a with range()

a = range(1,10000)

 

# initializing a with xrange()

x = xrange(1,10000)

 

# testing the size of a

# range() takes more memory

print ("The size allotted using range() is : ")

print (sys.getsizeof(a))

 

# testing the size of a

# range() takes less memory

print ("The size allotted using xrange() is : ")

print (sys.getsizeof(x))  
  
---  
  
 __

 __

Output:

    
    
    The size allotted using range() is : 
    80064
    The size allotted using xrange() is : 
    40
    

**Operations usage**

As range() returns the list, all the operations that **can** be applied on the
list can be used on it. On the other hand, as xrange() returns the xrange
object, operations associated to list **cannot** be applied on them, hence a
disadvantage.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate range() vs xrange()

# on basis of operations usage 

 

# initializing a with range()

a = range(1,6)

 

# initializing a with xrange()

x = xrange(1,6)

 

# testing usage of slice operation on range()

# prints without error

print ("The list after slicing using range is : ")

print (a[2:5])

 

# testing usage of slice operation on xrange()

# raises error

print ("The list after slicing using xrange is : ")

print (x[2:5])  
  
---  
  
 __

 __

Error:

    
    
    Traceback (most recent call last):
      File "1f2d94c59aea6aed795b05a19e44474d.py", line 18, in 
        print (x[2:5])
    TypeError: sequence index must be integer, not 'slice'
    

Output:

    
    
    The list after slicing using range is : 
    [3, 4, 5]
    The list after slicing using xrange is : 
    

**Speed**

Because of the fact that xrange() evaluates only the generator object
containing only the values that are required by lazy evaluation, therefore is
**faster** in implementation than range().

 **Important Points:**

  * If you want to write code that will run on both Python 2 and Python 3, use range() as the xrange function is deprecated in Python 3
  * range() is faster if iterating over the same sequence multiple times.
  * xrange() has to reconstruct the integer object every time, but range() will have real integer objects. (It will always perform worse in terms of memory however)

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
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


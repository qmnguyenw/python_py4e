Python – Initialize empty array of given length



 **Prerequisite:** List in Python

As we know Array is a collection of items stored at contiguous memory
locations. In Python, List (Dynamic Array) can be treated as Array. In this
article, we will learn how to initialize an empty array of some given size.

Let’s see different Pythonic ways to do this task.

 **Method 1 –**

 **Syntax:**

  

  

    
    
    list1 = [0] * size
    list2 = [None] * size
    

__

__  
__

__

__  
__  
__

# initializes all the 10 spaces with 0’s

a = [0] * 10

 

# initializes all the 10 spaces with None

b = [None] * 10

 

# initializes all the 10 spaces with A's

c = ['A'] * 5

 

# empty list which is not null, it's just empty.

d = [] 

 

print (a, "\n", b, "\n", c, "\n", d);  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    [None, None, None, None, None, None, None, None, None, None] 
    ['A', 'A', 'A', 'A', 'A'] 
    []
    

  
**Method 2 –** Use loops just like C and assign the size.

 **Syntax:**

    
    
    a = [0 for x in range(size)] #using loops
    

__

__  
__

__

__  
__  
__

a= []

b = []

 

# initialize the spaces with 0’s with 

# the help of list comprehensions

a = [0 for x in range(10)]

print(a)

 

# initialize multi-array 

b = [ [ None for y in range( 2 ) ]

 for x in range( 2 ) ]

 

print(b)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    [[None, None], [None, None]]
    

  
**Method 3 –** Using Numpy to create empty array.

 __

 __  
 __

 __

 __  
 __  
 __

import numpy

 

# create a simple array with numpy empty()

a = numpy.empty(5, dtype=object)

print(a)

 

# create multi-dim array by providing shape

matrix = numpy.empty(shape=(2,5),dtype='object')

print(matrix)  
  
---  
  
 __

 __

 **Output:**

    
    
    [None None None None None]
    
    [[None None None None None]
     [None None None None None]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


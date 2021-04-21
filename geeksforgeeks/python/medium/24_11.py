Extending a list in Python (5 different ways)



Extending a list in python can be done is following ways:  
 **1\. Usingappend() function**: We can append at the end of the list by using
append() function. For appending any single value to the list or appending a
list to the list, the syntax stays the same. But we can only append a single
value at a time using append() function

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to extend a list using append()

 

a = [10, 12, 13, 17] 

 

# appending multiple values

a.append(20)

a.append(22)

print(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 12, 13, 17, 20, 22]
    

**2\. Using ‘+’ operator:** We can add values by using the “+” operator. We
can use [] to add any number of values to the list. Adding multiple values can
be done by using ‘, ‘ values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to extend a list using '+'

 

a = [10, 12, 13, 17] 

 

# Appending single value

a = a + [20]

 

# append more then one values

a = a + [30, 40]

print(a)  
  
---  
  
 __

 __

Output:

    
    
    [10, 12, 13, 17, 20, 30, 40]
    

**3\. Using slicing:** Using slicing in python, single or multiple values can
be added to a list.

  

  

>  **a[:0] = [x, y, z…]**

Here a is the list in which the values(x, y, z..) are to be added. In this
method the values are appended to the front of the list.

![](https://media.geeksforgeeks.org/wp-content/uploads/WhatsApp-
Image-2017-12-23-at-8.13.04-PM.jpeg)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to extend a list using 'slicing'

 

# appending multiple value 

a =[10, 12, 13, 17] 

 

# add 1 number

a[:0] = [30]

 

# add two numbers

a[:0] = [40, 50]

print(a)  
  
---  
  
 __

 __

Output:

    
    
    [40, 50, 30, 10, 12, 13, 17]
    

**4.Using chain():** Using chain() iterator function, we can extend a list by
the syntax:

> list(chain(a, [x, y, z..]))

Here a is the list in which the values(x, y, z..) are to be added. In this
method the values are appended to the end of the list.

 __

 __  
 __

 __

 __  
 __  
 __

# python program to extend a list using

# "chain" iterator functions

from itertools import *

 

a = [10, 20, 30]

 

# extend a list

print(list(chain(a, [40, 50, 60])))  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 20, 30, 40, 50, 60]
    

**5\. UsingExtend**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to extend a list using extend()

a = [10, 12, 13, 17] 

 

b = [30, 40]

 

a.extend(b)

 

print(a)  
  
---  
  
 __

 __

Output:

    
    
    [10, 12, 13, 17, 30, 40]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


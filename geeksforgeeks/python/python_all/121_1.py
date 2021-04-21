Python | Minimum element in tuple list



Sometimes, while working with data in form of records, we can have a problem
in which we need to find the minimum element of all the records received. This
is a very common application that can occur in Data Science domain. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingmin() \+ generator expression**

This is the most basic method to achieve solution to this task. In this, we
iterate over whole nested lists using generator expression and get the minimum
element using min().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum element in tuple list

# using min() + generator expression

 

# initialize list 

test_list = [(2, 4), (6, 7), (5, 1), (6,
10), (8, 7)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Minimum element in tuple list

# using min() + generator expression

res = min(int(j) for i in test_list for j in i)

 

# printing result

print("The Minimum element of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]
    The Minimum element of list is : 1
    

  

  

**Method #2 : Usingmin() + map() + chain.from_iterable()**

The combination of above methods can also be used to perform this task. In
this, the extension of finding minimum is done by combination of map() and
from_iterable().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum element in tuple list

# using min() + map() + chain.from_iterable()

from itertools import chain

 

# initialize list 

test_list = [(2, 4), (6, 7), (5, 1), (6,
10), (8, 7)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Minimum element in tuple list

# using min() + map() + chain.from_iterable()

res = min(map(int, chain.from_iterable(test_list)))

 

# printing result

print("The Minimum element of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]
    The Minimum element of list is : 1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


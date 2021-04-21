Python – Count elements in tuple list



Sometimes, while working with data in form of records, we can have a problem
in which we need to find the count of all the records received. This is a very
common application that can occur in Data Science domain. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usinglen() \+ generator expression**  
This is the most basic method to achieve solution to this task. In this, we
iterate over whole nested lists using generator expression and get the count
using len().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple list elements count

# using len() + generator expression

 

# initialize list 

test_list = [(2, 4), (6, 7), (5, 1), (6,
10), (8, 7)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Tuple list elements count

# using len() + generator expression

temp = list((int(j) for i in test_list for j in
i))

res = len(temp)

 

# printing result

print("The tuple list elements count : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]
    The tuple list elements count : 10
    

**Method #2 : Usinglen() + map() + chain.from_iterable()**  
The combination of above methods can also be used to perform this task. In
this, the extension of finding count is done by combination of map() and
from_iterable().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple list elements count

# using len() + map() + chain.from_iterable()

from itertools import chain

 

# initialize list 

test_list = [(2, 4), (6, 7), (5, 1), (6,
10), (8, 7)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Tuple list elements count

# using len() + map() + chain.from_iterable()

res = len(list(map(int, chain.from_iterable(test_list))))

 

# printing result

print("The tuple list elements count : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]
    The tuple list elements count : 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Concatenate All Records



Sometimes, while working with data in form of records, we can have a problem
in which we need to concatenate elements of all the records received. This is
a very common application that can occur in Data Science domain. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using generator expression + join()**  
This is the most basic method to achieve solution to this task. In this, we
iterate over whole nested lists using generator expression and get the
concatenated elements using join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate All Records

# using join() + generator expression

 

# initialize list 

test_list = [('geeksforgeeks ', 'is' ), (' best', '
for'), (' all', ' geeks')]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Concatenate All Records

# using join() + generator expression

res = "".join(j for i in test_list for j in i)

 

# printing result

print("The Concatenated elements of list is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('geeksforgeeks ', 'is'), (' best', ' for'), (' all', ' geeks')]
    The Concatenated elements of list is : geeksforgeeks is best for all geeks
    

**Method #2 : Usingjoin() + map() + chain.from_iterable()**  
The combination of above methods can also be used to perform this task. In
this, the extension of concatenation is done by combination of map() and
from_iterable().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate All Records

# using join() + map() + chain.from_iterable()

from itertools import chain

 

# initialize list 

test_list = [('geeksforgeeks ', 'is' ), (' best', '
for'), (' all', ' geeks')]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Concatenate All Records

# using join() + map() + chain.from_iterable()

res = "".join(map(str, chain.from_iterable(test_list)))

 

# printing result

print("The Concatenated elements of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('geeksforgeeks ', 'is'), (' best', ' for'), (' all', ' geeks')]
    The Concatenated elements of list is : geeksforgeeks is best for all geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


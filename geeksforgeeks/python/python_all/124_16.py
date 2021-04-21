Python | Get tuple element data types



Tuples can be a collection of various data types, and unlike simpler data
types, conventional methods of getting the type of each element of tuple is
not possible. For this we need to have different ways to achieve this task.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingmap() + type()**  
Using this function is most conventional and best way to perform this task. In
this, we just allow map() to extend the logic of finding data types using
type() to each element of tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get tuple element data types

# Using map() + type()

 

# Initializing tuple

test_tup = ('gfg', 1, ['is', 'best'])

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# Get tuple element data types

# Using map() + type()

res = list(map(type, test_tup))

 

# printing result

print("The data types of tuple in order are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ('gfg', 1, ['is', 'best'])
    The data types of tuple in order are : [<class 'str'>, <class 'int'>, <class 'list'>]
    

**Method #2 : Using collections.Sequence +isinstance() + type()**  
We can perform this task using the combination of above functions. The
additional advantage of using this method it that it also provides us with the
length of each element if its type is complex data type.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get tuple element data types

# Using collections.Sequence + isinstance() + type()

import collections

 

# Initializing tuple

test_tup = ('gfg', 1, ['is', 'best'])

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# Get tuple element data types

# Using collections.Sequence + isinstance() + type()

res = [(type(ele), len(ele) if isinstance(ele,
collections.Sequence) else None)

 for ele in test_tup]

 

# printing result

print("The data types of tuple in order are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ('gfg', 1, ['is', 'best'])
    The data types of tuple in order are : [(<class 'str'>, 3), (<class 'int'>, None), (<class 'list'>, 2)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


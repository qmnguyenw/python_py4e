Python | Check order specific data type in tuple



Sometimes, while working with records, we can have a problem in which we need
to test for correct ordering of data types inserted while filling forms etc.
at the backend. These tests are generally handled at frontend while web
development, but are recommended to be tested at backend as well. For this, we
sometimes, need to check for record’s data types according to their ordering.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using chainedif and isinstance()**  
This task can be performed using combination of above functionalities. In
this, we just need to test for the data type using the isintance(), and to
check each element of tuple we employ chained if statements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check order specific data type in tuple

# Using chained if and isinstance()

 

# Initializing tuple

test_tup = ('gfg', ['is', 'best'], 1)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# Check order specific data type in tuple

# Using chained if and isinstance()

res = isinstance(test_tup, tuple)\

 and isinstance(test_tup[0], str)\

 and isinstance(test_tup[1], list)\

 and isinstance(test_tup[2], int)

 

# printing result

print("Does all the instances match required data types in order ? : "
+ str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ('gfg', ['is', 'best'], 1)
    Does all the instances match required data types in order ? : True
    

**Method #2 : Using map() + type() + isinstance()**  
The combination of above functions can also be used to achieve this task. The
checking for types for each element in tuple is extended by map(). The
advantage of this method is that it allows us to define the data type ordering
beforehand as a list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check order specific data type in tuple

# Using map() + type() + isinstance()

 

# Initializing tuple

test_tup = ('gfg', ['is', 'best'], 1)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# data type order list 

data_list = [str, list, int]

 

# Check order specific data type in tuple

# Using map() + type() + isinstance()

res = isinstance(test_tup, tuple) and list(map(type,
test_tup)) == data_list

 

# printing result

print("Does all the instances match required data types in order ? : "
+ str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ('gfg', ['is', 'best'], 1)
    Does all the instances match required data types in order ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


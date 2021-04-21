Python | N element incremental tuples



Sometimes, while working with data, we can have a problem in which we require
to gather a data that is of the form of sequence of increasing element tuple
with each tuple containing the element N times. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using generator expression +tuple()**  
The combination of above functions can be used to perform this task. In this,
we need to iterate through N using generator expression and construction of
tuple using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# N element incremental tuples

# Using generator expression + tuple

 

# initialize N 

N = 3

 

# printing N

print("Number of times to repeat : " + str(N))

 

# N element incremental tuples

# Using generator expression + tuple

res = tuple((ele, ) * N for ele in range(1, 6))

 

# printing result

print("Tuple sequence : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Number of times to repeat : 3
    Tuple sequence : ((1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5))
    

**Method #2 : Usingrepeat() \+ list comprehension**  
This task can also be performed using combination of above functions. In this,
we use repeat() to repeat elements N times. And iteration is handled using
list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# N element incremental tuples

# Using generator expression + tuple

from itertools import repeat

 

# initialize N 

N = 3

 

# printing N

print("Number of times to repeat : " + str(N))

 

# N element incremental tuples

# Using generator expression + tuple

res = tuple(tuple(repeat(ele, N)) for ele in range(1,
6))

 

# printing result

print("Tuple sequence : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Number of times to repeat : 3
    Tuple sequence : ((1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5))
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


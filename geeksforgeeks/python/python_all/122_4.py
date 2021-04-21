Python | All possible N combination tuples



Sometimes, while working with Python tuples, we might have a problem in which
we need to generate all possible combination pairs till N. This can have
application in mathematics domain. Let’s discuss certain ways in which this
problem can be solved.

 **Method #1 : Using list comprehension +product()**  
This task can be performed using list comprehension which can be used to
iterate the container of N numbers and product() performs the task of
formation of combinations from them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All possible N combination tuples

# Using list comprehesion + product()

from itertools import product

 

# initialize N 

N = 3

 

# All possible N combination tuples

# Using list comprehesion + product()

res = [ele for ele in product(range(1, N + 1),
repeat = N)]

 

# printing result

print("Tuple Combinations till N are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> Tuple Combinations till N are : [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1),
> (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 3, 3), (2, 1, 1), (2, 1, 2),
> (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3),
> (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 1),
> (3, 3, 2), (3, 3, 3)]

  

  

**Method #2 : Usingproduct()**  
This task can also be performed by using just the single function. The use of
list comprehension can be eliminated using the conversion to list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All possible N combination tuples

# Using product()

from itertools import product

 

# initialize N 

N = 3

 

# All possible N combination tuples

# Using product()

res = list(product(range(1, N + 1), repeat = N))

 

# printing result

print("Tuple Combinations till N are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> Tuple Combinations till N are : [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1),
> (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 3, 3), (2, 1, 1), (2, 1, 2),
> (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3),
> (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 1),
> (3, 3, 2), (3, 3, 3)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Interval List Summation



There are numerous ways to initialize the list with the elements, but
sometimes, its required to initialize the lists with the numbers in a sliced
way and find its summation. This can be custom and hence knowledge of this can
come handy. Let’s discuss certain ways in which this can be done.

 **Method #1 : Using list comprehension +enumerate() + sum()**  
The list comprehension can do the possible iteration part and enumerate can
help in the part of logic and checking for the valid elements required in the
list. The sum() is used to perform summation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Interval List Summation

# using list comprehension + enumerate() + sum()

 

# initializing lists

test_list = list(range(50))

 

# printing original list

print ("The original list is : " + str(test_list))

 

# interval elements

N = 5

 

# interval difference

K = 15

 

# using list comprehension + enumerate() + sum()

# Interval List Summation

res = sum([i for j, i in enumerate(test_list) if j %
K < N ])

 

# printing result 

print ("The modified range sum list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
> 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
> 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]  
> The modified range sum list : 490

  

  

**Method #2 : Usingitertools.compress() + itertools.cycle() + sum()**  
The above two function can combine to facilitate the solution of the discussed
problem. The cycle function can to the task of repetition and the compress
function can be beneficial when it comes to clubbing the segments together.
The sum() is used to perform summation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Interval List Summation

# using itertools.compress() + itertools.cycle() + sum()

from itertools import compress, cycle 

 

# initializing lists

test_list = list(range(50))

 

# printing original list

print ("The original list is : " + str(test_list))

 

# interval elements

N = 5

 

# interval difference

K = 15

 

# using itertools.compress() + itertools.cycle() + sum()

# Interval List Summation 

func = cycle([True] * N + [False] * (K - N))

res = sum(list(compress(test_list, func)))

 

# printing result 

print ("The modified range sum list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
> 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
> 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]  
> The modified range sum list : 490

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Construct Cartesian Product Tuple list



Sometimes, while working with data, we need to create data as all possible
pairs of containers. This type of application comes from web development
domain. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
This is one-liner way to perform this particular task. In this, we just
shorten the task of loop in one line to generate all possible pairs of tuple
with list elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct Cartesian Product Tuple list

# using list comprehension

 

# initialize list and tuple 

test_list = [1, 4, 6, 7]

test_tup = (1, 3)

 

# printing original list and tuple 

print("The original list : " + str(test_list))

print("The original tuple : " + str(test_tup))

 

# Construct Cartesian Product Tuple list

# using list comprehension

res = [(a, b) for a in test_tup for b in test_list]

 

# printing result

print("The Cartesian Product is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [1, 4, 6, 7]  
> The original tuple : (1, 3)  
> The Cartesian Product is : [(1, 1), (1, 4), (1, 6), (1, 7), (3, 1), (3, 4),
> (3, 6), (3, 7)]

  

  

**Method #2 : Usingitertools.product()**  
This task can also be performed using the single function which internally
performs the task of returning the required Cartesian Product.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct Cartesian Product Tuple list

# using itertools.product()

from itertools import product

 

# initialize list and tuple 

test_list = [1, 4, 6, 7]

test_tup = (1, 3)

 

# printing original list and tuple 

print("The original list : " + str(test_list))

print("The original tuple : " + str(test_tup))

 

# Construct Cartesian Product Tuple list

# using itertools.product()

res = list(product(test_tup, test_list))

 

# printing result

print("The Cartesian Product is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [1, 4, 6, 7]  
> The original tuple : (1, 3)  
> The Cartesian Product is : [(1, 1), (1, 4), (1, 6), (1, 7), (3, 1), (3, 4),
> (3, 6), (3, 7)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


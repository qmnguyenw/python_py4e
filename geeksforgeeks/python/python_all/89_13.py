Python – Maximum product using K elements



Sometimes, while working with Python lists, we can have a problem in which we
need to maximize certain numbers. There can be many conditions of maximizing.
Example of that is maximizing product by using K elements. Lets discuss
certain ways in which this can be performed.

 **Method #1 : Usingmax() + sort() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform sort and then extract maximum by using the best initial or rear
elements using max().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum product using K elements

# using max() + sort() + list comprehension

 

# Initializing list

test_list = [8, 5, 9, 11, 3, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 3

 

# Maximum product using K elements

# using max() + sort() + list comprehension

test_list.sort()

res = max(test_list[0] * test_list[1] *
test_list[-1], test_list[-1] * test_list[-2] *
test_list[-3])

 

# printing result 

print ("Maximum product using K elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [8, 5, 9, 11, 3, 7]
    Maximum product using K elements : 792
    

**Method #2 : Using max() + reduce() + combination() \+ mul + list
comprehension**  
The combinations of above functions can be used to solve this problem. In
this, we extract each possible maximum using combinations and mul is used to
perform multiplication. This can be applied with any possible number of K and
is recommended method to solve this. Works only for Python 2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Maximum product using K elements

# using max() + reduce() + combination() + mul + list comprehension

from itertools import combinations

from operator import mul

 

# Initializing list

test_list = [8, 5, 9, 11, 3, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 4

 

# Maximum product using K elements

# using max() + reduce() + combination() + mul + list comprehension

res = max([reduce(mul, ele) for ele in
combinations(test_list, K)])

 

# printing result 

print ("Maximum product using K elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [8, 5, 9, 11, 3, 7]
    Maximum product using K elements : 5544
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


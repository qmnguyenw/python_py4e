Python – Subtract K from tuples list



Sometimes, while working with data, we can have a problem in which we need to
perform update operation on tuples. This can have application across many
domains such as web development. Let’s discuss certain ways in which
subtraction of K can be performed.

 **Method #1 : Using list comprehension**  
This is shorthand to brute function that can be applied to perform this task.
In this, we iterate for each element of each tuple to perform bulk subtraction
of K of data.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Subtract K from tuples list

# Using list comprehension

 

# initialize list

test_list = [(1, 3, 4), (2, 4, 6), (3, 8,
1)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize add element

K = 4

 

# Subtract K from tuples list

# Using list comprehension

res = [tuple(j - K for j in sub ) for sub in
test_list]

 

# printing result

print("List after subtraction of K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
    List after subtraction of K : [(-3, -1, 0), (-2, 0, 2), (-1, 4, -3)]
    

**Method #2 : Usingmap() \+ lambda + list comprehension**  
The combination of above functions can be used to perform this task. In this,
we just iterate for all elements using map() and extend logic of update
using lambda function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Subtract K from tuples list

# Using list comprehension + map() + lambda

 

# initialize list

test_list = [(1, 3, 4), (2, 4, 6), (3, 8,
1)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize add element

K = 4

 

# Subtract K from tuples list

# Using list comprehension + map() + lambda

res = [tuple(map(lambda ele : ele - K, sub)) for sub
in test_list]

 

# printing result

print("List after subtraction of K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
    List after subtraction of K : [(-3, -1, 0), (-2, 0, 2), (-1, 4, -3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Update each element in tuple list



Sometimes, while working with data, we can have a problem in which we need to
perform update operations on tuples. This can have applications across many
domains such as web development. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Using list comprehension**  
This is shorthand to brute function that can be applied to perform this task.
In this, we iterate for each element of each tuple to perform bulk update of
data.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Update each element in tuple list

# Using list comprehension

 

# initialize list

test_list = [(1, 3, 4), (2, 4, 6), (3, 8,
1)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize add element

add_ele = 4

 

# Update each element in tuple list

# Using list comprehension

res = [tuple(j + add_ele for j in sub ) for sub in
test_list]

 

# printing result

print("List after bulk update : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
    List after bulk update : [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
    

**Method #2 : Using map() \+ lambda + list comprehension**  
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

# Update each element in tuple list

# Using list comprehension + map() + lambda

 

# initialize list

test_list = [(1, 3, 4), (2, 4, 6), (3, 8,
1)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize add element

add_ele = 4

 

# Update each element in tuple list

# Using list comprehension + map() + lambda

res = [tuple(map(lambda ele : ele + add_ele, sub)) for
sub in test_list]

 

# printing result

print("List after bulk update : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
    List after bulk update : [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


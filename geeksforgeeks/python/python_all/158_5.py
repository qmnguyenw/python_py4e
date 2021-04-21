Python | Custom length Matrix



Sometimes, we need to initialize a matrix in Python of variable length from
the list containing elements. In this article, we will discuss the variable
length method initialization and certain shorthands to do so. Let’s discuss
certain ways to perform this.

 **Method #1 : Usingzip() \+ list comprehension**  
The zip function combined with the list comprehension can help to achieve this
particular task. The zip function can help to zip the counter list with the
element list and list comprehension does the work of construction of matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Custom length Matrix 

# using zip() + list comprehension

 

# initializing list

test_list = ['a', 'b', 'c']

 

# initializing counter list 

counter_list = [1, 4, 2]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# printing counter list 

print ("The counter list is : " + str(counter_list))

 

# using zip() + list comprehension

# Custom length Matrix 

res = [[i] * j for i, j in zip(test_list, counter_list)]

 

# printing result

print ("The custom length matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['a', 'b', 'c']
    The counter list is : [1, 4, 2]
    The custom length matrix is : [['a'], ['b', 'b', 'b', 'b'], ['c', 'c']]
    

**Method #2 : Usingmap() + mul operator**  
This particular problem can also be solved using the inbuilt mul operator
which performs multiplication of liked index elements and map function
performs the task of formation of matrix.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Custom length Matrix 

# using map() + mul operator

from operator import mul

 

# initializing list

test_list = ['a', 'b', 'c']

 

# initializing counter list 

counter_list = [1, 4, 2]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# printing counter list 

print ("The counter list is : " + str(counter_list))

 

# using map() + mul operator

# Custom length Matrix 

res = list(map(mul, [['a'], ['b'], ['c']],
counter_list))

 

# printing result

print ("The custom length matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['a', 'b', 'c']
    The counter list is : [1, 4, 2]
    The custom length matrix is : [['a'], ['b', 'b', 'b', 'b'], ['c', 'c']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


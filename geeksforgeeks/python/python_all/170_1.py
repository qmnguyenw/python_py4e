Python | Get indices of True values in a binary list



Boolean lists are often used by the developers to check for True values during
hashing. Boolean list is also used in certain dynamic programming paradigms in
dynamic programming. Let’s discuss certain ways to get indices of true values
in list in Python.

 **Method #1 : Usingenumerate() and list comprehension**

enumerate() can do the task of hashing index with its value and coupled with
list comprehension can let us check for the true values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to return true value indices.

# using enumerate() + list comprehension

 

# initializing list 

test_list = [True, False, True, False, True,
True, False]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using enumerate() + list comprehension

# to return true indices.

res = [i for i, val in enumerate(test_list) if val]

 

# printing result

print ("The list indices having True values are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [True, False, True, False, True, True, False]
    The list indices having True values are : [0, 2, 4, 5]
    

  
**Method #2 : Usinglambda + filter() + range()**

  

  

filter() function coupled with lambda can perform this task with help of
range function. range() function is used to traverse the entire list and
filter checks for true values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to return true value indices.

# using lambda + filter() + range()

 

# initializing list 

test_list = [True, False, True, False, True,
True, False]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using lambda + filter() + range()

# to return true indices.

res = list(filter(lambda i: test_list[i],
range(len(test_list))))

 

# printing result

print ("The list indices having True values are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [True, False, True, False, True, True, False]
    The list indices having True values are :  [0, 2, 4, 5]
    

  
**Method #3 : Usingitertools.compress()**

compress function checks for all the elements in list and returns the list
of indices with True values. This is most Pythonic and elegant way to perform
this particular task.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to return true value indices.

# using itertools.compress()

from itertools import compress

 

# initializing list 

test_list = [True, False, True, False, True,
True, False]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using itertools.compress()

# to return true indices.

res = list(compress(range(len(test_list)), test_list))

 

# printing result

print ("The list indices having True values are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [True, False, True, False, True, True, False]
    The list indices having True values are : [0, 2, 4, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


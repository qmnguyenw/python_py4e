Python – False indices in a boolean list



Boolean lists are often used by the developers to check for False values
during hashing. These have many applications in developers daily life. Boolean
list is also used in certain dynamic programming paradigms in dynamic
programming. Also in Machine Learing preprocessing of values. Lets discuss
certain ways to get indices of false values in list in Python.

 **Method #1 : Usingenumerate() and list comprehension**  
enumerate() can do the task of hashing index with its value and coupled with
list comprehension can let us check for the false values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# False indices

# using enumerate() + list comprehension

 

# initializing list 

test_list = [True, False, True, False, True,
True, False]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using enumerate() + list comprehension

# False indices

res = [i for i, val in enumerate(test_list) if not val]

 

# printing result

print ("The list indices having False values are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [True, False, True, False, True, True, False]
    The list indices having False values are : [1, 3, 6]
    

**Method #2 : Using lambda +filter() + range()**  
filter function coupled with lambda can perform this task with help of range
function. range function is used to traverse the entire list and filter checks
for false values.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# False indices

# using lambda + filter() + range()

 

# initializing list 

test_list = [True, False, True, False, True,
True, False]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using lambda + filter() + range()

# False indices

res = list(filter(lambda i: not test_list[i],
range(len(test_list))))

 

# printing result

print ("The list indices having False values are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [True, False, True, False, True, True, False]
    The list indices having False values are : [1, 3, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


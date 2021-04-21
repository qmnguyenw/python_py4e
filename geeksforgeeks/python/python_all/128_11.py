Python | Unpacking nested tuples



Sometimes, while working with Python list of tuples, we can have a problem in
which we require to unpack the packed tuples. This can have a possible
application in web development. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Using list comprehension**  
This task can be performed using list comprehension in which we iterate for
tuples and construct the desired tuple. This technique is useful in case we
know the exact number of tuple elements and positioning.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unpacking nested tuples

# using list comprehension

 

# initialize list

test_list = [(4, (5, 'Gfg')), (7, (8, 6))]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Unpacking nested tuples

# using list comprehension

res = [(x, y, z) for x, (y, z) in test_list]

 

# printing result

print("The unpacked nested tuple list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, (5, 'Gfg')), (7, (8, 6))]
    The unpacked nested tuple list is : [(4, 5, 'Gfg'), (7, 8, 6)]
    

**Method #2 : Using list comprehension + “*” operator**  
Many times, there might be a case in which we don’t know the exact number of
element in tuple and also the element count is variable among tuples. The “*”
operator can perform the task of this variable unpacking.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unpacking nested tuples

# using list comprehension + * operator

 

# initialize list

test_list = [(4, (5, 'Gfg')), (7, (8, 6))]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Unpacking nested tuples

# using list comprehension + * operator

res = [(z, *x) for z, x in test_list]

 

# printing result

print("The unpacked nested tuple list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, (5, 'Gfg')), (7, (8, 6))]
    The unpacked nested tuple list is : [(4, 5, 'Gfg'), (7, 8, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


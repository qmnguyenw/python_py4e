Python | Convert Triple nesting to Double nesting list



Sometimes, while working with lists, we can have a problem in which we need to
perform the flattening of nested list. This kind of problem have been
discussed many times. But sometimes, flattening can be from a triple to double
nesting as well. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension**  
This task can be performed using technique of list comprehension. In this, one
can just take the initial element of triple nested list and just unpack it to
double nested list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Triple nesting to Double nesting list

# using list comprehension

 

# initialize list

test_list = [[[1, 4, 6]], [[8, 9, 10, 7]]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Triple nesting to Double nesting list

# using list comprehension

res = [sub[0] for sub in test_list]

 

# printing result

print("Double nested list from triple nested : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[[1, 4, 6]], [[8, 9, 10, 7]]]
    Double nested list from triple nested : [[1, 4, 6], [8, 9, 10, 7]]
    

**Method #2 : Usingchain.from_iterable()**  
This task can also be performed using this function. This is the inbuilt
method that is made to perform the task of flattening a list and hence is
highly recommended to perform this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Triple nesting to Double nesting list

# using chain.from_iterable()

from itertools import chain

 

# initialize list

test_list = [[[1, 4, 6]], [[8, 9, 10, 7]]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Triple nesting to Double nesting list

# using list comprehension

res = list(chain.from_iterable(test_list))

 

# printing result

print("Double nested list from triple nested : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[[1, 4, 6]], [[8, 9, 10, 7]]]
    Double nested list from triple nested : [[1, 4, 6], [8, 9, 10, 7]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Flatten and Reverse Sort Matrix



The flattening of list of list has been discussed many times, but sometimes,
in addition to flattening, it is also required to get the string in reverse
sorted manner. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingsorted() + reverse \+ list comprehension**  
This idea is similar to flattening a list of list but in addition to it, we
add a sorted function along with reverse as key, to reverse sort the returned
flattened list done by list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Flatten and Reverse Sort Matrix

# using sorted + list comprehension

 

# initializing list of list 

test_list = [[3, 5], [7, 3, 9], [1, 12]]

 

# printing original list of list 

print("The original list : " + str(test_list))

 

# using sorted + list comprehension

# Flatten and Reverse Sort Matrix

res = sorted([j for i in test_list for j in i], reverse
= True)

 

# print result

print("The reverse sorted and flattened list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 5], [7, 3, 9], [1, 12]]
    The reverse sorted and flattened list : [12, 9, 7, 5, 3, 3, 1]
    

**Method #2 : Usingitertools.chain() + sorted() + reverse**  
The task that was done by list comprehension above can also be performed using
the chain function that links elements of list and then sorted function does
the task of sorting with the help of reverse for reverse sorting.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Flatten and Reverse Sort Matrix

# using itertools.chain() + sorted()

from itertools import chain

 

# initializing list of list 

test_list = [[3, 5], [7, 3, 9], [1, 12]]

 

# printing original list of list 

print("The original list : " + str(test_list))

 

# using itertools.chain() + sorted()

# Flatten and Reverse Sort Matrix

res = sorted(chain(*test_list), reverse = True)

 

# print result

print("The reverse sorted and flattened list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 5], [7, 3, 9], [1, 12]]
    The reverse sorted and flattened list : [12, 9, 7, 5, 3, 3, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


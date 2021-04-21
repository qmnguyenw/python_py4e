Python | Sort Flatten list of list



The flattening of list of lists has been discussed earlier, but sometimes, in
addition to flattening, it is also required to get the string in a sorted
manner. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingsorted() \+ list comprehension**  
This idea is similar to flattening a list of list but in addition to it, we
add a sorted function to sort the returned flattened list done by list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# sort flatten list of list 

# using sorted + list comprehension

 

# initializing list of list 

test_list = [[3, 5], [7, 3, 9], [1, 12]]

 

# printing original list of list 

print("The original list : " + str(test_list))

 

# using sorted + list comprehension

# sort flatten list of list

res = sorted([j for i in test_list for j in i])

 

# print result

print("The sorted and flattened list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 5], [7, 3, 9], [1, 12]]
    The sorted and flattened list : [1, 3, 3, 5, 7, 9, 12]
    

**Method #2 : Usingitertools.chain() + sorted()**  
The task that was done by list comprehension above can also be performed using
the chain function that links elements of list and then sorted function does
the task of sorting.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# sort flatten list of list 

# using itertools.chain() + sorted()

from itertools import chain

 

# initializing list of list 

test_list = [[3, 5], [7, 3, 9], [1, 12]]

 

# printing original list of list 

print("The original list : " + str(test_list))

 

# using itertools.chain() + sorted()

# sort flatten list of list

res = sorted(chain(*test_list))

 

# print result

print("The sorted and flattened list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 5], [7, 3, 9], [1, 12]]
    The sorted and flattened list : [1, 3, 3, 5, 7, 9, 12]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Delete elements in range



The deletion of a single element comparatively easier, but when we wish to
delete element in range, the task becomes a tedious once due to the
rearrangements and shifting of list elements automatically in python. Let’s
discuss certain ways in which elements can be deleted in range.  

 **Method #1 : Using del +sorted()**  
In this method, we reverse the list of indices we wish to delete and delete
them in the original list in backward manner so that the rearrangement of list
doesn’t destroy the integrity of the solution.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# range deletion of elements 

# using del + sorted()

 

# initializing list 

test_list = [3, 5, 6, 7, 2, 10]

 

# initializing indices

indices_list = [1, 4, 2]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# printing the indices list

print ("The indices list is : " + str(indices_list))

 

# using del + sorted()

# range deletion of elements

for i in sorted(indices_list, reverse = True):

 del test_list[i]

 

# printing result

print ("The modified deleted list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 5, 6, 7, 2, 10]
    The indices list is : [1, 4, 2]
    The modified deleted list is : [3, 7, 10]
    

  
**Method #2 : Usingenumerate() \+ list comprehension**  
This task can also be performed if we make a list that would not have the
elements in the delete list, i.e rather than actually deleting the elements,
we can remake it without them.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# range deletion of elements 

# using enumerate() + list comprehension

 

# initializing list 

test_list = [3, 5, 6, 7, 2, 10]

 

# initializing indices

indices_list = [1, 4, 2]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# printing the indices list

print ("The indices list is : " + str(indices_list))

 

# using enumerate() + list comprehension

# range deletion of elements

test_list[:] = [ j for i, j in enumerate(test_list)

 if i not in indices_list ]

 

# printing result

print ("The modified deleted list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 5, 6, 7, 2, 10]
    The indices list is : [1, 4, 2]
    The modified deleted list is : [3, 7, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save


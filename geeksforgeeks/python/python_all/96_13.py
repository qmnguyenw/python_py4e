Python | Remove Front K elements



We often come to the situations in which we need to decrease the size of the
list by truncating the first elements of the list. This particular problem
occurs when we need to optimize memory. This has its application in the day-
day programming when sometimes we require to get all the lists of similar
size. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usinglen() \+ list slicing**  
List slicing can perform this particular task in which we just slice the last
len(list) – K elements to be in the list and hence removing the first K
elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Remove Front K elements

# using len() + list slicing

 

# initializing list 

test_list = [1, 4, 6, 3, 5, 8]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using len() + list slicing

# Remove Front K elements

res = test_list[K:]

 

# printing result 

print ("The list after removing first K elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 6, 3, 5, 8]
    The list after removing first K elements : [3, 5, 8]
    

**Method #2 : Using Negative list slicing**  
We can perform this particular task using the negative list slicing in which
we start removing the elements from the first index of the list and hence
remove all the K elements from the first. We remove None if 0 elements are
asked to be removed.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Remove Front K elements

# using negative list slicing

 

# initializing list 

test_list = [1, 4, 6, 3, 5, 8]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using negative list slicing

# Remove Front K elements

res = test_list[-(len(test_list) - K) or None:]

 

# printing result 

print ("The list after removing first K elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 6, 3, 5, 8]
    The list after removing first K elements : [3, 5, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


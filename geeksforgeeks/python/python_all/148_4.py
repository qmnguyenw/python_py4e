Python | Remove given element from list of lists



The deletion of elementary elements from list has been dealt with many times,
but sometimes rather than having just a one list, we have list of list where
we need to perform this particular task. Having shorthands to perform this
particular task can help. Let’s discuss certain ways to perform this
particular task.

 **Method #1 : Using list comprehension**

The logic behind this kind of method is to reduce the size of code and do the
task to perform using loops as a way of list comprehension itself.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Removing element from list of lists

# using list comprehension

 

# initializing list

test_list = [[4, 5, 6], [5, 6, 4, 1],
[4], [4, 8, 9, 10]]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing Number to delete

N = 4

 

# using list comprehension

# Removing element from list of lists

res = [[ele for ele in sub if ele != N] for sub in
test_list]

 

# print result

print("The list after deletion of element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[4, 5, 6], [5, 6, 4, 1], [4], [4, 8, 9, 10]]
    The list after deletion of element : [[5, 6], [5, 6, 1], [], [8, 9, 10]]
    

  

  

**Method 2 : Using list comprehension + list slicing**  
In this method, we generally do the task similar to the above method, the
variation is just we use list slicing for better code readability.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Removing element from list of lists

# using list comprehension + list slicing

 

# initializing list

test_list = [[4, 5, 6], [5, 6, 4, 1],
[4], [4, 8, 9, 10]]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing Number to delete

N = 4

 

# using list comprehension + list slicing

# Removing element from list of lists

for sub in test_list:

 sub[:] = [ele for ele in sub if ele != N]

 

# print result

print("The list after deletion of element : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[4, 5, 6], [5, 6, 4, 1], [4], [4, 8, 9, 10]]
    The list after deletion of element : [[5, 6], [5, 6, 1], [], [8, 9, 10]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


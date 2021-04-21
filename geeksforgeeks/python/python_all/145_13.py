Python | Remove all occurrences in nested list



The task of removal of element generally doesn’t pose any challenge, but
sometimes, we may have a more complex problem than just removing a single
element or performing removal in just a normal list. Problem can be removing
all occurrences of nested list. Let’s discuss certain ways in which this
problem can be solved.

 **Method #1 : Using list comprehension**

The list comprehension can be used as a shorter method to the recommended
longer method in normal way of loops to perform this task in which we just
check for a match and reconstruct the list without the target list element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove all occurrences in nested list

# using list comprehension

 

# initializing list

test_list = [[4, 5], [1, 2, 3], [4, 5],
[8, 9], [10, 11]]

 

# initializing list to delete

del_list = [4, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# printing delete list 

print("The list to be deleted is : " + str(del_list))

 

# using list comprehension

# Remove all occurrences in nested list

res = [i for i in test_list if i != del_list]

 

# print result

print("The list after removal of list element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[4, 5], [1, 2, 3], [4, 5], [8, 9], [10, 11]]
    The list to be deleted is : [4, 5]
    The list after removal of list element : [[1, 2, 3], [8, 9], [10, 11]]
    

  

  

**Method #2 : Usingfilter() + partial() + operator.ne**

The task can also be performed using the above functions. The filter function
performs filtering, and returns the partial list by partial function and not
equal condition is imposed using the operator.ne method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove all occurrences in nested list

# using filter() + partial() + operator.ne

from functools import partial

from operator import ne

 

# initializing list

test_list = [[4, 5], [1, 2, 3], [4, 5],
[8, 9], [10, 11]]

 

# initializing list to delete

del_list = [4, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# printing delete list 

print("The list to be deleted is : " + str(del_list))

 

# using filter() + partial() + operator.ne

# Remove all occurrences in nested list

res = list(filter(partial(ne, del_list), test_list))

 

# print result

print("The list after removal of list element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[4, 5], [1, 2, 3], [4, 5], [8, 9], [10, 11]]
    The list to be deleted is : [4, 5]
    The list after removal of list element : [[1, 2, 3], [8, 9], [10, 11]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


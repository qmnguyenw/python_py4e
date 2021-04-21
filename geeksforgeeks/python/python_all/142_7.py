Python program to fetch the indices of true values in a Boolean list



Given a list of only boolean values, write a Python program to fetch all the
indices with True values from given list.

Let’s see certain ways to do this task.

 **Method #1:** Using itertools [Pythonic way]

itertools.compress() function checks for all the elements in list and
returns the list of indices with True values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to fetch the indices

# of true values in a Boolean list

from itertools import compress 

 

# initializing list 

bool_list = [False, True, False, True, True,
True] 

 

# printing given list 

print ("Given list is : " + str(bool_list)) 

 

# using itertools.compress() 

# to return true indices. 

res = list(compress(range(len(bool_list )), bool_list )) 

 

# printing result 

print ("Indices having True values are : " + str(res))   
  
---  
  
__

__

**Output:**

  

  

    
    
    Given list is : [False, True, False, True, True, True]
    Indices having True values are : [1, 3, 4, 5]
    


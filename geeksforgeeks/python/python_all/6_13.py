Python – Remove multiple elements from Set



Given a set, the task is to write a Python program remove multiple elements
from set.

 **Example:**

    
    
    Input : test_set = {6, 4, 2, 7, 9}, rem_ele = [2, 4, 8]
    Output : {9, 6, 7}
    
    Explanation : 2, 4 are removed from set.
    
    Input : test_set = {6, 4, 2, 7, 9}, rem_ele = [4, 8]
    Output : {2, 9, 6, 7}
    
    Explanation : 4 is removed from set.

 **Method #1 : Using “-” operator**

In this, we perform task of eliminating elements using computing difference
using “-” operator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove multiple elements from Set

# Using "-" operator

 

# initializing set

test_set = {6, 4, 2, 7, 9}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing remove elements

rem_ele = [2, 4, 8]

 

# using "-" operator to remove multiple elements

res = test_set - set(rem_ele)

 

# printing result

print("Set after removal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original set is : {2, 4, 6, 7, 9}
    Set after removal : {9, 6, 7}

 **Method #2 : Using difference_update()**

In this, we remove elements getting difference and updating the set using
inbuild set method difference_update().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove multiple elements from Set

# Using difference_update()

 

# initializing set

test_set = {6, 4, 2, 7, 9}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing remove elements

rem_ele = [2, 4, 8]

 

# using difference_update() to remove multiple elements

test_set.difference_update(set(rem_ele))

 

# printing result

print("Set after removal : " + str(test_set))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original set is : {2, 4, 6, 7, 9}
    Set after removal : {9, 6, 7}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


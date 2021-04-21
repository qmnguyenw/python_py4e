Python – Find Numbers in Range and not in Set



Given a set and range of numbers, the task is to write a Python program to
extract all numbers in range not in set.

 **Examples:**

    
    
     **Input :** test_set = {6, 4, 2, 7, 9}, low, high = 5, 10
    **Output :** [5, 8]
    **Explanation :** 6, 7 and 9 are present in set, remaining 5, 8 are in output.
    
    **Input :** test_set = {6, 4, 2, 7, 9}, low, high = 5, 8
    **Output :** [5]
    **Explanation :** 6 and 7 are present in set, remaining 5 is in output.

 **Method #1 : Using loop**

In this, we iterate for all the elements in range and using conditional
statements omit the elements from result which are not present in set.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Range Numbers not in set

# Using loop

 

# initializing set

test_set = {6, 4, 2, 7, 9}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing range

low, high = 5, 10

 

res = []

for ele in range(low, high):

 

 # getting elements not in set

 if ele not in test_set:

 res.append(ele)

 

# printing result

print("Elements not in set : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original set is : {2, 4, 6, 7, 9}
    Elements not in set : [5, 8]

 **Method #2 : Using “-” operator**

In this, we perform task of performing getting difference from range through
set elements using “-” operator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Range Numbers not in set

# Using "-" operator

 

# initializing set

test_set = {6, 4, 2, 7, 9}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing range

low, high = 5, 10

 

# using "-" operator to get difference

res = list(set(range(low, high)) - test_set)

 

# printing result

print("Elements not in set : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original set is : {2, 4, 6, 7, 9}
    Elements not in set : [8, 5]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Consecutive Missing elements Sum



Sometimes, we can get elements in range as input but some values are missing
in otherwise consecutive range. We might have a use case in which we need to
get summation of all the missing elements. Let’s discuss certain ways in which
this can be done.

 **Method #1 : Using list comprehension +sum()**  
We can perform the task of finding missing elements using the the range
function to get the maximum element fill and then insert the elements if there
is a miss. The summation is performed using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Missing elements Sum

# using list comprehension + sum()

 

# initializing list

test_list = [3, 5, 6, 8, 10]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + sum()

# Consecutive Missing elements Sum

res = sum([ele for ele in range(max(test_list) + 1)
if ele not in test_list])

 

# print result

print("The sum of missing elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 5, 6, 8, 10]
    The sum of missing elements : 23
    

**Method #2 : Usingset() + sum()**  
This problem can also be performed using the properties of difference of set
and then getting the elements that are missing in a range. The summation is
performed using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Missing elements Sum

# Using set() + sum()

 

# initializing list

test_list = [3, 5, 6, 8, 10]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using set() + sum()

# Consecutive Missing elements Sum

res = sum(list(set(range(max(test_list) + 1))
- set(test_list)))

 

# print result

print("The sum of missing elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 5, 6, 8, 10]
    The sum of missing elements : 23
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


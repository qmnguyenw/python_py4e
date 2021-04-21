Python – Dual Element row with Maximum difference



Sometimes, while working with Python Matrix, we can have Matrix with its
elements to be rows with just two elements and we may desire to get row with
elements having maximum difference. This can have application in many domains.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this we
iterate for each row and compute maximum and store row with larger difference
each time while iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dual Element row with Maximum difference

# using loop

 

# Initializing list

test_list = [[5, 10], [1, 3], [4, 11], [1,
2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Dual Element row with Maximum difference

# using loop

max_till = -float('inf')

res = []

for sub in test_list:

 if abs(sub[0] - sub[1]) > max_till:

 max_till = abs(sub[0] - sub[1])

 res = sub

 

# printing result 

print ("The maximum difference row is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[5, 10], [1, 3], [4, 11], [1, 2]]
    The maximum difference row is : [4, 11]
    

**Method #2 : Usingmax() \+ lambda + list comprehension**  
The combination of above functionalities can be used to perform this task. In
this, we perform the task of getting maximum using max() and lambda function
and list comprehension is used to perform task of iteration.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dual Element row with Maximum difference

# using max() + lambda + list comprehension

 

# Initializing list

test_list = [[5, 10], [1, 3], [4, 11], [1,
2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Dual Element row with Maximum difference

# using max() + lambda + list comprehension

res = max(test_list, key = lambda ele: abs(ele[0] -
ele[1]))

 

# printing result 

print ("The maximum difference row is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[5, 10], [1, 3], [4, 11], [1, 2]]
    The maximum difference row is : [4, 11]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


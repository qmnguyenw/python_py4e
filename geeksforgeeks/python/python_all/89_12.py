Python – Test if common values are greater than K



Sometimes, while working with Lists, we can have a problem in which we need to
track common elements in list. This is quite common and we often have
constructs to solve this. But sometimes, we require to consider two list as
matching if they contain aleast K matching elements. Lets discuss certain ways
in which this can be performed.

 **Method #1 : Usingset() + len()**  
The combination of above methods can be used to solve this task. In this we
first convert each list into set and then use len() to check if matching
elements are greater than K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if common values are greater than K

# using len() + set()

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'for', 'Geeks']

test_list2 = [1, 'Gfg', 2, 'Geeks']

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing K 

K = 2

 

# Test if common values are greater than K

# using len() + set()

res = len(set(test_list1) & set(test_list2)) >= K

 

# printing result 

print ("Are common elements greater than K ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['Gfg', 'is', 'for', 'Geeks']
    The original list 2 is : [1, 'Gfg', 2, 'Geeks']
    Are common elements greater than K ? : True
    

**Method #2 : Usingsum()**  
This is yet another way in which this problem can be solved. In this, we just
take count of all the column elements and sum them using sum() and then check
with K.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if common values are greater than K

# using sum()

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'for', 'Geeks']

test_list2 = [1, 'Gfg', 2, 'Geeks']

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing K 

K = 2

 

# Test if common values are greater than K

# using sum()

res = sum(i in test_list1 for i in test_list2) >= 2

 

# printing result 

print ("Are common elements greater than K ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['Gfg', 'is', 'for', 'Geeks']
    The original list 2 is : [1, 'Gfg', 2, 'Geeks']
    Are common elements greater than K ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


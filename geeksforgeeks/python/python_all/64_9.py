Python – Test Similar Data Type in Tuple



Sometimes, while working with Python tuples, we can have a problem in which we
need to test if all the elements in tuple have same data type. This kind of
problem can have application across all domains such as web development and
day-day programming. Let’s discuss certain ways in which this task can be
performed.

    
    
    **Input** : test_tuple = (5, 6, 7, 3, "Gfg")
    **Output** : False
    
    **Input** : test_tuple = (2, 3)
    **Output** : True
    

**Method #1 : Using loop +isinstance()**  
The combination of above functions can be used to solve this problem. In this,
we perform the checking of data types using isinstance() and iteration is done
as brute force way to account for all the elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Similar Data Type in Tuple

# Using isinstance() + loop

 

# initializing tuple

test_tuple = (5, 6, 7, 3, 5, 6)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Test Similar Data Type in Tuple

# Using isinstance() + loop

res = True

for ele in test_tuple:

 if not isinstance(ele, type(test_tuple[0])):

 res = False

 break

 

# printing result 

print("Do all elements have same type ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (5, 6, 7, 3, 5, 6)
    Do all elements have same type ? : True
    

**Method #2 : Usingall() + isinstance()**  
The combination of above functions can also be used to solve this problem. In
this, we test for all the values using all() and isinstance() is used to check
for data type.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Similar Data Type in Tuple

# Using all() + isinstance()

 

# initializing tuple

test_tuple = (5, 6, 7, 3, 5, 6)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Test Similar Data Type in Tuple

# Using all() + isinstance()

res = all(isinstance(ele, type(test_tuple[0])) for ele
in test_tuple)

 

# printing result 

print("Do all elements have same type ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (5, 6, 7, 3, 5, 6)
    Do all elements have same type ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


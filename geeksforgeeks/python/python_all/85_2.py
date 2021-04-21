Python – Matrix Data Type Rectification



Sometimes, while working with data, we can have problems in which we need to
perform rectification of list data types, i.e convert the Number Strings to
Numbers where necessary. This can occur in Matrix form as well. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +isdigit()**  
This is one of the way in which this task can be performed. In this, we
iterate each element of Matrix and check for digit string using typecasting
and then perform a conversion.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Matrix Data Type Rectification

# using isdigit() + list comprehension

 

# Initializing list

test_list = [['5', 'GFG'], ['1', '3'], ['is',
'11'], ['1', 'best']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Matrix Data Type Rectification

# using isdigit() + list comprehension

res = [[int(ele) if ele.isdigit() else ele for ele in
sub] for sub in test_list]

 

# printing result 

print ("The rectified Matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [['5', 'GFG'], ['1', '3'], ['is', '11'], ['1', 'best']]
    The rectified Matrix is : [[5, 'GFG'], [1, 3], ['is', 11], [1, 'best']]
    

**Method #2 : Usingmap() + isdigit()**  
This is yet another way in which this task can be performed. In this, we
extend the logic to each element using map() rather than list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Matrix Data Type Rectification

# using map() + isdigit()

 

# Initializing list

test_list = [['5', 'GFG'], ['1', '3'], ['is',
'11'], ['1', 'best']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Matrix Data Type Rectification

# using map() + isdigit()

res = [list(map(lambda ele: int(ele) if ele.isdigit()
else ele, sub)) for sub in test_list]

 

# printing result 

print ("The rectified Matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [['5', 'GFG'], ['1', '3'], ['is', '11'], ['1', 'best']]
    The rectified Matrix is : [[5, 'GFG'], [1, 3], ['is', 11], [1, 'best']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

